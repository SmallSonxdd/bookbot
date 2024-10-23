def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(len(text.split()))


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()