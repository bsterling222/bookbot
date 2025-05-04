def word_count(book_text):
    return len(book_text.split())

def char_count(book_text):
    char_list = {}
    lower_book_text = book_text.lower()
    for char in lower_book_text:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list