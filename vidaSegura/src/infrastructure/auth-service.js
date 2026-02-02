/**
 * AuthService - Servicio de autenticación con Form.io
 * Infraestructura - Lógica de autenticación
 */

import { httpClient } from './http-client.js';
import { FORMIO_CONFIG, ENDPOINTS, HEADERS } from '../shared/config.js';
import { logger } from '../shared/logger.js';

export class AuthService {
    constructor() {
        this.baseUrl = FORMIO_CONFIG.BASE_URL;
        this.token = null;
    }

    /**
     * Autentica usuario con email y contraseña
     */
    async loginWithCredentials(email, password) {
        try {
            logger.info('🔐 Authenticating user...');

            const url = `${this.baseUrl}${ENDPOINTS.LOGIN}`;
            const response = await httpClient.post(
                url,
                { email, password },
                HEADERS.JSON
            );

            this.token = response.token || response._id;
            logger.success('Authentication successful!', {
                token: this.token?.substring(0, 50) + '...'
            });

            return this.token;
        } catch (error) {
            logger.error('Login failed', error);
            throw error;
        }
    }

    /**
     * Obtiene el token actual
     */
    getToken() {
        return this.token;
    }

    /**
     * Verifica si hay token activo
     */
    isAuthenticated() {
        return !!this.token;
    }

    /**
     * Limpia el token (logout)
     */
    logout() {
        this.token = null;
        logger.success('User logged out');
    }
}

export const authService = new AuthService();
