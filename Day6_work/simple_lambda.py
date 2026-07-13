import time
add=lambda x, y: x + y
print(add(5, 3))
find_largest=lambda sentences: max(sentences, key=len)
sentence=input("Enter a sentence: ")
start_time = time.perf_counter()

largest_word=find_largest(sentence)
end_time = time.perf_counter()
print("Largest word in the sentence is:", largest_word)
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")