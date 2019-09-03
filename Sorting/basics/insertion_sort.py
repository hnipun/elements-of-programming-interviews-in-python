# worst case : n^2
# avg case :  n^2
# best case : n

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def main():
    arr = [64, 25, 12, 22, 11]
    print(insertion_sort(arr))


if __name__ == "__main__":
    main()
