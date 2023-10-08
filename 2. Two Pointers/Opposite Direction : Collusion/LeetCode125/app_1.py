def isPalindrome(s):
    # Step 1: Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if the modified string is equal to its reverse
    return s == s[::-1]
