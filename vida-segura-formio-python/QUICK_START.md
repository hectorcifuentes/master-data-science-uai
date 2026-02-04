# Python version of vida-segura-formio

## Quick Start

```bash
## Antes de ejecutar el login o crear formularios, debes crear tu propio usuario y contraseña en Form.io.
## Luego, añade tu email y contraseña en los archivos de configuración correspondientes (por ejemplo, src/shared/config.py), reemplazando los valores dummy.
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

- Cliente: dummy_cliente_id
- Contrato: dummy_contrato_id
- Plan Salud: dummy_plan_salud_id
- Beneficiario: dummy_beneficiario_id
- Atención Médica: dummy_atencion_medica_id
- Diagnóstico: dummy_diagnostico_id
- Prestación: dummy_prestacion_id
- Prestador: dummy_prestador_id
- Profesional: dummy_profesional_id
- Cobertura: dummy_cobertura_id
- Pago: dummy_pago_id
