# Estructura del Proyecto - Clean Architecture

## 📁 Árbol de Directorios

```
master-data-science-uai/
│
├── 📂 vidaSegura/                    # Módulo principal de Vida Segura
│   │
│   ├── 📂 src/                       # Código fuente
│   │   ├── 📂 domain/                # Capa de Dominio
│   │   │   └── form-schemas.js       # Esquemas y entidades
│   │   │
│   │   ├── 📂 application/           # Capa de Aplicación
│   │   │   └── form-service.js       # Servicios de aplicación
│   │   │
│   │   ├── 📂 infrastructure/        # Capa de Infraestructura
│   │   │   ├── http-client.js        # Cliente HTTP reutilizable
│   │   │   └── auth-service.js       # Servicio de autenticación
│   │   │
│   │   └── 📂 shared/                # Utilidades compartidas
│   │       ├── config.js             # Configuración global
│   │       └── logger.js             # Sistema de logging
│   │
│   ├── README.md                     # Documentación del módulo
│   │
│   └── 📂 formularios/               # [DEPRECATED] Archivos antiguos
│
├── 📂 auth/                          # Autenticación (entrada)
│   └── login.js                      # Script de login
│
├── 📂 scripts/                       # Scripts de inicialización
│   └── create-forms.js               # Script para crear formularios
│
├── 📂 MR_VidaSegura_3FN.mmd          # Diagrama ER de la base de datos
│
├── package.json                      # Dependencias del proyecto
├── .gitignore                        # Archivos a ignorar en Git
└── README.md                         # Documentación general
```

## 🏗️ Flujo de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                   │
│                    (Scripts & CLI)                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │  auth/login.js  │  scripts/create-forms.js      │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│               APPLICATION LAYER                         │
│           (Business Logic & Use Cases)                 │
│  ┌──────────────────────────────────────────────────┐  │
│  │          FormService                             │  │
│  │  - createForm()                                  │  │
│  │  - updateForm()                                  │  │
│  │  - submitForm()                                  │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│            INFRASTRUCTURE LAYER                         │
│      (External Services & Technical Details)           │
│  ┌──────────────────────────────────────────────────┐  │
│  │  AuthService    │    HttpClient                  │  │
│  │  - loginWith... │    - post()                    │  │
│  │  - getToken()   │    - get()                     │  │
│  │  - logout()     │    - put()                     │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│               DOMAIN LAYER                              │
│         (Business Rules & Entities)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Form Schemas                                    │  │
│  │  - cliente                                       │  │
│  │  - contrato                                      │  │
│  │  - plan_salud                                    │  │
│  │  - ... más esquemas                              │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│               SHARED UTILITIES                          │
│      (Global Config & Helper Functions)                │
│  ┌──────────────────────────────────────────────────┐  │
│  │  config.js (Config)  │  logger.js (Logger)       │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 🔄 Flujo de Ejecución

```
1. Usuario ejecuta:
   node auth/login.js

2. Script de Login
   ↓
3. AuthService.loginWithCredentials()
   ↓
4. HttpClient.post() → Form.io API
   ↓
5. Retorna token JWT
   ↓
6. AuthService almacena token
   ↓
7. Retorna token al usuario
```

## 📋 Características

✅ **Clean Architecture** - Separación clara de capas
✅ **SOLID Principles** - Código mantenible y escalable
✅ **DRY** - Código reutilizable
✅ **Logging** - Sistema centralizado de logs
✅ **Error Handling** - Gestión robusta de errores
✅ **Configuration** - Centralización de configuración

## 🚀 Cómo Ejecutar

```bash
# Instalar dependencias
npm install

# Ejecutar login
npm run login

# Crear formularios
npm run create:forms
```

## 📚 Referencias

- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Form.io Documentation](https://formio.github.io/formio.js/)
