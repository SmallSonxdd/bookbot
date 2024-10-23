def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count=count_characters(text)
    word_count=count_words(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    print('')
    print_report_of_character_count(character_count)
    print('--- End report ---')

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


def print_report_of_character_count(dict_of_charater_their_count):
    for key in dict_of_charater_their_count:
        print(f'The {key} character was found {dict_of_charater_their_count[key]} times')
    pass

main()