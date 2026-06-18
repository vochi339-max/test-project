import pandas as pd
import logging
from logging.handlers import RotatingFileHandler
import os

# 1. Configuración del Logging
logger = logging.getLogger("DataPipelineLogger")
logger.setLevel(logging.DEBUG) # Captura todos los niveles

# Formato de los mensajes de log
log_format = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')

# Handler para archivo (con rotación: máximo 1MB por archivo, guarda hasta 3 respaldos)
file_handler = RotatingFileHandler('proceso_datos.log', maxBytes=1*1024*1024, backupCount=3)
file_handler.setLevel(logging.INFO) # Archivo registra INFO y niveles superiores
file_handler.setFormatter(log_format)

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) # Consola registra todo (útil para desarrollo)
console_handler.setFormatter(log_format)

# Agregar handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def procesar_datos(ruta_csv: str, ruta_json: str):
    logger.info(f"Iniciando ingesta del archivo: {ruta_csv}")
    
    try:
        # 2. Ingesta del CSV
        df = pd.read_csv(ruta_csv)
        logger.info(f"Archivo CSV cargado exitosamente. Filas: {len(df)}, Columnas: {list(df.columns)}")
        
        # 3. Cálculo de Métricas Básicas
        logger.debug("Calculando métricas estadísticas...")
        
        # Ejemplo: Métricas descriptivas generales
        metricas_resumen = df.describe().to_dict()
        
        # Ejemplo: Conteo de valores nulos
        nulos = df.isnull().sum().to_dict()
        
        logger.info("Métricas calculadas exitosamente.")
        
        # 4. Estructurar el resultado final (Datos + Métricas)
        resultado_final = {
            "metadata": {
                "total_filas": len(df),
                "metricas_resumen": metricas_resumen,
                "valores_nulos": nulos
            },
            "datos": df.to_dict(orient="records")
        }
        
        # 5. Exportación a JSON
        logger.info(f"Exportando resultados a JSON en: {ruta_json}")
        with open(ruta_json, 'w', encoding='utf-8') as archivo_json:
            import json
            json.dump(resultado_final, archivo_json, indent=4, ensure_ascii=False)
            
        logger.info("Proceso completado con éxito.")
        
    except FileNotFoundError:
        logger.error(f"El archivo CSV en la ruta '{ruta_csv}' no fue encontrado.", exc_info=True)
    except pd.errors.EmptyDataError:
        logger.warning(f"El archivo CSV en '{ruta_csv}' está vacío.", exc_info=True)
    except Exception as e:
        logger.critical(f"Ocurrió un error crítico durante la ejecución: {e}", exc_info=True)


if __name__ == "__main__":
    # Definir rutas de archivos
    archivo_entrada = "datos.csv"
    archivo_salida = "resultado.json"
    
    # Asegurar que el archivo de entrada existe para la prueba
    if not os.path.exists(archivo_entrada):
        logger.warning(f"Archivo {archivo_entrada} no encontrado. Creando uno de ejemplo...")
        df_ejemplo = pd.DataFrame({
            "id": [1, 2, 3],
            "nombre": ["Ana", "Juan", "Pedro"],
            "salario": [1500.50, None, 2800.00]
        })
        df_ejemplo.to_csv(archivo_entrada, index=False)

    # Ejecutar proceso
    procesar_datos(archivo_entrada, archivo_salida)