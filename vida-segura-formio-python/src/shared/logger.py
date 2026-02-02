"""
Logger - Sistema centralizado de logging
Proporciona logging consistente en toda la aplicación
"""

from datetime import datetime
import json


class Logger:
    """Servicio de logging centralizado con diferentes niveles"""
    
    # Emojis para cada tipo de log
    EMOJIS = {
        'info': 'ℹ️',
        'success': '✅',
        'warning': '⚠️',
        'error': '❌',
        'section': '📋'
    }
    
    @staticmethod
    def _format_message(level, message, data=None):
        """Formatea un mensaje de log"""
        emoji = Logger.EMOJIS.get(level, '')
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        output = f"{emoji} {message}"
        
        if data:
            if isinstance(data, dict):
                data_str = json.dumps(data, indent=2, ensure_ascii=False)
            else:
                data_str = str(data)
            output += f" {data_str}"
        
        return output
    
    @staticmethod
    def info(message, data=None):
        """Log de información"""
        print(Logger._format_message('info', message, data))
    
    @staticmethod
    def success(message, data=None):
        """Log de éxito"""
        print(Logger._format_message('success', message, data))
    
    @staticmethod
    def warning(message, data=None):
        """Log de advertencia"""
        print(Logger._format_message('warning', message, data))
    
    @staticmethod
    def error(message, error=None):
        """Log de error"""
        if error:
            error_msg = str(error)
            print(Logger._format_message('error', message, error_msg))
        else:
            print(Logger._format_message('error', message))
    
    @staticmethod
    def section(title):
        """Sección de logs (separador visual)"""
        print("\n" + "=" * 60)
        print(f"📋 {title}")
        print("=" * 60 + "\n")


# Instancia singleton
logger = Logger()
