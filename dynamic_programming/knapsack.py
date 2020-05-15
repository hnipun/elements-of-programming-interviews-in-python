def knapSack(W, wt, val, n):
    #base case
    if n == 0 or W ==0:
        return 0

    if wt[n-1]> W:
        return knapSack(W,wt,val,n-1)
    else:
        return max(knapSack(W,wt,val,n-1),val[n-1] + knapSack(W-wt[n-1],wt,val,n-1))

def knapSackDp(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        print(i)
        for w in range(W + 1):
            print(w)
            if i == 0 or w == 0:
                print("*")
                K[i][w] = 0
            elif wt[i - 1] <= w:
                print("**")
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                print(val[i - 1] + K[i - 1][w - wt[i - 1]])
                print(K[i - 1][w])
            else:
                print("***")
                K[i][w] = K[i - 1][w]

    print(n)
    print(w)
    return K[n][W]


def main():
    # To test above function
    val = [12, 25, 24,15,14]
    wt = [2, 2, 6,4,5]
    W = 10
    n = len(val)
    print (knapSackDp(W, wt, val, n))


if __name__ == "__main__":
    print(1%3)
