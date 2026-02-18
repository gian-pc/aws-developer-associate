# Proyecto: iam-user-audit

Script de auditoría de seguridad IAM que detecta configuraciones inseguras en tu cuenta AWS.

## ¿Qué hace?

- Lista todos los usuarios IAM de la cuenta
- Detecta usuarios **sin MFA habilitado**
- Detecta usuarios con **claves de acceso antiguas** (más de 90 días)
- Detecta usuarios con **acceso a consola pero sin actividad reciente**
- Genera un reporte en formato JSON y una tabla en consola

## Prerrequisitos

```bash
pip install boto3 tabulate
```

Tu usuario/rol IAM necesita estos permisos:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListUsers",
        "iam:ListMFADevices",
        "iam:ListAccessKeys",
        "iam:GetLoginProfile",
        "iam:GetUser",
        "iam:GenerateCredentialReport",
        "iam:GetCredentialReport"
      ],
      "Resource": "*"
    }
  ]
}
```

## Cómo ejecutar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar auditoría
python src/audit.py

# Guardar reporte en archivo
python src/audit.py --output reporte.json
```

## Salida esperada

```
=== AWS IAM Security Audit ===
Cuenta: 123456789012
Fecha: 2024-01-15 10:30:00

USUARIOS SIN MFA (¡RIESGO ALTO!):
+----------+---------------------+-----------------+
| Usuario  | Creado              | Tiene Consola   |
+----------+---------------------+-----------------+
| juan     | 2023-06-01          | Sí              |
| maria    | 2023-08-15          | Sí              |
+----------+---------------------+-----------------+

CLAVES DE ACCESO ANTIGUAS (>90 días):
+----------+----------------+------------------+
| Usuario  | Clave          | Última Rotación  |
+----------+----------------+------------------+
| carlos   | AKIA...XXXX    | 2023-01-01       |
+----------+----------------+------------------+

Reporte guardado en: reporte.json
```

## Estructura del código

```
proyecto/
├── README.md
├── requirements.txt
└── src/
    ├── audit.py          # Script principal
    ├── iam_checker.py    # Funciones de verificación
    └── reporter.py       # Generación de reportes
```

## Reto extra

Una vez que el script funcione, añade:
1. Enviar el reporte por email usando **Amazon SES**
2. Guardar el reporte en un **bucket S3**
3. Programar la ejecución con **EventBridge** (lo verás en módulos posteriores)
