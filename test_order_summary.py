from order_summary import summarize_orders

orders = [
    {"id": 1, "status": " SHIPPED ", "total": 100},
    {"id": 2, "status": "pending", "total": True},
    {"id": 3, "status": "shipped", "total": 50},
    {"id": 4, "status": None, "total": 25},
    {"id": 5, "status": "   ", "total": "invalid"},
    {"id": 6, "total": 75}
]

print(summarize_orders(orders))