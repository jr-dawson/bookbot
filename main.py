
def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words(file_contents)
        count_characters(file_contents)

def count_words(book_string):
    num_words = len(book_string.split())
    print(f"{num_words} words found in the document\n")

def count_characters(book_string):
    char_dict = {}
    for char in book_string:
        char = char.lower()
        if char not in char_dict.keys():
            char_dict[char] = 1
        elif char in char_dict.keys():
            char_dict[char] += 1
        else:
            return 1
    char_report(char_dict)

def sort_on(dict):
    return dict["num"]

def char_report(char_dict: dict):
    dict_list = []
    for char in char_dict.items():
        dict_list.append({
            "char": char[0],
            "num": char[1]
        })
    dict_list.sort(reverse=True, key=sort_on)
    for indiv_char_dict in dict_list:
        if indiv_char_dict["char"].isalpha():
            if indiv_char_dict["num"] == 1:
                print(f"The {indiv_char_dict['char']} character was found {indiv_char_dict['num']} time")
            else:
                print(f"The {indiv_char_dict['char']} character was found {indiv_char_dict['num']} times")


main()