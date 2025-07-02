#stats.py

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()

    return book_contents

def count_words(word_count):
    num_words = len(word_count.split())

    return num_words

def count_char(char_count):
    character_dict = {}
    words = char_count.split()
    for word in words:
        lower_case = word.lower()
        for letter in lower_case:
            if letter not in character_dict:
                character_dict[letter] = 1
            else:
                character_dict[letter] += 1
    return character_dict

def sorted_list_chars(char_count):
    sorted_chars = []
    sorted_dict = count_char(char_count)
    for key in sorted_dict:
        sorted_chars.append({"char": key, "num" : sorted_dict[key]})
    def sort_on(sorted_dict):
        return sorted_dict["num"]
    sorted_chars.sort(reverse=True, key = sort_on)
    return sorted_chars



