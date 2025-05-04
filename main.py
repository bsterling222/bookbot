from stats import word_count, char_count, report, print_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    # print (book_text)
    total_words = word_count(book_text)
    char_counts = char_count(book_text)
    # sorted_characters = report(char_counts)
    print_report(total_words,char_counts, filepath)

    # print(char_counts)
    # print(f"{total_words} words found in the document")

main()