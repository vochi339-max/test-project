import backoff
import requests

# Excepción personalizada para simular un fallo en el servidor/red
class ErrorDeConexion(Exception):
    pass

# Simulamos una función propensa a fallar
# Reintentará hasta 5 veces si ocurre un 'ErrorDeConexion'
# El tiempo entre reintentos se duplicará exponencialmente (1s, 2s, 4s, 8s, 16s...)
@backoff.on_exception(
    backoff.expo,
    ErrorDeConexion,
    max_tries=5,
    giveup=lambda e: "404" in str(e) # Opcional: No reintentar si es un error fatal (ej. 404)
)
def conectar_a_api(url):
    print(f"Intentando conectar a {url}...")
    
    # Simulamos un fallo aleatorio en la red
    # En un caso real, aquí iría tu petición requests.get(url)
    raise ErrorDeConexion("¡Error 503: El servidor no está disponible temporalmente!")
    
    return "Datos obtenidos exitosamente"

# --- Ejecución del programa ---
if __name__ == "__main__":
    try:
        resultado = conectar_a_api("https://ejemplo.com")
        print(resultado)
    except Exception as e:
        print(f"\nOperación fallida tras agotar todos los reintentos: {e}")