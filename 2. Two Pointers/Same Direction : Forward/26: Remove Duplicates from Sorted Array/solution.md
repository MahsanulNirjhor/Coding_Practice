# Removing Duplicates from Sorted Array

## Problem Statement

You are given an integer array `nums` that is sorted in non-decreasing order. Your task is to remove the duplicates from this array in-place. After removing duplicates, you need to return the number of unique elements in the modified array. Additionally, you need to ensure that the unique elements are placed at the beginning of the array in the same order as they appear in the original array.

### Example

```python
Input: nums = [1, 1, 2, 2, 2, 3]
Output: 3
Modified Array: [1, 2, 3, ...] (The rest of the elements are not important)
```

## Edge Cases
When solving problems related to removing duplicates from a sorted array, it's important to consider various edge cases to ensure that your solution works correctly and efficiently. Here are some edge cases you should consider, along with examples:

1. **Empty Array**:
   - Input: `[]`
   - Expected Output: `0`
   - Explanation: When the input array is empty, there are no duplicates to remove, and the result should be 0.

2. **Array with No Duplicates**:
   - Input: `[1, 2, 3, 4, 5]`
   - Expected Output: `5`
   - Explanation: When there are no duplicates in the input array, the output should be the length of the original array, and the array itself remains unchanged.

3. **Array with All Duplicates**:
   - Input: `[1, 1, 1, 1, 1]`
   - Expected Output: `1`
   - Explanation: When all elements in the input array are the same, the output should be 1 (the length of the array after removing duplicates), and the array should contain only one unique element.

4. **Array with Some Duplicates**:
   - Input: `[1, 1, 2, 2, 3, 3, 4, 5]`
   - Expected Output: `5`
   - Explanation: The input array has some duplicates, but they should be removed, and the result should contain only the unique elements, with the relative order preserved.

5. **Array with Negative Numbers**:
   - Input: `[-2, -1, -1, 0, 1, 1, 2, 3]`
   - Expected Output: `6`
   - Explanation: The input array can contain negative numbers, and the solution should work correctly for such cases.

6. **Large Input Array**:
   - Input: `[1, 1, 2, 2, ... 100000]` (an array with a large number of duplicates)
   - Expected Output: `2`
   - Explanation: Consider cases where the input array is very large. The solution should still run efficiently and produce the correct result.

7. **Performance Test**:
   - Input: `[1, 2, 3, 4, 5, ..., 100000]` (a large sorted array with no duplicates)
   - Expected Output: `100000`
   - Explanation: Test the performance of your solution on a large input array with no duplicates.

8. **Single Element Array**:
   - Input: `[42]` (an array with only one element)
   - Expected Output: `1`
   - Explanation: When there's only one element in the array, there are no duplicates, and the result should be 1.

## My Suggestion
I suggest solve this problem using two pointers (a slow pointer and a fast pointer) because this is a common and efficient approach for solving problems that involve removing duplicates from a sorted array in-place while maintaining the relative order of the elements. Here's how I arrived at this conclusion:

1. **Sorted Array**: The problem statement mentions that the input array `nums` is sorted in non-decreasing order. When dealing with sorted arrays, it's often beneficial to use pointers to compare and manipulate elements efficiently.

2. **Remove Duplicates In-Place**: To remove duplicates in-place means that we should modify the original array without using additional data structures like sets or dictionaries. This suggests that we need to work with the array's elements directly.

3. **Maintain Relative Order**: The problem also specifies that we must maintain the relative order of the elements. This means that if two distinct elements appear consecutively in the input array, they should also appear consecutively in the modified array.

Given these considerations, a common approach is to use two pointers:

- The `slow` pointer points to the current position in the modified array where unique elements are stored.
- The `fast` pointer iterates through the original array to check for duplicates.

By comparing the elements at the `slow` and `fast` pointers, we can efficiently identify duplicates and copy unique elements to their correct positions while maintaining the relative order. This approach is well-suited for this problem because it avoids the need for additional data structures and takes advantage of the fact that the array is already sorted.

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
