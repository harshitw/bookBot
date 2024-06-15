import sys
import collections

def main():

    book_path = "books/frankenstein.txt"

    text = get_book_path(book_path)

    word_count = count_words_in_book(text)

    character_frequency_map = count_character_frequency(text)

    print("{} words found in the document. \n\n".format(word_count))

    for key, val in sorted(character_frequency_map.items(), key=lambda x:x[1]):
        if key.isalpha() == True:
            print("The '{}' character was found {} times\n".format(key, val))
    
    print(" --- End report ---")


def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words_in_book(text):
    return len(text.split())

def count_character_frequency(text):
    words = str(text.split()).lower()
    freqMap = collections.defaultdict(int)
    for word in words:
        for char in word:
            freqMap[char] += 1
    print(freqMap)
    return freqMap

main()