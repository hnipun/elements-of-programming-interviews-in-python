# worst case : n^2
# avg case :  n^2
# best case : n^2

def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))


if __name__ == "__main__":
    main()
