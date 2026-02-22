# Given Questions: Sort given array make square of each element and return sorted array of squares.


def sortedSquares(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        result[i] = nums[i] ** 2

    result.sort()
    return result


# Test the function
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    result = sortedSquares(nums)
    print("Input:", nums)
    print("Sorted squares:", result)