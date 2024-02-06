def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        middle = arr[mid]
        if middle < target:
            left = mid + 1
        elif middle > target:
            right = mid - 1
        else:
            return mid
    return -1


def main():
    print(binary_search([1, 3, 4, 6, 7, 8, 10, 13, 14], 4))

if __name__ == "__main__":
    main()