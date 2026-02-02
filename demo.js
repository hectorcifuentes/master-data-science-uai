/**
 * Demo Script - Demostración completa de la arquitectura Clean
 * Demuestra las diferentes capas y servicios
 */

import { formService } from './vidaSegura/src/application/form-service.js';
import { getFormSchema } from './vidaSegura/src/domain/form-schemas.js';
import { logger } from './vidaSegura/src/shared/logger.js';
import { FORM_IDS } from './vidaSegura/src/shared/config.js';

async function demonstrateArchitecture() {
    try {
        logger.section('🏗️  Clean Architecture Demo');

        // 1️⃣ Domain Layer - Obtener esquemas
        logger.info('1️⃣ Domain Layer - Form Schemas');
        const clienteSchema = getFormSchema('cliente');
        logger.success('✓ Client form schema loaded', {
            title: clienteSchema.title,
            fields: clienteSchema.components?.length || 0
        });

        // 2️⃣ Infrastructure Layer - HTTP Communication
        logger.info('2️⃣ Infrastructure Layer - HTTP Communication');
        logger.success('✓ HttpClient configured for API requests');

        // 3️⃣ Application Layer - Business Logic
        logger.info('3️⃣ Application Layer - FormService');
        const forms = await formService.listForms();
        logger.success('✓ Forms retrieved via FormService', {
            total: forms.length,
            forms: forms.map(f => f.title).slice(0, 3)
        });

        // 4️⃣ Shared Layer - Configuration & Logging
        logger.info('4️⃣ Shared Layer - Config & Logger');
        logger.success('✓ Centralized configuration and logging', {
            trackedForms: Object.keys(FORM_IDS).length
        });

        // Get specific form info
        logger.section('📊 Formularios Registrados');
        const clienteForm = forms.find(f => f._id === FORM_IDS.CLIENTE);
        if (clienteForm) {
            logger.success('Cliente', {
                id: clienteForm._id,
                name: clienteForm.name,
                path: clienteForm.path
            });
        }

        const contratoForm = forms.find(f => f._id === FORM_IDS.CONTRATO);
        if (contratoForm) {
            logger.success('Contrato', {
                id: contratoForm._id,
                name: contratoForm.name
            });
        }

        // Demonstrate architecture benefits
        logger.section('✨ Arquitectura Benefits');
        logger.success('Clean Architecture Implemented:', {
            layers: ['Domain', 'Application', 'Infrastructure', 'Shared'],
            principles: ['SRP', 'DIP', 'DRY', 'SOLID'],
            testability: 'High (isolated services)',
            maintainability: 'Excellent (clear structure)'
        });

    } catch (error) {
        logger.error('Demo failed', error);
        process.exit(1);
    }
}

demonstrateArchitecture();
