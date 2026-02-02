/**
 * Test Script - Verificar que la nueva arquitectura funciona
 * Prueba simple sin autenticación de usuario
 */

import { formService } from './vidaSegura/src/application/form-service.js';
import { getFormSchema } from './vidaSegura/src/domain/form-schemas.js';
import { logger } from './vidaSegura/src/shared/logger.js';

async function testForms() {
    try {
        logger.section('Testing Form Service');

        // Obtener el schema del formulario cliente
        const clienteSchema = getFormSchema('cliente');
        
        logger.success('Schema loaded:', {
            title: clienteSchema.title,
            name: clienteSchema.name,
            components: clienteSchema.components?.length || 0
        });

        // Intentar listar formularios existentes
        logger.info('Listing existing forms...');
        const forms = await formService.listForms();
        
        logger.success('Forms retrieved:', {
            count: forms?.length || 0,
            forms: forms?.slice(0, 3)?.map(f => ({ id: f._id, title: f.title }))
        });

        logger.section('✅ All tests passed!');
    } catch (error) {
        logger.error('Test failed', error);
        process.exit(1);
    }
}

testForms();
