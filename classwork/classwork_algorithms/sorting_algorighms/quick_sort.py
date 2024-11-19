def partition(arr, low, high):
  pivot = arr[low]
  i = low + 1
  j = high

  while True:
    while i <= j and arr[i] < pivot:
      i += 1
    
    while i <= j and arr[j] > pivot:
      j -= 1

    if i > j:
      break
    arr[i], arr[j] = arr[j], arr[i]
  
  arr[low], arr[j] = arr[j], arr[low]
  return j

def quick_sort(arr: list[int], low, high)->None:
  if low < high:
    pi = partition(arr, low, high)

    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)

  


arr = [10, 16, 5, 54, 12, 8, 43]

quick_sort(arr, 0, len(arr) - 1)
print(arr)