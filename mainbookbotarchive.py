from stats import get_num_words, get_characters_dict, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_characters_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # --- EVERYTHING BELOW IS NOW INDENTED ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")

# Execute main function
main()