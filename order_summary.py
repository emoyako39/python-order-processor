def summarize_orders(orders):
    total_orders = 0
    total_amount = 0
    orders_by_status = {}
    for order in orders:
        total_orders += 1
        raw_status = order.get("status")
        if isinstance(raw_status, str) and raw_status.strip():
            status = raw_status.strip().lower()
        else:
            status = "unknown"
        raw_total = order.get("total")
        orders_by_status[status] = orders_by_status.get(status, 0) + 1
        if isinstance(raw_total, (int, float)) and not isinstance(raw_total, bool):
            total_amount += raw_total

    return {
    "total_orders": total_orders,
    "total_amount": total_amount,
    "orders_by_status": orders_by_status
}