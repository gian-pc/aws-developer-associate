# Módulo 01 — IAM: Identity and Access Management

> **PDF de referencia:** Páginas 21–38 (IAM) + 246–260 (CLI, SDK, Políticas IAM)
> **Semana:** 1 de 12
> **Proyecto:** `iam-user-audit` — Script de auditoría de usuarios IAM

---

## 🎯 Objetivos del Módulo

Al terminar este módulo deberás ser capaz de:
- Crear y gestionar usuarios, grupos y roles IAM
- Escribir políticas IAM en JSON
- Usar AWS CLI y boto3 (SDK de Python)
- Seguir el principio de mínimo privilegio
- Identificar configuraciones inseguras de IAM

---

## 📚 Teoría

### ¿Qué es IAM?

IAM es un servicio **global** (no está ligado a ninguna región) que controla **quién puede hacer qué** en tu cuenta de AWS.

**Entidades principales:**

| Entidad | Descripción | Caso de uso |
|---------|-------------|-------------|
| **Usuario** | Persona o aplicación con credenciales permanentes | Desarrollador que accede a la consola |
| **Grupo** | Colección de usuarios | Equipo de desarrollo, equipo de ops |
| **Rol** | Conjunto de permisos asumible temporalmente | Lambda necesita leer S3 |
| **Política** | Documento JSON que define permisos | Allow s3:GetObject en mi-bucket |

### Estructura de una Política IAM

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PermitirLecturaS3",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::mi-bucket",
        "arn:aws:s3:::mi-bucket/*"
      ]
    }
  ]
}
```

**Elementos clave:**
- `Version`: Siempre `"2012-10-17"` para políticas modernas
- `Effect`: `"Allow"` o `"Deny"` — **Deny siempre gana sobre Allow**
- `Action`: Qué operaciones (puede usar wildcards: `s3:*`, `ec2:Describe*`)
- `Resource`: ARN del recurso. `"*"` significa cualquier recurso

### Tipos de Políticas

1. **Identity-based policies**: Adjuntas a usuarios, grupos o roles
2. **Resource-based policies**: Adjuntas a recursos (ej: bucket policy de S3)
3. **Permission Boundaries**: Límite máximo de permisos que puede tener un usuario/rol
4. **Service Control Policies (SCP)**: Solo en AWS Organizations

### Regla de evaluación de permisos

```
¿Hay un DENY explícito? → Denegar
¿Hay un ALLOW explícito? → Permitir
Por defecto → Denegar implícito (todo está denegado si no se permite)
```

### Roles IAM — El concepto más importante para el examen

Los roles son **temporales** y los asumen servicios o usuarios:

```
Lambda  → asume rol → puede acceder a DynamoDB
EC2     → asume rol → puede escribir en S3
Usuario cuenta A → asume rol en cuenta B → Cross-account access
```

**¿Por qué usar roles en lugar de claves de acceso?**
- Las credenciales de rol son **temporales** (expiran solas)
- No hay credenciales que guardar en el código
- Más seguro y más fácil de revocar

### AWS CLI — Comandos esenciales

```bash
# Configurar credenciales
aws configure

# Listar usuarios IAM
aws iam list-users

# Ver políticas de un usuario
aws iam list-attached-user-policies --user-name juan

# Asumir un rol
aws sts assume-role \
  --role-arn arn:aws:iam::123456789:role/MiRol \
  --role-session-name mi-sesion
```

### boto3 — SDK de Python para AWS

```python
import boto3

# Cliente IAM
iam = boto3.client('iam')

# Listar usuarios (con paginación)
paginator = iam.get_paginator('list_users')
for page in paginator.paginate():
    for user in page['Users']:
        print(user['UserName'])

# Verificar si un usuario tiene MFA
mfa_devices = iam.list_mfa_devices(UserName='juan')
has_mfa = len(mfa_devices['MFADevices']) > 0
```

---

## 🏗️ Proyecto: `iam-user-audit`

Script de auditoría de seguridad IAM que detecta configuraciones inseguras.

Ver instrucciones en: [proyecto/README.md](./proyecto/README.md)

### Lo que aprenderás construyendo este proyecto:
- Usar boto3 para interactuar con IAM
- Paginación de resultados en AWS API
- Estructurar un script Python profesional
- Manejar errores y excepciones de AWS

---

## 📝 Notas para el Examen

Ver: [notas-examen.md](./notas-examen.md)
