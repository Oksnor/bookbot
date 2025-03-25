from stats import (
    get_num_words, 
    get_num_char, # import the functions used in the main function
    sort_dict,
)

import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_filepath): # function to find and open and return a file on a given path
    with open(book_filepath) as f:
        return f.read()

def main():
    book_text = get_book_text(book_path) # book_text variable becomes the entire file get_book_text finds
    word_count = get_num_words(book_text) # word_count becomes the number of words found by the get_num_words function, it uses the book_text variable as input for the function
    char_count = get_num_char(book_text) # char_count becomes a dict with the charachters found and how many with the get_num_char function, it uses the book_text variable as input for the function
    dict_sort = sort_dict(char_count) # dict_sort becomes a list with as many dictionaries as there are different letters, it uses the char_count variable as input for the function
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in dict_sort: 
        symbol = dict["symbol"]
        number = dict["number"]
        print(f"{symbol}: {number}")
    print("============= END ===============")
    


main()