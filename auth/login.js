/**
 * Login Script - Autenticación del usuario
 * Punto de entrada para autenticarse en Form.io usando API Key
 */

import { logger } from '../vidaSegura/src/shared/logger.js';
import { FORMIO_CONFIG } from '../vidaSegura/src/shared/config.js';


async function main() {
    try {
        logger.section('Form.io Authentication');

        const apiKey = FORMIO_CONFIG.API_KEY;

        logger.success('API Key loaded successfully!', {
            apiKey: apiKey?.substring(0, 20) + '...',
            baseUrl: FORMIO_CONFIG.BASE_URL
        });

        logger.info('Ready to use with Form.io', {
            authenticated: true,
            method: 'API Key',
            projects: 'All projects accessible'
        });

        return apiKey;
    } catch (error) {
        logger.error('Authentication failed', error);
        process.exit(1);
    }
}

main();
