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


def words_ending_with_d_percentage(words: list[str]):
    count = 0
    for word in words:
        if word.endswith("d"):
            count += 1

    return count / len(words)


def count_substring_occurrences(words: list[str], substring: str):
    count = 0
    for word in words:
        if substring in word:
            count += 1

    return count

def count_y_occurrences(words: list[str]):
    return count_substring_occurrences(words, "y")


def have_substring(words: list[str], substring: str):
    for word in words:
        if substring in word:
            return 1

    return 0

def have_th_substring(words: list[str]):
    return have_substring(words, "th")

def have_ng_substring(words: list[str]):
    return have_substring(words, "ng")

def have_ing_substring(words: list[str]):
    return have_substring(words, "ing")

def have_ph_substring(words: list[str]):
    return have_substring(words, "ph")

def have_ght_substring(words: list[str]):
    return have_substring(words, "ght")


def y_occurence_percentage(words: list[str]):
    count = 0
    for word in words:
        for letter in word:
            if letter == "y":
                count += 1

    return count / len(words)

def have_words_ending_with(words: list[str], substring: str):
    for word in words:
        if word.endswith(substring):
            return 1
    
    return 0

def have_words_ending_with_y(words: list[str]):
    return have_words_ending_with(words, "y")

def have_words_ending_with_n(words: list[str]):
    return have_words_ending_with(words, "n")

def have_words_ending_with_l(words: list[str]):
    return have_words_ending_with(words, "l")

def have_words_ending_with_ing(words: list[str]):
    return have_words_ending_with(words, "ing")

def have_words_ending_with_th(words: list[str]):
    return have_words_ending_with(words, "th")

def have_words_ending_with_d(words: list[str]):
    return have_words_ending_with(words, "d")


def extract_metrics_from_phrase(phrase: str):
    # 75% -> words_mean_length, words_vowel_percentage, have_words_ending_with_n, have_words_ending_with_ng, have_words_ending_with_l
    # 83% -> words_mean_length, words_vowel_percentage, have_words_ending_with_n, have_words_ending_with_ng, have_words_ending_with_l, have_th_substring, have_ng_substring, have_ph_substring
    
    metrics = [
        words_mean_length,
        words_vowel_percentage,
        # have_words_ending_with_y,
        have_words_ending_with_n,
        have_words_ending_with_ing,
        have_words_ending_with_l,
        # have_words_ending_with_d,
        # words_ending_with_d_percentage,
        # count_y_occurrences,
        # y_occurence_percentage,
        # have_words_ending_with_th,
        have_th_substring,
        have_ng_substring,
        # have_ing_substring,
        have_ph_substring,
        have_ght_substring
    ]
    splitted = phrase.split(" ")
    metrics_values = []
    for metric in metrics:
        metrics_values.append(metric(splitted))
    # print(f"{' '.join(splitted)} : {metrics_values}")
    return metrics_values