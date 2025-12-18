
import sys
from stats import get_num_words, get_characters_dict, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #stops program
    book_path = sys.argv[1]
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




