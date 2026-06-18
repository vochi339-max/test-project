import json
import os

def procesar_datos_json(ruta_entrada, ruta_salida):
    # 1. Manejo de errores de lectura y formato
    try:
        with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_entrada}' no existe.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: El archivo no tiene un formato JSON válido. Detalles: {e}")
        return

    # Verificamos que los datos sean una lista
    if not isinstance(datos, list):
        print("Error: El JSON principal debe contener una lista de objetos.")
        return

    # 2. Filtrado y agregación de datos
    datos_procesados = []
    for item in datos:
        # Ejemplo de filtro: conservar solo elementos con un estado activo (ej. 'activo' == True)
        # Puedes cambiar esta condición según tus necesidades
        if item.get('activo') == True:
            
            # Agregamos/Modificamos datos: añadimos una nueva propiedad
            item['procesado'] = True
            item['margen_calculado'] = item.get('precio', 0) * 1.15
            
            datos_procesados.append(item)

    # 3. Guardar el nuevo archivo JSON
    try:
        # Asegurarse de que el directorio de salida exista
        directorio = os.path.dirname(ruta_salida)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            
        with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
            # indent=4 formatea el JSON para que sea legible
            json.dump(datos_procesados, archivo_salida, indent=4, ensure_ascii=False)
        print(f"Proceso exitoso. Datos guardados en '{ruta_salida}'.")
        
    except IOError as e:
        print(f"Error al intentar guardar el archivo de salida. Detalles: {e}")

# --- Ejecución del Script ---
if __name__ == "__main__":
    archivo_entrada = 'C:/Users/Administrador/Documents/documentos_phyton/.vscode/datos_originales.json'
    archivo_salida =  'C:/Users/Administrador/Documents/documentos_phyton/.vscode/datos_procesados.json'
    
    
    procesar_datos_json(archivo_entrada, archivo_salida)