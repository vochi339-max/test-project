from pydantic import BaseModel
from typing import List
from datetime import datetime

# 1. Modelo de Entrada (Datos que recibimos del cliente/API)
class OrderIn(BaseModel):
    client_name: str
    items: List[str]
    total_price: float

# 2. Modelo de Entidad (Lógica interna, contiene metadatos como ID y fecha)
class Order(BaseModel):
    id: int
    client_name: str
    items: List[str]
    total_price: float
    created_at: datetime

# 3. Modelo de Salida (Datos que devolvemos al cliente)
class OrderOut(BaseModel):
    id: int
    client_name: str
    total_items: int
    total_price: float

# --- SIMULACIÓN DEL PROCESO ---

# Datos entrantes simulados (ej. petición HTTP)
raw_data = {
    "client_name": "Ana Gómez",
    "items": ["Laptop", "Mouse"],
    "total_price": 1250.50
}

# Paso 1: Validar y parsear datos de entrada
order_in = OrderIn(**raw_data)
print(f"1. OrderIn validado: {order_in}")

# Paso 2: Convertir a Entidad de Negocio (Asignamos ID y fecha)
order_entity = Order(
    id=101,
    client_name=order_in.client_name,
    items=order_in.items,
    total_price=order_in.total_price,
    created_at=datetime.now()
)
print(f"\n2. Entidad Order creada: {order_entity}")

# Paso 3: Convertir a Modelo de Salida (Adaptamos el formato)
# Usamos .model_dump() (o .dict() en Pydantic v1) para convertir el modelo a diccionario
order_out = OrderOut(
    id=order_entity.id,
    client_name=order_entity.client_name,
    total_items=len(order_entity.items),
    total_price=order_entity.total_price
)
print(f"\n3. OrderOut para el cliente: {order_out}")
