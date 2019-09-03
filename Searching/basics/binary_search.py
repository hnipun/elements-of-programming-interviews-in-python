# via recurssion
def bsearch(A, l, r, t):
    # Check base case
    if r >= l:

        mid = (l + r) // 2

        if A[mid] == t:
            return mid

        if A[mid] > t:
            return bsearch(A, l, mid - 1, t)
        else:
            return bsearch(A, mid + 1, r, t)

    else:
        return -1


# via iteration
def binaryserach(A, t):
    r = len(A) - 1
    l = 0

    while r >= l:
        mid = (l + r) // 2

        if A[mid] == t:
            return mid

        if A[mid] > t:
          r = mid -1
        else:
          l = mid +1

    return -1

def main():
    A = [1, 2, 3, 4, 5, 6]

    t =5

    #print(bsearch(A, 0, 5, t))
    print(binaryserach(A, t))


if __name__ == "__main__":
    main()
