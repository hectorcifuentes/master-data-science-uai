/**
 * HttpClient - Servicio para realizar peticiones HTTP
 * Infraestructura - Abstracción de llamadas a la API
 */

import fetch from 'node-fetch';
import { logger } from '../shared/logger.js';

export class HttpClient {
    async request(method, url, headers = {}, body = null) {
        try {
            const options = {
                method,
                headers
            };

            if (body) {
                options.body = JSON.stringify(body);
            }

            const response = await fetch(url, options);

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(
                    `HTTP ${response.status}: ${response.statusText} - ${errorText.substring(0, 200)}`
                );
            }

            return await response.json();
        } catch (error) {
            logger.error(`Request failed: ${method} ${url}`, error);
            throw error;
        }
    }

    post(url, body, headers) {
        return this.request('POST', url, headers, body);
    }

    put(url, body, headers) {
        return this.request('PUT', url, headers, body);
    }

    get(url, headers) {
        return this.request('GET', url, headers);
    }

    delete(url, headers) {
        return this.request('DELETE', url, headers);
    }
}

export const httpClient = new HttpClient();
