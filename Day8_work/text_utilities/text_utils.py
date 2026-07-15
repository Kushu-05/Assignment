from collections import Counter
class TextUtilities:
    def word_count(slef,text):
        words=text.split()
        count = Counter(words)
        return count
    def unique_words(slef,text):
        words= text.split()
        return list(set(words))
    
    def reverse_string(self, text):
        return text[::-1]