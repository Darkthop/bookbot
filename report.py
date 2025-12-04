from stats import get_char_dict,get_num_words

def print_report_header(book_text : str):
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book_text)} total words")
        print("--------- Character Count -------")

def print_char_counts(book_text):

    result = get_char_dict(book_text)
    for r in result:
        print(f"{r["char"]}: {r["num"]}")

    #Print END
    print("============= END ===============")