from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class OrderItem:
    name: str
    price: float
    quantity: int

    # Campo calculado que no interviene en la inicialización (__init__)
    subtotal: float = field(init=False)

    def __post_init__(self):
        # Se ejecuta después de __init__ para calcular el subtotal
        self.subtotal = self.price * self.quantity

@dataclass(order=True)
class Order:
    # El orden en los atributos define la prioridad para las comparaciones
    total: float = field(init=False, compare=True)
    order_id: str = field(compare=False)
    items: List[OrderItem] = field(compare=False)
    tax_rate: float = field(default=0.16, compare=False)
    discount: float = field(default=0.0, compare=False)

    def __post_init__(self):
        # Cálculo derivado: suma de los subtotales de los items
        items_subtotal = sum(item.subtotal for item in self.items)
        
        # Cálculo derivado: impuestos y descuentos
        tax_amount = items_subtotal * self.tax_rate
        self.total = items_subtotal + tax_amount - self.discount

# --- Demostración ---

# 1. Crear artículos
item1 = OrderItem(name="Laptop", price=1200.0, quantity=1)
item2 = OrderItem(name="Mouse", price=50.0, quantity=2)

# 2. Crear órdenes
order1 = Order(order_id="ORD-001", items=[item1, item2], discount=0.0)
order2 = Order(order_id="ORD-002", items=[item1], discount=100.0)

print(f"Total Orden 1: ${order1.total:.2f}")
print(f"Total Orden 2: ${order2.total:.2f}")

# 3. Comparaciones automáticas basadas en el 'total' (gracias a @dataclass(order=True))
print(f"¿Orden 1 es mayor que Orden 2? {order1 > order2}")
print(f"¿Orden 1 es menor o igual a Orden 2? {order1 <= order2}")