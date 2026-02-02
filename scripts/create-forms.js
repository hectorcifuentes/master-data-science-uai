/**
 * Create Forms Script - Crear todos los formularios en Form.io
 * Script de inicialización
 */

import { formService } from '../vidaSegura/src/application/form-service.js';
import { getFormSchema } from '../vidaSegura/src/domain/form-schemas.js';
import { logger } from '../vidaSegura/src/shared/logger.js';

/**
 * Lista de formularios a crear/actualizar
 */
const FORMS_TO_CREATE = [
    { key: 'cliente', name: 'Cliente' }
    // Agregar más formularios aquí
];

async function createOrUpdateForms() {
    try {
        logger.section('Creating Forms in Form.io');

        for (const form of FORMS_TO_CREATE) {
            try {
                const schema = getFormSchema(form.key);
                logger.info(`Processing form: ${form.name}`);

                // Crear el formulario
                const createdForm = await formService.createForm(schema);
                logger.success(`Form created: ${form.name}`, {
                    id: createdForm._id,
                    url: `${createdForm.url || 'N/A'}`
                });
            } catch (error) {
                logger.warning(`Could not create ${form.name}`, error.message);
            }
        }

        logger.section('All forms processed');
    } catch (error) {
        logger.error('Failed to create forms', error);
        process.exit(1);
    }
}

createOrUpdateForms();
