def main():
    books = "books/frankenstein.txt"
    text =  book_text(books)
    num_words = word_count(text)
    char_counts = char_count(text)
    report(char_counts, num_words)
    # print(text)
    # print(num_words)
    # print(char_counts)

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    num_char = {}
    for char in lowercase:
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def report(char_count, word_count):
    alph_dict = {}
    for char, count in char_count.items():
        if char.isalpha():
            alph_dict[char] = count
    
    char_list = []
    for char, count in alph_dict.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key = sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")

    print("--- End Report ---")
main()