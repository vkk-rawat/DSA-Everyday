'''binary search is a searching algorithm used to find the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half. If the value of the target is less than the value in the middle of the interval, the search continues in the lower half. Otherwise, it continues in the upper half. This process is repeated until the target value is found or the interval is empty. Binary search is efficient with a time complexity of O(log n), making it much faster than linear search for large datasets.'''


'''Divide the search space into two halves by finding the middle index "mid". 
Compare the middle element of the search space with the key. 
If the key is found at middle element, the process is terminated.
If the key is not found at middle element, choose which half will be used as the next search space.
-> If the key is smaller than the middle element, then the left side is used for next search.
-> If the key is larger than the middle element, then the right side is used for next search.
This process is continued until the key is found or the total search space is exhausted.'''

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1   

if __name__ == "__main__":  
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binarySearch(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array") 
