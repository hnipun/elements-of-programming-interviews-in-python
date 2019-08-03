import heapq

def main():
    H = [21,1,45,78,3,5]

    # Use heapify to rearrange the elements
    heapq._heapify_max(H)
    #heapq.heapify(H)
    print(H)

    # Add element
    heapq.heappush(H, 8)
    print(H)

    # Remove element from the heap
    heapq.heappop(H)
    print(H)

    # Replace an element
    heapq.heapreplace(H, 6)  # returns the smallest elemnt
    print(H)

    # push pop up
    heapq.heappushpop(H, 4)  # returns the smallest elemnt
    print(H)

    print(heapq.nlargest(3,H)) # not poping
    print(heapq.nsmallest(3,H))
    print(H)

if __name__ == "__main__":
    main()
    H = [9, 7, 4, 2, 6, 1, 3]

    # Use heapify to rearrange the elements
    heapq._heapify_max(H)
    print(H)


