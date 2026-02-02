/**
 * Form Schemas - Esquemas de dominio para todos los formularios
 * Capa de dominio - Definiciones de entidades
 */

export const schemas = {
    cliente: {
        title: 'Registro de Cliente',
        name: 'registro-cliente',
        path: 'registro-cliente',
        components: [
            {
                input: true,
                tableView: true,
                inputType: 'text',
                label: 'RUT',
                key: 'rut',
                placeholder: 'Ej: 12345678-K',
                persistent: true,
                validate: { required: true },
                type: 'textfield'
            },
            {
                input: true,
                tableView: true,
                inputType: 'text',
                label: 'Nombre',
                key: 'nombre',
                placeholder: '',
                persistent: true,
                validate: { required: true },
                type: 'textfield'
            },
            {
                input: true,
                tableView: true,
                inputType: 'text',
                label: 'Apellidos',
                key: 'apellidos',
                placeholder: '',
                persistent: true,
                validate: { required: true },
                type: 'textfield'
            },
            {
                input: true,
                tableView: true,
                label: 'Fecha de Nacimiento',
                key: 'fecha_nacimiento',
                placeholder: '',
                persistent: true,
                validate: { required: true },
                type: 'datetime',
                format: 'yyyy-MM-dd'
            },
            {
                input: true,
                tableView: true,
                label: 'Sexo',
                key: 'id_sexo',
                placeholder: 'Selecciona tu sexo',
                persistent: true,
                validate: { required: true },
                data: {
                    values: [
                        { label: 'Masculino', value: 'M' },
                        { label: 'Femenino', value: 'F' }
                    ]
                },
                type: 'select'
            },
            {
                input: true,
                tableView: true,
                inputType: 'text',
                label: 'Dirección',
                key: 'direccion',
                placeholder: '',
                persistent: true,
                validate: { required: true },
                type: 'textarea'
            },
            {
                input: true,
                tableView: true,
                inputType: 'text',
                label: 'Teléfono',
                key: 'telefono',
                placeholder: '',
                persistent: true,
                validate: { required: true },
                type: 'phoneNumber'
            },
            {
                input: true,
                tableView: true,
                inputType: 'email',
                label: 'Correo Electrónico',
                key: 'correo',
                placeholder: 'correo@ejemplo.com',
                persistent: true,
                validate: { required: true },
                type: 'email'
            },
            {
                input: true,
                tableView: true,
                label: 'Estado de Afiliación',
                key: 'id_estado_afiliacion',
                placeholder: 'Selecciona el estado',
                persistent: true,
                validate: { required: true },
                data: {
                    values: [
                        { label: 'Activo', value: '1' },
                        { label: 'Inactivo', value: '2' },
                        { label: 'Suspendido', value: '3' }
                    ]
                },
                type: 'select'
            },
            {
                input: true,
                label: 'Registrar',
                tableView: false,
                key: 'submit',
                size: 'md',
                action: 'submit',
                disableOnInvalid: false,
                theme: 'primary',
                type: 'button'
            }
        ]
    },

    // Agregar más esquemas aquí según sea necesario
};

export const getFormSchema = (formType) => {
    const schema = schemas[formType];
    if (!schema) {
        throw new Error(`Form schema for '${formType}' not found`);
    }
    return {
        ...schema,
        display: 'form',
        type: 'form',
        tags: [formType],
        revisions: 'original'
    };
};
