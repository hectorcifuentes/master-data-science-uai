# Python version of vida-segura-formio

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run demo
python demo.py

# Run tests
python test_forms.py

# Login (API Key)
python auth/login.py

# Create forms
python scripts/create_forms.py
```

## Architecture

Clean Architecture with 4 layers:
- **Domain**: Form schemas (framework-independent)
- **Application**: FormService (business logic)
- **Infrastructure**: HttpClient, AuthService
- **Shared**: Config, Logger

## Form IDs (11 registered)

- Cliente: 697ebba1cd4b046138f5e4ee
- Contrato: 697ebf91db796af904668b44
- Plan Salud: 697ec2d5cd4b046138f602bd
- Beneficiario: 697ec50acd4b046138f61017
- Atención Médica: 697ec966db796af90466bbcc
- Diagnóstico: 697eca2acd4b046138f627d6
- Prestación: 697eca2acd4b046138f627df
- Prestador: 697eca2adb796af90466c05f
- Profesional: 697eca2acd4b046138f627ea
- Cobertura: 697eca2adb796af90466c05c
- Pago: 697eca2acd4b046138f627e7
