"""
reporter.py
Generación de reportes de auditoría IAM en consola y JSON
"""

import json
from datetime import datetime
from tabulate import tabulate


class Reporter:
    def __init__(self, results: dict, account_id: str):
        self.results = results
        self.account_id = account_id

    def print_summary(self):
        """Imprime el reporte completo en consola."""
        results = self.results

        # Resumen general
        total = results['total_users']
        issues = (
            len(results['users_without_mfa']) +
            len(results['old_access_keys']) +
            len(results['inactive_console_users'])
        )
        print(f"Total usuarios: {total} | Problemas encontrados: {issues}\n")

        # Usuarios sin MFA
        without_mfa = results['users_without_mfa']
        if without_mfa:
            print(f"🔴 USUARIOS SIN MFA ({len(without_mfa)}) — ¡RIESGO ALTO!")
            table = [[u['username'], u['created'], 'Sí' if u['has_console'] else 'No', u['risk']]
                     for u in without_mfa]
            print(tabulate(table, headers=['Usuario', 'Creado', 'Consola', 'Riesgo']))
            print()
        else:
            print("✅ Todos los usuarios tienen MFA habilitado\n")

        # Claves antiguas
        old_keys = results['old_access_keys']
        if old_keys:
            print(f"🟡 CLAVES DE ACCESO ANTIGUAS >90 días ({len(old_keys)})")
            table = [[k['username'], k['key_id'], k['created'], f"{k['age_days']} días"]
                     for k in old_keys]
            print(tabulate(table, headers=['Usuario', 'Clave (parcial)', 'Creada', 'Antigüedad']))
            print()
        else:
            print("✅ No hay claves de acceso antiguas\n")

        # Usuarios inactivos
        inactive = results['inactive_console_users']
        if inactive:
            print(f"🟡 USUARIOS INACTIVOS CON ACCESO A CONSOLA ({len(inactive)})")
            table = [[u['username'], u['last_login'], u['created']]
                     for u in inactive]
            print(tabulate(table, headers=['Usuario', 'Último Login', 'Creado']))
            print()
        else:
            print("✅ No hay usuarios inactivos con acceso a consola\n")

        # Recomendaciones
        print("--- RECOMENDACIONES ---")
        if without_mfa:
            print("1. Habilitar MFA para todos los usuarios con acceso a consola")
            print("   → aws iam create-virtual-mfa-device")
        if old_keys:
            print("2. Rotar claves de acceso antiguas (cada 90 días)")
            print("   → aws iam create-access-key --user-name <usuario>")
            print("   → aws iam delete-access-key --user-name <usuario> --access-key-id <clave-vieja>")
        if inactive:
            print("3. Revisar y desactivar usuarios inactivos")
            print("   → aws iam delete-login-profile --user-name <usuario>")

    def save_json(self, filename: str):
        """Guarda el reporte como JSON."""
        report = {
            'account_id': self.account_id,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_users': self.results['total_users'],
                'users_without_mfa': len(self.results['users_without_mfa']),
                'old_access_keys': len(self.results['old_access_keys']),
                'inactive_console_users': len(self.results['inactive_console_users']),
            },
            'details': self.results
        }

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
