def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    while text:
        char = text[0]
        if char in vowels:
            count += 1
        text = text[1:]
    return count
sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"The number of vowels in the sentence is: {vowel_count}")