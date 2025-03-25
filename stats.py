def get_num_words(text):
    words = text.split()
    num_words = 0
    for i in range(0, len(words), 1):
        num_words += 1
    return num_words

def get_num_char(text):
    lowertext = text.lower()
    char_dict = {}
    for char in lowertext:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["number"]

def sort_dict(char_count):
    dict_list = []
    for symbol in char_count:
        if symbol.isalpha():
            number = char_count[symbol]
            tempt_dict = {}
            tempt_dict["symbol"] = symbol
            tempt_dict["number"] = number
            dict_list.append(tempt_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

