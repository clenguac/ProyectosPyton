"""
Programa que demuestra las principales funciones de listas en Python
"""

# Crear una lista
print("=== CREAR UNA LISTA ===")
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# 1. APPEND - Agregar un elemento al final
print("\n=== 1. APPEND ===")
numeros.append(6)
print(f"Después de append(6): {numeros}")

# 2. INSERT - Insertar un elemento en una posición específica
print("\n=== 2. INSERT ===")
numeros.insert(0, 0)  # Insertar 0 en la posición 0
print(f"Después de insert(0, 0): {numeros}")

# 3. EXTEND - Agregar múltiples elementos
print("\n=== 3. EXTEND ===")
numeros.extend([7, 8, 9])
print(f"Después de extend([7, 8, 9]): {numeros}")

# 4. REMOVE - Eliminar un elemento específico
print("\n=== 4. REMOVE ===")
numeros.remove(0)  # Elimina el primer 0 encontrado
print(f"Después de remove(0): {numeros}")

# 5. POP - Eliminar un elemento por índice y retornarlo
print("\n=== 5. POP ===")
elemento_eliminado = numeros.pop()  # Elimina el último elemento
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Lista después de pop(): {numeros}")

# 6. CLEAR - Limpiar toda la lista
print("\n=== 6. CLEAR ===")
lista_temp = [10, 20, 30]
print(f"Lista temporal: {lista_temp}")
lista_temp.clear()
print(f"Después de clear(): {lista_temp}")

# 7. INDEX - Encontrar el índice de un elemento
print("\n=== 7. INDEX ===")
frutas = ["manzana", "plátano", "cereza", "plátano"]
indice = frutas.index("plátano")
print(f"Lista de frutas: {frutas}")
print(f"Índice de 'plátano': {indice}")

# 8. COUNT - Contar cuántas veces aparece un elemento
print("\n=== 8. COUNT ===")
cantidad = frutas.count("plátano")
print(f"'plátano' aparece {cantidad} veces en la lista")

# 9. SORT - Ordenar la lista
print("\n=== 9. SORT ===")
numeros_desordenados = [5, 2, 9, 1, 5, 6]
print(f"Lista desordenada: {numeros_desordenados}")
numeros_desordenados.sort()
print(f"Después de sort(): {numeros_desordenados}")

# 10. REVERSE - Invertir el orden de la lista
print("\n=== 10. REVERSE ===")
numeros_copia = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros_copia}")
numeros_copia.reverse()
print(f"Después de reverse(): {numeros_copia}")

# 11. COPY - Crear una copia de la lista
print("\n=== 11. COPY ===")
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()
lista_copia.append(4)
print(f"Lista original: {lista_original}")
print(f"Lista copia: {lista_copia}")

# 12. LEN - Obtener la longitud de la lista
print("\n=== 12. LEN ===")
lista_ejemplo = ["a", "b", "c", "d"]
print(f"Lista: {lista_ejemplo}")
print(f"Longitud: {len(lista_ejemplo)}")

# 13. Acceder a elementos por índice
print("\n=== 13. ACCESO POR ÍNDICE ===")
letras = ["a", "b", "c", "d", "e"]
print(f"Lista: {letras}")
print(f"Primer elemento (índice 0): {letras[0]}")
print(f"Último elemento (índice -1): {letras[-1]}")
print(f"Elementos del índice 1 al 3: {letras[1:4]}")

# 14. IN - Verificar si un elemento está en la lista
print("\n=== 14. IN (Búsqueda) ===")
colores = ["rojo", "azul", "verde"]
print(f"Lista: {colores}")
print(f"¿'azul' está en la lista? {'azul' in colores}")
print(f"¿'amarillo' está en la lista? {'amarillo' in colores}")

print("\n=== FIN DEL PROGRAMA ===")
<<<<<<< Updated upstream

print("¡Gracias por aprender sobre listas en Python!")
=======
print("Este programa ha demostrado las principales funciones de listas en Python.")
>>>>>>> Stashed changes
