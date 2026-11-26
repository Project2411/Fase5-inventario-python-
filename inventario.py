def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual 
    else:
        return 0


inventario = [ 
    ["A001", "Teclado", 10, 20],
    ["A002", "Mouse", 15, 10],
    ["A003", "Monitor", 5, 12],
    ["A004", "Impresora", 8, 15],
    ["A005", "Auriculares", 25, 20]
]

print("REPORTE DE REABASTECIMENTO")
print("-" * 30)

for articulo in inventario:
    cantidad = calcular_pedido(articulo[2], articulo[3])

    print("Articulo:", articulo[1])
    print("Cantidad a solicitar:", cantidad)
    print("-" * 30)
    