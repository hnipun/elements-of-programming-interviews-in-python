# worst case : n^2
# avg case :  n^2
# best case : n

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False

        for i in range(len(arr) - i - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if swapped == False:
            break

    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
