#main.py
from stats import get_book_text, count_words, count_char, sorted_list_chars
import sys

def main():

    input = sys.argv[1]
    book_contents = get_book_text(input)
    word_counting = count_words(book_contents)
    char_counting = count_char(input)
    letter_counting = sorted_list_chars(book_contents)


    print(f"\n ============ BOOKBOT ============")
    print(f"\n Analyzing book found at {input}...")
    print(f"\n ----------- Word Count ----------")
    print(f"\n Found {word_counting} total words.")
    print(f"\n --------- Character Count -------")
    for dictionary in letter_counting:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")
    
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()