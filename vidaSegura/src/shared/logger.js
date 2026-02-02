/**
 * Logger simple para el proyecto
 */

export const logger = {
    info: (message, data = '') => {
        console.log(`ℹ️  ${message}`, data ? JSON.stringify(data, null, 2) : '');
    },

    success: (message, data = '') => {
        console.log(`✅ ${message}`, data ? JSON.stringify(data, null, 2) : '');
    },

    warning: (message, data = '') => {
        console.warn(`⚠️  ${message}`, data ? JSON.stringify(data, null, 2) : '');
    },

    error: (message, error = '') => {
        console.error(`❌ ${message}`, error?.message || error || '');
    },

    section: (title) => {
        console.log(`\n${'='.repeat(60)}`);
        console.log(`📋 ${title}`);
        console.log(`${'='.repeat(60)}\n`);
    }
};
