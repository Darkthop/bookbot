def get_book_text(filepath) -> str:
    try:
        with open(filepath) as book:
            return book.read()
    except OSError as e:
        print(f"Wrong File Path : {e}")

def get_num_words(string : str) -> int:
    return len(string.split())

def get_char_dict(book_text : str) -> list:
    book_text = book_text.lower()
    words = book_text.split()

    consolidated_string = str()

    result = []

    for word in words:
        consolidated_string += word
    
    for char in consolidated_string:

        if not char.isalpha() : continue

        found = False
        for r in result:
            if r["char"] == char : 
                r["num"] += 1
                found = True
        
        if not found:
            result.append({"char" : char,"num" : 1})

    return sorted(result,key=lambda item : item["num"],reverse=True)

