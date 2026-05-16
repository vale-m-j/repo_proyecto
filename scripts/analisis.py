import pandas as pd

ventas = pd.DataFrame({
    'producto': ['Lapiz', 'Cuaderno', 'Lapiz', 'Goma'],
    'cantidad': [2, 1, 3, 2],
    'precio': [100, 500, 100, 50]
})

ventas['total'] = ventas['cantidad'] * ventas['precio']

print("Ventas totales:")
print(ventas['total'].sum())

print("\nProductos vendidos:")
print(ventas.groupby('producto')['cantidad'].sum())
