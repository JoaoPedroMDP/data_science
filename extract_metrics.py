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


def count_substring_occurrences(words: list[str], substring: str):
    count = 0
    for word in words:
        if substring in word:
            count += 1

    return count


def count_y_occurrences(words: list[str]):
    return count_substring_occurrences(words, "y")


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


def have_words_ending_with_ng(words: list[str]):
    return have_words_ending_with(words, "ng")


def extract_metrics_from_phrase(phrase: str):
    # 75% -> words_mean_length, words_vowel_percentage, have_words_ending_with_n, have_words_ending_with_ng, have_words_ending_with_l

    metrics = [
        words_mean_length,
        words_vowel_percentage,
        # have_words_ending_with_y,
        have_words_ending_with_n,
        have_words_ending_with_ng,
        have_words_ending_with_l,
        # count_y_occurrences,
        # y_occurence_percentage,
    ]
    splitted = phrase.split(" ")
    metrics_values = []
    for metric in metrics:
        metrics_values.append(metric(splitted))
    
    return metrics_values
