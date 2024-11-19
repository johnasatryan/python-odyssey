

def merge_sort(nums: list[int], left, right) -> None:
	if len(nums) < 1:
		return

	mid = left + right // 2

	merge_sort(arr, left, mid)
	merge_sort(arr, mid + 1, right)

	merge(arr, left, mid, right)


def merge(arr, left, mid, right):
	left_part = arr[left: mid + 1]
	right_part = arr[mid + 1: right + 1]


	i = j = 0
	k = left

	while i < len(left_part) and j < len(right_part):
		if left_part[i] <= right_part[j]:
			arr[k] = left_arr[i]
			i += 1
		else:
			arr[k] = right_arr[j]
			j += 1
		k += 1
