import json
from difflib import SequenceMatcher

my_data = json.load(open('data.json'))


def print_result(my_input):
    result_list = my_data['{}'.format(my_input)]
    for number, definition in enumerate(result_list):
        print(number + 1, definition)
    translate()


def translate():
    user_word = input('Enter a word to check.\nIf you want to quit type: quit \n').lower()
    if user_word == 'quit':
        quit()
    elif user_word.title() in my_data:
        print_result(user_word.title())
    elif user_word.upper() in my_data:
        print_result(user_word.upper())
    elif user_word in my_data:
        print_result(user_word)
    else:
        best_match_ratio = 0
        best_match = None
        for word in my_data:
            ratio = SequenceMatcher(None, user_word, word).ratio()
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                best_match = word
        print('Did you mean: {}'.format(best_match))
        user_answer = input('Type: Y if yes, N if no.').lower()
        if user_answer == 'y':
            print_result(best_match)
            translate()
        else:
            translate()


if __name__ == '__main__':
    translate()
