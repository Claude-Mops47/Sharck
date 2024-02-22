def quick_sort(arr):
    # Cas de base : le tableau est déjà trié s'il est vide ou a un seul élément
    if len(arr) <= 1:
        return arr

    # Choix du pivot comme premier élément du tableau
    pivot = arr[0]

    # Partitionnement des éléments autour du pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Appel récursif sur les tableaux left et right, avec concaténation du pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Exemple d'utilisation
arrays = [1, 3, 5, 7, 2, 4, 6, 8, -9, -7]
print("Tableau initial:", arrays)
print("Tableau trié:", quick_sort(arrays))
