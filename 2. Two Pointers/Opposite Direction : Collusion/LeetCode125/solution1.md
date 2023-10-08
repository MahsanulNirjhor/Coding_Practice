# Problem Solving: Checking Palindromes in Python

## Introduction
A common problem in programming is determining whether a given string is a palindrome. A palindrome is a sequence of characters that reads the same forwards and backward. However, when checking for palindromes, we often want to ignore certain aspects like letter case and non-alphanumeric characters.

In this article, we'll explore an approach to solve this problem using Python. We'll break down the steps, provide an intuitive explanation, and analyze the time and space complexity of the solution. This article is beginner-friendly and aims to help you understand the problem-solving process.

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Intuition](#intuition)
3. [Python Implementation](#python-implementation)
4. [Time Complexity](#time-complexity)
5. [Space Complexity](#space-complexity)
6. [Conclusion](#conclusion)

## Problem Statement
Given a string `s`, we need to determine if it is a palindrome. To do this, we should:

1. Convert the entire input string to lowercase to ensure case insensitivity.
2. Remove all non-alphanumeric characters (such as spaces and punctuation) from the string.
3. Compare the modified string with its reverse to check if it's a palindrome.

## Intuition
The intuition behind this approach is that by removing non-alphanumeric characters and converting the string to lowercase, we eliminate potential sources of difference that don't affect the palindrome property. This allows us to focus solely on the alphanumeric characters in the string.

For example, in the input string "A man, a plan, a canal: Panama," after converting to lowercase and removing non-alphanumeric characters, we get "amanaplanacanalpanama," which is a palindrome when read forwards or backwards.

The pattern here is that a palindrome remains the same when its characters are read in reverse order. Therefore, if the modified string (with lowercase and non-alphanumeric characters removed) is the same as its reverse, the original string is a palindrome.

## Python Implementation
Here's the Python code to implement this approach:

```python
def isPalindrome(s):
    # Step 1: Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if the modified string is equal to its reverse
    return s == s[::-1]
```

## Time Complexity
The time complexity of this solution is determined by the following operations:
1. Converting the string to lowercase and removing non-alphanumeric characters, which takes O(n) time, where n is the length of the input string.
2. Checking if the modified string is a palindrome using slicing, which also takes O(n) time.

Overall, the time complexity is O(n).

## Space Complexity
The space complexity of this solution includes the following components:
1. Original input string `s`: O(n), where 'n' is the length of the input string.
2. Modified string `s`: O(n) in the worst case (if the input string has no non-alphanumeric characters).
3. Additional variables: O(1), as they use constant space.

The total space complexity of the function is O(n + 1), which simplifies to O(n).

## Conclusion
This approach efficiently solves the problem of checking whether a string is a palindrome while considering alphanumeric characters and ignoring case. It provides a clear and intuitive solution suitable for beginners and is especially useful when dealing with large strings.

Feel free to use the provided Python code and explanations to check for palindromes in your own projects. Happy coding!