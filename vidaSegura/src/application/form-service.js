/**
 * FormService - Servicio de aplicación para gestionar formularios
 * Capa de aplicación - Lógica de negocio de formularios
 */

import { httpClient } from '../infrastructure/http-client.js';
import { FORMIO_CONFIG, HEADERS } from '../shared/config.js';
import { logger } from '../shared/logger.js';

export class FormService {
    constructor() {
        this.baseUrl = FORMIO_CONFIG.BASE_URL;
        this.apiKey = FORMIO_CONFIG.API_KEY;
    }

    /**
     * Crear un nuevo formulario
     */
    async createForm(formData) {
        try {
            logger.info('📝 Creating form...', {
                title: formData.title,
                name: formData.name
            });

            const url = `${this.baseUrl}/form`;
            const response = await httpClient.post(
                url,
                formData,
                HEADERS.WITH_API_KEY
            );

            logger.success('Form created successfully', { id: response._id });
            return response;
        } catch (error) {
            logger.error('Failed to create form', error);
            throw error;
        }
    }

    /**
     * Actualizar un formulario existente
     */
    async updateForm(formId, formData) {
        try {
            logger.info('📝 Updating form...', { id: formId });

            const url = `${this.baseUrl}/form/${formId}`;
            const response = await httpClient.put(
                url,
                formData,
                HEADERS.WITH_API_KEY
            );

            logger.success('Form updated successfully', { id: response._id });
            return response;
        } catch (error) {
            logger.error('Failed to update form', error);
            throw error;
        }
    }

    /**
     * Obtener un formulario por ID
     */
    async getForm(formId) {
        try {
            const url = `${this.baseUrl}/form/${formId}`;
            const response = await httpClient.get(
                url,
                HEADERS.WITH_API_KEY
            );

            return response;
        } catch (error) {
            logger.error('Failed to get form', error);
            throw error;
        }
    }

    /**
     * Listar todos los formularios
     */
    async listForms() {
        try {
            const url = `${this.baseUrl}/form`;
            const response = await httpClient.get(
                url,
                HEADERS.WITH_API_KEY
            );

            return response;
        } catch (error) {
            logger.error('Failed to list forms', error);
            throw error;
        }
    }

    /**
     * Enviar datos de un formulario
     */
    async submitForm(formId, data) {
        try {
            logger.info('📤 Submitting form...', { id: formId });

            const url = `${this.baseUrl}/form/${formId}/submission`;
            const response = await httpClient.post(
                url,
                { data },
                HEADERS.WITH_API_KEY
            );

            logger.success('Form submitted successfully', { submissionId: response._id });
            return response;
        } catch (error) {
            logger.error('Failed to submit form', error);
            throw error;
        }
    }
}

export const formService = new FormService();
