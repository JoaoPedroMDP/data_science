#  coding: utf-8
import json

from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt

from extract_metrics import extract_metrics_from_phrase


def calculate_success_rate(matrix: list[list[int]]):
    total = 0
    success = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]
            if i == j:
                success += matrix[i][j]
    
    print(f"Success rate: {success / total * 100}%")

def main():
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
    
    real_class = []
    predicted_class = []
    for item in json_new_data:
        for key, phrase in item.items():
            predito = model.predict([extract_metrics_from_phrase(phrase)])
            real_class.append(key)
            predicted_class.append(predito)
            print( f"{phrase} ({key}): {predito}")
    
    mat = confusion_matrix(real_class, predicted_class)
    print(mat)
    calculate_success_rate(mat)
    cm_display = ConfusionMatrixDisplay(mat, display_labels=model.classes_)
    cm_display.plot()
    plt.savefig("confusion_matrix.png")
    

if __name__ == "__main__":
    main()
