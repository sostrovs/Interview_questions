def findMaxCrossArea(A, low, mid, high):
    left_sum = -float("inf")
    sumA = 0
    max_left = mid
    for i in range(mid, low-1,-1):
        hight = min(A[i], A[mid])
        width = mid - i
        sumA = hight * width
        if sumA > left_sum:
            left_sum = sumA
            max_left = i

    right_sum = -float("inf")
    sumA = 0

    max_right = mid+1
    if mid == high:
        max_right = mid
    for i in range(mid+1, high+1):
        hight = min(A[i], A[mid+1])
        width = i - (mid+1)
        sumA = hight * width
        if sumA > right_sum:
            right_sum = sumA
            max_right = i
    cross_sum = min(A[max_left], A[max_right])*(max_right-max_left)
    return max_left, max_right, max(cross_sum, left_sum, right_sum)

def findMaxArea(A, low, high):
    if high == low:
        return low, high, 0
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = findMaxArea(A, low, mid)
        right_low, right_high, right_sum = findMaxArea(A, mid+1, high)
        cross_low, cross_high, cross_sum = findMaxCrossArea(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def main():
    L = [[1,1], [1,8,6,2,5,4,8,3,7], [1,1,0], [4,3,2,1,4], [1,2,1], [1,8,8,1,1,1,1,1], [8,8]]
    for H in L:
        result = findMaxCrossArea(H, 0, len(H)//2, len(H)-1)
        print("Cross: ",result, H)
        result = findMaxArea(H, 0, (len(H)-1))
        print("Full: ",result, H)


if __name__ == '__main__':
    main()