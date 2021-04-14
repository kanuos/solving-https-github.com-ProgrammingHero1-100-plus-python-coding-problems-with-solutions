import requests


def get_all_words():
    url = "http://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(url)
    data = response.text.split("\n")
    return data


def generate_four_letter_words():
    data = get_all_words()
    four_letter_words = [x for x in data if len(x) == 4]
    return four_letter_words
