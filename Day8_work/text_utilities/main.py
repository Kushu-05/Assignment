from text_utils import TextUtilities
obj = TextUtilities()
while True :
    print("\n==== Text Utilities====")
    print("1. Word Count:")
    print("2. Unique Words:")
    print("3. Reverse String")
    print("4.Exit")

    choice = int(input("Enter your choice:"))
    if choice ==1:
        text =input("Enter text: ")
        result =obj.word_count(text)
        print("Word Frequency:")
        for word, count in result.items():
            print(word, ":",count)

    elif choice ==2:
        text=input("Enter text:")
        print("Unique Words: ", obj.unique_words(text))
    elif choice==3:
        text =input("Enter Text: ")
        print("Reversed String",obj.reverse_string(text))
    elif choice ==4:
        print("Existing...")
        break
    else:
        print("Invalid Choice")