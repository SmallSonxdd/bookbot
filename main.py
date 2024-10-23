def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count=count_characters(text)
    word_count=count_words(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    print('')
    print_sorted_list_of_dictionaries(sort_dict(dict_split_into_list_of_dictionaries_per_character(text)))
    print('--- End report ---')
    

def sort_on(dict):
    return dict["num"]

def sort_dict(input_text):
    input_text.sort(reverse=True, key=sort_on)
    return input_text


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(input_text):
    return len(input_text.split())

def count_characters(input_text):
    characters = {}
    for c in input_text:
        c_lowered=c.lower()
        if c_lowered.isalpha() == True:
            if c_lowered in characters:
                characters[c_lowered]+=1
            else:
                characters[c_lowered]=1

    return characters


def dict_split_into_list_of_dictionaries_per_character(input_text):
    characters_dict=count_characters(input_text)
    list_of_dict_of_characters=[]
    for key in characters_dict:
        char_dict = {'character': key, "num": characters_dict[key]}
        list_of_dict_of_characters.append(char_dict)
    return list_of_dict_of_characters

def print_sorted_list_of_dictionaries(input_text):
    for i in input_text:
        print(f'The {i["character"]} character was found {i["num"]} times')
    pass


main()