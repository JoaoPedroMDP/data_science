#  coding: utf-8

def words_mean_length(words: list[str]):
    mean = 0
    for word in words:
        mean += len(word)

    return mean / len(words)


def words_vowel_percentage(words: list[str]):
    count = 0
    for word in words:
        for letter in word:
            if letter in "aeiou":
                count += 1

    return count / len(words)


def have_words_ending_with_n(words: list[str]):
    count = 0
    for word in words:
        if word[-1] == "n":
            count += 1

    if count > 0:
        return 1
    
    return 0



def extract_metrics_from_phrase(phrase: str):
    splitted = phrase.split(" ")
    return [
        words_mean_length(splitted),
        words_vowel_percentage(splitted),
        have_words_ending_with_n(splitted)
    ]


def extract_metrics_from_data_source(item: str):
    return extract_metrics_from_phrase(item)
