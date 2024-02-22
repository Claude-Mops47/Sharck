function quickSort(arr) {
  // Cas de base : le tableau est déjà trié s'il est vide ou a un seul élément
  if (arr.length <= 1) {
    return arr;
  }

  // Choix du pivot comme premier élément du tableau
  const pivot = arr[0];

  // Partitionnement des éléments autour du pivot
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    // Les éléments inférieurs vont dans le tableau left, les autres dans le tableau right
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  // Appel récursif sur les tableaux left et right, avec concaténation du pivot
  return [...quickSort(left), pivot, ...quickSort(right)];
}

// Exemple d'utilisation
const arrays = [1, 3, 5, 7, 2, 4, 6, 8, -9, -7];
console.log("Tableau initial :", arrays);
console.log("Tableau trié :", quickSort(arrays));
