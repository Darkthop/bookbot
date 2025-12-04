#!/usr/bin/env python3
from stats import *
from report import print_report_header , print_char_counts
from sys import exit , argv



def main():

    if len(argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    try:
        book_text = get_book_text(argv[1])
    except:
        print("Exiting Program")
        exit(1)
    
    print_report_header(book_text)

    print_char_counts(book_text)


if __name__ == "__main__":
    main()