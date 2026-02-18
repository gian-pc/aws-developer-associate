"""
iam_checker.py
Funciones de verificación de seguridad IAM

Conceptos clave de boto3 que practicas aquí:
- Paginación con paginators (los resultados vienen en "páginas")
- Manejo de excepciones de AWS (botocore.exceptions)
- Trabajo con fechas timezone-aware
"""

import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timezone, timedelta


class IamChecker:
    def __init__(self):
        # boto3 buscará credenciales en el orden estándar:
        # 1. Variables de entorno
        # 2. ~/.aws/credentials
        # 3. IAM Role (si estás en EC2/Lambda)
        self.iam = boto3.client('iam')
        self.KEY_AGE_THRESHOLD_DAYS = 90

    def run_all_checks(self) -> dict:
        """Ejecuta todas las verificaciones y retorna los resultados."""
        print("Ejecutando verificaciones...")

        users = self._list_all_users()
        print(f"  ✓ Usuarios encontrados: {len(users)}")

        users_without_mfa = self._check_mfa(users)
        print(f"  ✓ Usuarios sin MFA: {len(users_without_mfa)}")

        old_keys = self._check_old_access_keys(users)
        print(f"  ✓ Claves antiguas (>90 días): {len(old_keys)}")

        inactive_console = self._check_inactive_console_users(users)
        print(f"  ✓ Usuarios inactivos con acceso a consola: {len(inactive_console)}")

        root_mfa = self.check_root_mfa()
        print(f"  ✓ MFA en cuenta root: {'✅ Sí' if root_mfa else '🔴 NO — CRÍTICO'}")

        return {
            'total_users': len(users),
            'users_without_mfa': users_without_mfa,
            'old_access_keys': old_keys,
            'inactive_console_users': inactive_console,
            'root_mfa_enabled': root_mfa,
        }

    def _list_all_users(self) -> list:
        """
        Lista todos los usuarios usando paginación.

        CONCEPTO IMPORTANTE: La API de AWS devuelve max 100 resultados
        por llamada. Los paginators manejan esto automáticamente.
        """
        users = []
        # Usar paginator en lugar de list_users() directamente
        paginator = self.iam.get_paginator('list_users')

        for page in paginator.paginate():
            users.extend(page['Users'])

        return users

    def _check_mfa(self, users: list) -> list:
        """
        Verifica qué usuarios tienen MFA habilitado.

        Para el examen: MFA es obligatorio para una cuenta segura,
        especialmente para usuarios con acceso a la consola.
        """
        users_without_mfa = []

        for user in users:
            username = user['UserName']

            # Verificar si tiene acceso a consola (login profile)
            has_console = self._has_console_access(username)

            # Verificar dispositivos MFA
            try:
                response = self.iam.list_mfa_devices(UserName=username)
                has_mfa = len(response['MFADevices']) > 0
            except ClientError as e:
                print(f"  ⚠ Error verificando MFA de {username}: {e}")
                has_mfa = False

            if not has_mfa:
                users_without_mfa.append({
                    'username': username,
                    'created': user['CreateDate'].strftime('%Y-%m-%d'),
                    'has_console': has_console,
                    'risk': 'HIGH' if has_console else 'MEDIUM'
                })

        return users_without_mfa

    def _check_old_access_keys(self, users: list) -> list:
        """
        Detecta claves de acceso que no han sido rotadas en 90+ días.

        Para el examen: Las claves deben rotarse regularmente.
        Usar IAM Credential Report para auditar esto a escala.
        """
        old_keys = []
        threshold = datetime.now(timezone.utc) - timedelta(days=self.KEY_AGE_THRESHOLD_DAYS)

        for user in users:
            username = user['UserName']

            try:
                response = self.iam.list_access_keys(UserName=username)
                for key in response['AccessKeyMetadata']:
                    if key['Status'] == 'Active':
                        create_date = key['CreateDate']
                        age_days = (datetime.now(timezone.utc) - create_date).days

                        if create_date < threshold:
                            old_keys.append({
                                'username': username,
                                'key_id': key['AccessKeyId'][:8] + '...',
                                'created': create_date.strftime('%Y-%m-%d'),
                                'age_days': age_days,
                            })
            except ClientError as e:
                print(f"  ⚠ Error verificando claves de {username}: {e}")

        return old_keys

    def _check_inactive_console_users(self, users: list) -> list:
        """
        Detecta usuarios con acceso a consola pero sin actividad reciente.
        Inactivo = no ha iniciado sesión en los últimos 90 días.
        """
        inactive = []
        threshold = datetime.now(timezone.utc) - timedelta(days=90)

        for user in users:
            username = user['UserName']

            if not self._has_console_access(username):
                continue

            # PasswordLastUsed puede no existir si nunca ha iniciado sesión
            last_used = user.get('PasswordLastUsed')

            if last_used is None:
                # Nunca ha iniciado sesión
                inactive.append({
                    'username': username,
                    'last_login': 'Nunca',
                    'created': user['CreateDate'].strftime('%Y-%m-%d'),
                })
            elif last_used < threshold:
                inactive.append({
                    'username': username,
                    'last_login': last_used.strftime('%Y-%m-%d'),
                    'created': user['CreateDate'].strftime('%Y-%m-%d'),
                })

        return inactive

    def _has_console_access(self, username: str) -> bool:
        """Verifica si un usuario tiene acceso a la consola de AWS."""
        try:
            self.iam.get_login_profile(UserName=username)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchEntity':
                return False
            raise
    
    def check_root_mfa(self) -> bool:
        """
        Verifica si la cuenta ROOT tiene MFA habilitado.
        El root es el mayor riesgo de seguridad en AWS.
        """
        response = self.iam.get_account_summary()
        root_mfa = response['SummaryMap'].get('AccountMFAEnabled', 0)
        return root_mfa == 1
