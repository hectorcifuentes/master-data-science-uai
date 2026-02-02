# Vida Segura - Form.io Integration

## Arquitectura del Proyecto

Este proyecto sigue el patrón de **Clean Architecture** dividido en capas:

```
vidaSegura/
├── src/
│   ├── domain/              # Capa de Dominio
│   │   └── form-schemas.js  # Esquemas y entidades de formularios
│   │
│   ├── application/         # Capa de Aplicación
│   │   └── form-service.js  # Servicios de aplicación
│   │
│   ├── infrastructure/      # Capa de Infraestructura
│   │   ├── http-client.js   # Cliente HTTP reutilizable
│   │   └── auth-service.js  # Servicio de autenticación
│   │
│   └── shared/              # Utilidades compartidas
│       ├── config.js        # Configuración global
│       └── logger.js        # Logger simple
│
└── formularios/             # Formularios (deprecated)
```

## Capas de la Arquitectura

### 1. **Domain Layer** (Dominio)
- Define las **entidades** y reglas de negocio
- Contiene esquemas de formularios independientes del framework
- **Archivos:** `form-schemas.js`

### 2. **Application Layer** (Aplicación)
- **Servicios de aplicación** que orquestan la lógica de negocio
- Utiliza servicios de infraestructura
- **Archivos:** `form-service.js`

### 3. **Infrastructure Layer** (Infraestructura)
- Implementación de detalles técnicos (APIs, bases de datos, etc.)
- Abstracción de dependencias externas
- **Archivos:** `http-client.js`, `auth-service.js`

### 4. **Shared** (Compartido)
- Configuración global
- Utilidades (logger, constantes, helpers)
- Reutilizable en toda la aplicación

## Uso

### Login
```bash
node auth/login.js
```

### Crear Formularios
```bash
node scripts/create-forms.js
```

## Dependencias
- `node-fetch` - Para peticiones HTTP

## Buenas Prácticas Implementadas

✅ **Single Responsibility Principle** - Cada clase tiene una única responsabilidad
✅ **Dependency Inversion** - Las capas superiores no dependen de las inferiores
✅ **DRY (Don't Repeat Yourself)** - Código reutilizable
✅ **Logging centralizado** - Logger compartido
✅ **Configuración centralizada** - Variables en un solo lugar
✅ **Manejo de errores** - Try-catch y logging de errores

## Próximos Pasos

1. Implementar casos de uso completos (UseCases)
2. Agregar validación de datos (Validators)
3. Implementar repositorios para abstracción de datos
4. Agregar tests unitarios
5. Implementar dependencia injection
