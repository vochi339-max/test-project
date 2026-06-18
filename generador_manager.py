import time
from contextlib import contextmanager

# 1. Gestor de contexto de temporización
@contextmanager
def medir_tiempo(operacion):
    """Mide el tiempo de ejecución de un bloque de código."""
    tiempo_inicio = time.perf_counter()
    try:
        yield
    finally:
        tiempo_fin = time.perf_counter()
        tiempo_total = tiempo_fin - tiempo_inicio
        print(f"[TEMPORIZADOR] La operación '{operacion}' tardó {tiempo_total:.4f} segundos.")

# 2. Generador por lotes (Batch Generator)
def generar_lotes(elementos, tamano_lote):
    """Divide una lista en lotes más pequeños para procesamiento secuencial."""
    for i in range(0, len(elementos), tamano_lote):
        yield elementos[i:i + tamano_lote]

# 3. Simulación de procesamiento de datos
if __name__ == "__main__":
    datos_completos = list(range(1, 10001)) # 10,000 elementos simulados
    tamano_del_lote = 1000

    print("Iniciando procesamiento...\n")

    # Usando el temporizador para medir todo el proceso
    with medir_tiempo("Procesamiento Total"):
        
        # Procesando por lotes
        for lote in generar_lotes(datos_completos, tamano_del_lote):
            
            # Midiendo el tiempo de un lote específico
            with medir_tiempo(f"Lote {lote[0]}-{lote[-1]}"):
                # Simulación de trabajo pesado (ej. escritura en BD, transformación)
                tiempo_simulado = 0.0001 * len(lote)
                time.sleep(tiempo_simulado) 
                
            print(f"  -> Lote procesado: {len(lote)} elementos.\n")

    print("Programa finalizado.")