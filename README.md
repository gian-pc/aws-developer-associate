# 🚀 AWS Certified Developer Associate — Plan de Estudio con Proyectos Prácticos

> **Basado en:** Curso de Stephane Maarek & Joan Amengual (938 páginas)
> **Enfoque:** Aprender haciendo — cada módulo tiene teoría + proyecto práctico en Python
> **Duración estimada:** 12 semanas (8+ horas/semana)
> **Objetivo:** Aprobar el examen AWS Certified Developer - Associate

---

## 📁 Estructura del Repositorio

```
aws-developer-associate/
│
├── README.md                    ← Este archivo (roadmap general)
│
├── modulo-01-iam/
│   ├── README.md                ← Notas teóricas del módulo
│   ├── proyecto/                ← Código del proyecto práctico
│   └── notas-examen.md          ← Puntos clave para el examen
│
├── modulo-02-ec2/
├── modulo-03-s3/
├── modulo-04-rds-dynamodb/
├── modulo-05-lambda/
├── modulo-06-api-gateway/
├── modulo-07-sqs-sns-kinesis/
├── modulo-08-ecs-beanstalk/
├── modulo-09-cloudformation-cdk/
├── modulo-10-cicd/
├── modulo-11-monitoring/
└── modulo-12-security/
```

---

## 🗺️ Roadmap Completo (12 Semanas)

### FASE 1 — Fundamentos (Semanas 1-2)

#### 📌 Módulo 01: IAM + CLI/SDK
**PDF:** Páginas 21–38 + 246–260

**Teoría:**
- Usuarios, grupos y roles
- Políticas IAM (Allow/Deny, JSON)
- MFA y acceso seguro
- AWS CLI y SDK con Python (boto3)
- Claves de acceso y buenas prácticas

**🏗️ Proyecto: `iam-user-audit`**
Script Python con boto3 que:
- Lista todos los usuarios IAM y sus grupos
- Detecta usuarios sin MFA habilitado
- Genera un reporte en JSON/CSV
- Envía alerta si hay usuarios sin MFA

**Habilidades adquiridas:** boto3, políticas IAM, seguridad básica

---

#### 📌 Módulo 02: EC2 + EBS + Redes
**PDF:** Páginas 39–144

**Teoría:**
- Tipos de instancias EC2 (On-Demand, Reserved, Spot)
- AMIs, User Data, Metadata
- Grupos de seguridad (Security Groups)
- Elastic IPs, ENI
- Volúmenes EBS (gp2, gp3, io1, io2)
- EBS Snapshots y AMI personalizada

**🏗️ Proyecto: `ec2-web-server-automation`**
Script Python con boto3 que:
- Crea y configura una instancia EC2 automáticamente
- Instala un servidor web con User Data
- Adjunta un volumen EBS adicional
- Crea un snapshot de backup automático

**Habilidades adquiridas:** EC2, EBS, automatización de infraestructura

---

### FASE 2 — Storage y Networking (Semanas 3-4)

#### 📌 Módulo 03: Amazon S3 (Básico + Avanzado + Seguridad)
**PDF:** Páginas 221–293

**Teoría:**
- Buckets, objetos, versionado
- Clases de almacenamiento (Standard, IA, Glacier)
- Ciclo de vida (Lifecycle Rules)
- Políticas de bucket y ACLs
- S3 Encryption (SSE-S3, SSE-KMS, SSE-C)
- Pre-signed URLs, CORS
- S3 Event Notifications
- S3 Transfer Acceleration, Multipart Upload

**🏗️ Proyecto: `s3-file-manager`**
Aplicación Python que:
- Sube archivos con multipart upload para archivos grandes
- Genera pre-signed URLs con expiración configurable
- Configura ciclo de vida automático (mover a Glacier después de 90 días)
- Configura notificaciones S3 → Lambda (preparación para módulo Lambda)

**Habilidades adquiridas:** S3 avanzado, cifrado, gestión de objetos

---

#### 📌 Módulo 04: Route 53 + CloudFront
**PDF:** Páginas 173–220 + 294–323

**Teoría:**
- DNS y registros (A, AAAA, CNAME, Alias)
- Routing policies (Simple, Weighted, Latency, Failover)
- Health Checks
- CloudFront: Distributions, Origins, Cache Behaviors
- Edge Locations y cómo funciona el caché
- CloudFront + S3 (Origin Access Identity)
- Lambda@Edge

**🏗️ Proyecto: `static-website-cdn`**
Deploy completo:
- Website estático subido a S3
- CloudFront distribution apuntando al bucket
- Configurar cache behaviors y TTL
- Script para invalidar caché de CloudFront

**Habilidades adquiridas:** CDN, DNS, optimización de entrega de contenido

---

