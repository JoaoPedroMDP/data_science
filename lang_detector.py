#  coding: utf-8
import json
import sys

from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from extract_metrics import extract_metrics_from_phrase


def detect(phrase: str):
    pass


def main():
    # Read the file
    file = open("phrases.txt", "r")
    text = file.read()
    file.close()
    detect(text)


def train():
    print("Training...")

    def extract_languages_from_source(source: list[dict]):
        languages = {}
        for item in source:
            for key, phrase in item.items():
                if key not in languages:
                    languages[key] = []

                languages[key].append(phrase)

        return languages

    file = open("train_data.json", "r")
    json_train_data = json.loads(file.read())
    file.close()
    # Train the model
    languages = extract_languages_from_source(json_train_data)

    phrases_metrics = []
    phrases_langs = []
    for language, phrases in languages.items():
        for phrase in phrases:
            phrases_metrics.append(
                extract_metrics_from_phrase(phrase))
            phrases_langs.append(language)

    print(phrases_metrics)
    print(phrases_langs)
    model = svm.SVC().fit(phrases_metrics, phrases_langs)

    file = open("new_data.json", "r")
    json_new_data = json.loads(file.read())
    file.close()
    
    classe_real = []
    classe_predita = []
    for item in json_new_data:
        for key, phrase in item.items():
            predito = model.predict([extract_metrics_from_phrase(phrase)])
            classe_real.append(key)
            classe_predita.append(predito)
            print( f"{key}: {predito}")
    
    mat = confusion_matrix(classe_real, classe_predita)
    cm_display = ConfusionMatrixDisplay(mat)
    cm_display.plot()
    

if __name__ == "__main__":
    train()
