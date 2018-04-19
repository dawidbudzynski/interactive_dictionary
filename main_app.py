import json
from difflib import SequenceMatcher

from flask import Flask, render_template, request

my_data = json.load(open('data.json'))


def print_result(my_input):
    result_list = my_data['{}'.format(my_input)]
    result_list_enumerated = []
    for number, definition in enumerate(result_list):
        result_list_enumerated.append([number + 1, definition])
    return result_list_enumerated


def translate(user_word):
    user_word = user_word.lower()

    if user_word.title() in my_data:
        return print_result(user_word.title())
    elif user_word.upper() in my_data:
        return print_result(user_word.upper())
    elif user_word in my_data:
        return print_result(user_word)
    else:
        best_match_ratio = 0
        best_match = None
        for word in my_data:
            ratio = SequenceMatcher(None, user_word, word).ratio()
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                best_match = word
        definitions = print_result(best_match)
        result = ['wrong']
        result.append(best_match)
        result.append(definitions)
        return result


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dictionary():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        user_word = request.form['word']
        if user_word == '':
            return render_template('form_wrong.html')
        result = translate(user_word)
        if result[0] == 'wrong':
            return render_template("result_wrong_input.html", user_word=user_word, result=result)
        return render_template("result.html", user_word=user_word, result=result)


if __name__ == '__main__':
    app.run()
