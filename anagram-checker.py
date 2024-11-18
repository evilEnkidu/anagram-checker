def is_anagram(str1, str2):

    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    if len(str1) != len(str2):
        return False
    
    char_count1 = {}
    char_count2 = {}
    
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    return char_count1 == char_count2

def main():
    while True:
        print("\nAnagram Checker")
        print("Enter 'quit' at any time to exit")
        
        str1 = input("Enter the first string: ")
        if str1.lower() == 'quit':
            break
            
        str2 = input("Enter the second string: ")
        if str2.lower() == 'quit':
            break
        
        if is_anagram(str1, str2):
            print(f"'{str1}' and '{str2}' are anagrams!")
        else:
            print(f"'{str1}' and '{str2}' are not anagrams.")

if __name__ == "__main__":
    main()