### FASE 3 — Bases de Datos (Semana 5)

#### 📌 Módulo 05: RDS + Aurora + ElastiCache + DynamoDB
**PDF:** Páginas 145–172 + 630–683

**Teoría:**
- RDS (MySQL, PostgreSQL) — Multi-AZ, Read Replicas
- Aurora — características y ventajas
- ElastiCache — Redis vs Memcached, patrones de caché
- DynamoDB — tablas, items, atributos
- DynamoDB — Primary Key, GSI, LSI
- DynamoDB Streams, TTL
- DynamoDB — Query vs Scan, operaciones de escritura
- DynamoDB Accelerator (DAX)
- Provisioned vs On-Demand capacity

**🏗️ Proyecto: `serverless-todo-api-backend`**
Backend de una app de tareas con DynamoDB:
- Tabla DynamoDB con GSI por usuario
- CRUD completo con Python/boto3
- TTL para tareas completadas hace más de 30 días
- DynamoDB Streams para auditoría de cambios

**Habilidades adquiridas:** DynamoDB avanzado, diseño de tablas NoSQL

---

### FASE 4 — Serverless (Semanas 6-7)

#### 📌 Módulo 06: AWS Lambda
**PDF:** Páginas 555–629

**Teoría:**
- Modelos de invocación (sync, async, event source mapping)
- Variables de entorno y parámetros
- Límites de Lambda (tiempo, memoria, tamaño)
- Lambda Layers
- Concurrencia (reservada y provisionada)
- Lambda + VPC
- Lambda Destinations
- Cold start y optimizaciones

**🏗️ Proyecto: `image-processing-pipeline`**
Pipeline de procesamiento de imágenes:
- Lambda se activa con S3 Event cuando se sube imagen
- Crea thumbnail de la imagen
- Guarda metadata en DynamoDB
- Envía notificación con SNS al completar

**Habilidades adquiridas:** Lambda avanzado, event-driven architecture

---

#### 📌 Módulo 07: API Gateway
**PDF:** Páginas 684–727

**Teoría:**
- REST vs HTTP vs WebSocket APIs
- Stages y variables de stage
- Mapping templates, modelos
- Autenticación (IAM, Cognito, Lambda Authorizer)
- API Gateway + Lambda Proxy Integration
- Rate limiting y throttling
- CORS en API Gateway
- Canary deployments

**🏗️ Proyecto: `rest-api-completa`**
API REST completa:
- Conecta API Gateway con Lambda (módulo anterior)
- CRUD de tareas usando la tabla DynamoDB
- Autenticación con Lambda Authorizer
- Stages (dev, prod) con variables de entorno distintas
- Swagger/OpenAPI export

**Habilidades adquiridas:** APIs serverless, autenticación, stages

---

### FASE 5 — Mensajería y Eventos (Semana 8)

#### 📌 Módulo 08: SQS + SNS + Kinesis + Step Functions
**PDF:** Páginas 492–554 + 826–848

**Teoría:**
- SQS: Standard vs FIFO, Dead Letter Queue, Visibility Timeout
- SNS: Topics, Subscriptions, Fan-out pattern
- Kinesis: Data Streams, Firehose, Analytics
- Diferencias entre SQS, SNS y Kinesis
- Step Functions: State machines, tipos de estados

**🏗️ Proyecto: `order-processing-system`**
Sistema de procesamiento de pedidos:
- SNS topic para nuevos pedidos
- SQS queues suscritas (procesamiento de pago + inventario)
- Lambda procesa cada queue con Dead Letter Queue
- Step Functions orquesta el flujo de pedido completo

**Habilidades adquiridas:** Arquitecturas desacopladas, mensajería asíncrona

---

### FASE 6 — Contenedores y Deploy (Semana 9)

#### 📌 Módulo 09: ECS + ECR + Elastic Beanstalk
**PDF:** Páginas 324–395

**Teoría:**
- Docker básico y por qué usarlo en AWS
- ECS: Tasks, Services, Clusters
- Fargate vs EC2 Launch Type
- ECR: Push/Pull de imágenes
- IAM roles para ECS Tasks
- Elastic Beanstalk: plataformas, entornos
- Beanstalk deployments (Rolling, Blue/Green)
- .ebextensions para configuración

**🏗️ Proyecto: `containerized-api`**
Containerizar la API del módulo anterior:
- Crear Dockerfile para la app Flask/FastAPI
- Push a ECR con boto3/CLI
- Deploy en ECS Fargate
- Load Balancer delante del servicio ECS

**Habilidades adquiridas:** Contenedores en AWS, Fargate, ECR

---

### FASE 7 — Infraestructura como Código (Semana 10)

#### 📌 Módulo 10: CloudFormation + CDK
**PDF:** Páginas 396–440 + 790–801

