from pathlib import Path
# Busca datos/productos.txt a partir de donde está este archivo,
# así funciona desde cualquier carpeta (terminal o botón ▶ de VS Code)
carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"
lineas = archivo.read_text(encoding="utf-8").splitlines()
print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

for linea in lineas[2:]:
    print("-", linea)
    total_productos += 1

# Extrae el precio después del '$' y quita el punto de miles
    valor_inventario += int(linea.split("$")[1].replace(".", ""))

print("Total de productos:", total_productos)
print(f"Valor del inventario: ${valor_inventario}")