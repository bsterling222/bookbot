from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    # print (book_text)
    result = word_count(book_text)
    print(f"{result} words found in the document")
    num_char = char_count(book_text)
    print(num_char)

main()