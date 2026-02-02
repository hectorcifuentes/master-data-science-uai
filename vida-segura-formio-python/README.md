# Python Form.io Integration - Vida Segura
## Clean Architecture Implementation

### Directory Structure

```
vida-segura-formio-python/
├── src/                              # Source code
│   ├── domain/                       # Domain Layer
│   │   ├── __init__.py
│   │   └── form_schemas.py          # Form schema definitions
│   │
│   ├── application/                  # Application Layer
│   │   ├── __init__.py
│   │   └── form_service.py          # Business logic
│   │
│   ├── infrastructure/               # Infrastructure Layer
│   │   ├── __init__.py
│   │   ├── http_client.py           # HTTP abstraction
│   │   └── auth_service.py          # Authentication
│   │
│   └── shared/                       # Shared Layer
│       ├── __init__.py
│       ├── config.py                # Configuration
│       └── logger.py                # Logging
│
├── auth/
│   └── login.py                     # Authentication entry point
│
├── scripts/
│   └── create_forms.py              # Form creation script
│
├── test_forms.py                    # Testing script
├── demo.py                          # Demonstration script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file

```

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python test_forms.py

# Run demo
python demo.py

# Run login
python auth/login.py

# Create forms
python scripts/create_forms.py
```

### Architecture

This project follows **Clean Architecture** principles with 4 layers:

1. **Domain Layer** - Form schemas and business entities (framework-independent)
2. **Application Layer** - Business logic and use cases (FormService)
3. **Infrastructure Layer** - Technical details (HTTP, Authentication)
4. **Shared Layer** - Configuration and utilities (logging, config)

### Key Features

✅ Clean Architecture  
✅ SOLID Principles  
✅ Centralized configuration  
✅ Unified logging system  
✅ HTTP abstraction  
✅ 11 form types configured  
✅ API Key authentication  

### Configuration

All configuration is in `src/shared/config.py`:

- `FORMIO_CONFIG` - Form.io connection settings
- `FORM_IDS` - IDs of created forms
- `HEADERS` - Predefined HTTP headers
- `ENDPOINTS` - API endpoints

### Usage Examples

```python
from src.application.form_service import form_service
from src.domain.form_schemas import get_form_schema

# Get a form schema
schema = get_form_schema('cliente')

# List all forms
forms = form_service.list_forms()

# Create a new form
new_form = form_service.create_form(schema)

# Get a specific form
form = form_service.get_form('form-id')

# Submit form data
submission = form_service.submit_form('form-id', {'name': 'John Doe'})
```

### Testing

Run the test suite:

```bash
python test_forms.py
```

See the architecture in action:

```bash
python demo.py
```

### Notes

- Uses `requests` library for HTTP communication
- All services are singleton instances
- Logger provides consistent output across the application
- Configuration is centralized and environment-aware
- Easy to extend with new form types
