def merge_sort(arr, l, r):
    if (l < r):

        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    k = 0
    temp = [0] * (r - l + 1)

    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    arr[l:r + 1] = temp

def anagram_checking_off(s1, s2):
    if len(s1) != len(s2):
        return False

    to_check_off = list(s2)

    for char in s1:
        for i, other_char in enumerate(to_check_off):
            if char == other_char:
                to_check_off[i] = None
                break
        else:
             return False

    return True


def main():
    # arr = [38, 27, 43, 3, 9, 82, 10]
    # merge_sort(arr, 0, len(arr) - 1)
    # print(arr)
    print(anagram_checking_off('abcd', 'dcba'))
    ret = 'ba'
    word = 'ab'
    print(sorted(['cd','',ret, word ]))


if __name__ == "__main__":
    main()