**Teoría:**
- CloudFormation: Templates, Stacks, Change Sets
- Recursos, parámetros, outputs, mappings
- Nested Stacks
- CloudFormation Drift Detection
- SAM (Serverless Application Model)
- CDK: Constructs, Stacks, App
- CDK vs CloudFormation vs SAM

**🏗️ Proyecto: `infra-as-code-stack`**
Recrear toda la infraestructura con CDK:
- Stack con DynamoDB + Lambda + API Gateway
- Stack con S3 + CloudFront
- Pipeline de deploy automatizado
- Comparativa CDK vs CloudFormation puro

**Habilidades adquiridas:** IaC, reproducibilidad, CDK Python

---

### FASE 8 — CI/CD y Monitoreo (Semana 11)

#### 📌 Módulo 11: CodeCommit + CodeBuild + CodeDeploy + CodePipeline + CloudWatch + X-Ray
**PDF:** Páginas 728–789 + 441–491

**Teoría:**
- CodeCommit: repositorio Git en AWS
- CodeBuild: compilación y tests (buildspec.yml)
- CodeDeploy: estrategias (In-Place, Blue/Green)
- CodePipeline: pipeline completo de CI/CD
- CloudWatch: Métricas, Alarmas, Logs, Dashboards
- CloudWatch Events / EventBridge
- X-Ray: trazas distribuidas, segments, subsegments
- CloudTrail: auditoría de API calls

**🏗️ Proyecto: `cicd-pipeline-completo`**
Pipeline CI/CD para el proyecto anterior:
- Código en CodeCommit (o GitHub como source)
- CodeBuild corre tests y construye imagen Docker
- CodeDeploy hace Blue/Green deployment en ECS
- CodePipeline orquesta todo el flujo
- Alarmas de CloudWatch para errores 5xx
- X-Ray habilitado en Lambda y API Gateway

**Habilidades adquiridas:** DevOps completo, observabilidad

---

### FASE 9 — Seguridad y Repaso (Semana 12)

#### 📌 Módulo 12: Cognito + KMS + SSM + Identidad Avanzada
**PDF:** Páginas 802–928

**Teoría:**
- Cognito User Pools vs Identity Pools
- JWT tokens y flujos de autenticación
- KMS: Customer Managed Keys, Key Rotation
- Envelope Encryption
- SSM Parameter Store vs Secrets Manager
- STS: AssumeRole, Cross-Account Access
- IAM avanzado: Resource-based policies, Permission Boundaries

**🏗️ Proyecto: `secure-app-completa`**
Añadir seguridad enterprise a la API:
- Cognito User Pool para registro/login de usuarios
- Reemplazar Lambda Authorizer con Cognito Authorizer
- Secretos de DB en SSM Parameter Store (no en código)
- Cifrado de datos en DynamoDB con KMS CMK
- Cross-account role para staging vs producción

**Habilidades adquiridas:** Seguridad AWS, gestión de secretos, identidad

---

## 🏆 Proyecto Final: `aws-full-stack-app`

Al terminar los 12 módulos construirás una aplicación completa que use:

- **Frontend:** S3 + CloudFront
- **Auth:** Cognito
- **API:** API Gateway + Lambda
- **DB:** DynamoDB
- **Mensajería:** SQS + SNS
- **Infra:** CDK
- **CI/CD:** CodePipeline completo
- **Monitoreo:** CloudWatch + X-Ray
- **Seguridad:** KMS + SSM + IAM avanzado

---

## 📋 Cómo usar este repositorio

Cada módulo tiene su propia carpeta con:

```
modulo-XX-nombre/
├── README.md          # Teoría resumida + notas para el examen
├── notas-examen.md    # Puntos clave, gotchas y tips del examen
└── proyecto/
    ├── README.md      # Instrucciones del proyecto
    ├── src/           # Código Python
    ├── requirements.txt
    └── deploy/        # Scripts de deploy / CloudFormation / CDK
```

## 🎯 Tips para el Examen

1. AWS recomienda **1-2 años de experiencia** práctica en desarrollo con AWS
2. El examen dura **130 minutos** con **65 preguntas**
3. Puntuación mínima aprobatoria: **720/1000**
4. Dominios del examen:
   - Development with AWS Services (32%)
   - Security (26%)
   - Deployment (24%)
   - Troubleshooting and Optimization (18%)

## 🔗 Recursos Adicionales

- [AWS Certified Developer Study Guide](https://aws.amazon.com/certification/certified-developer-associate/)
- [AWS Free Tier](https://aws.amazon.com/free/) — Usa esto para todos los proyectos
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS SDK for Python Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python)

---

> 💡 **Consejo:** Commit cada proyecto que completes con el tag `modulo-XX-completado` para trackear tu progreso.
