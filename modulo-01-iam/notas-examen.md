# Notas para el Examen — Módulo 01: IAM

## Reglas de oro IAM

- **Root account**: NUNCA usar en el día a día. Solo para la cuenta inicial.
- **Un Deny explícito SIEMPRE gana** sobre cualquier Allow.
- **Por defecto todo está denegado** — si no hay Allow explícito, está denegado.
- IAM es **global**, no tiene regiones.

## Roles vs Usuarios

| Situación | Usar |
|-----------|------|
| EC2 necesita acceder a S3 | **Rol IAM** (Instance Profile) |
| Lambda necesita escribir en DynamoDB | **Rol IAM** para Lambda |
| Desarrollador accede a la consola | **Usuario IAM** con MFA |

**NUNCA** hardcodear claves de acceso en código. Siempre usar roles.

## ARN de S3 — Gotcha frecuente

```
arn:aws:s3:::mi-bucket        ← Para ListBucket
arn:aws:s3:::mi-bucket/*      ← Para GetObject/PutObject
```
Necesitas AMBOS si quieres listar y leer objetos.

## STS (Security Token Service)

- `AssumeRole`: Obtener credenciales temporales de un rol
- `GetSessionToken`: Credenciales temporales con MFA
- `AssumeRoleWithWebIdentity`: Usuarios federados (Cognito, Google)

## Cadena de credenciales boto3 (en orden)

1. Variables de entorno
2. Archivo `~/.aws/credentials`
3. **Rol IAM / Instance Profile** (EC2, Lambda, ECS)

## Preguntas típicas del examen

**Q: Un usuario tiene Allow ec2:* pero Deny ec2:TerminateInstances. ¿Puede terminar instancias?**
A: **No.** Deny siempre gana.

**Q: Una EC2 necesita leer de S3. ¿Mejor práctica?**
A: **IAM Role** como Instance Profile. NUNCA claves de acceso en el código.

**Q: ¿Qué servicio da credenciales temporales?**
A: **STS (Security Token Service)**

## Checklist

- [ ] Usuario IAM creado (no usar root)
- [ ] MFA habilitado en root y en mi usuario
- [ ] AWS CLI configurado
- [ ] boto3 instalado y funcionando
- [ ] Proyecto completado y en GitHub con tag `modulo-01-completado`
