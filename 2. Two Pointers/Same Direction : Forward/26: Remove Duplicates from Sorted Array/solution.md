# Removing Duplicates from Sorted Array

## Problem Statement

You are given an integer array `nums` that is sorted in non-decreasing order. Your task is to remove the duplicates from this array in-place. After removing duplicates, you need to return the number of unique elements in the modified array. Additionally, you need to ensure that the unique elements are placed at the beginning of the array in the same order as they appear in the original array.

### Example

```python
Input: nums = [1, 1, 2, 2, 2, 3]
Output: 3
Modified Array: [1, 2, 3, ...] (The rest of the elements are not important)
```

## Approach

To solve this problem, we can use two pointers - a slow pointer and a fast pointer.

1. Initialize two pointers, `slow` and `fast`, both initially at index 0.
2. Start iterating through the array with the `fast` pointer.
3. Compare the elements at the `fast` and `slow` pointers. If they are the same, it means we've found a duplicate, so we move the `fast` pointer to the next element.
4. If the elements are different, it means we've found a unique element. In this case, we increment the `slow` pointer and copy the value from the `fast` pointer to the `slow` pointer's position. This step effectively removes duplicates by overwriting them with unique elements.
5. Continue this process until you've processed all elements in the array.
6. The `slow` pointer will be pointing to the last unique element, so the number of unique elements is `slow + 1`.
7. Return `slow + 1` as the answer.

## Python Implementation

Here's a Python implementation of the approach described above:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(0,len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]           
                

        
        return slow + 1

```

This algorithm efficiently removes duplicates in-place while maintaining the relative order of the elements. It returns the count of unique elements and updates the array to contain only the unique elements at the beginning.
