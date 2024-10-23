def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_characters(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(input_text):
    return len(input_text.split())

def count_characters(input_text):
    characters = {}
    for c in input_text:
        c_lowered=c.lower()
        if c_lowered in characters:
            characters[c_lowered]+=1
        else:
            characters[c_lowered]=1

    return characters

    
main()