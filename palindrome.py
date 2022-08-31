def isPalindrome(test_word):
    list = test_word
    list2 = list[::-1]
    print("Test_word is " + list)
    print("Test_word reversed is " + list2)
    if list == list2:
        print(test_word + " is a palindrome")
    elif list != list2: 
        print(test_word + " is not a palindrome")
    else: 
        print("You need to enter a string value.")
    return

isPalindrome('racecar')
print("Will this work for a start with capitals?")
isPalindrome('Racecar')
print("We need to make all letters lower case.")

def isPalindrome2(test_word):
    test_word_lower = test_word.lower()
    list = test_word_lower
    list2 = list[::-1]
    print("Test_word is " + test_word)
    print("Test_word_lower is " + list)
    print("Test_word reversed is " + list2)
    if list == list2:
        print(test_word + " is a palindrome")
    elif list != list2: 
        print(test_word + " is not a palindrome")
    else: 
        print("You need to enter a string value.")
    return

isPalindrome2('Racecar')
