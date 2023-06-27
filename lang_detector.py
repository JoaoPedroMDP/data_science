#  coding: utf-8
import argparse
import json
import pickle

from sklearn import svm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt

from extract_metrics import extract_metrics_from_phrase


MODEL_FILENAME = "model.pickle"

def calculate_success_rate(matrix: list[list[int]]):
    total = 0
    success = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]
            if i == j:
                success += matrix[i][j]
    
    print(f"Success rate: {success / total * 100}%")


def extract_languages_from_source(source: list[dict]):
    languages = {}
    for item in source:
        for key, phrase in item.items():
            if key not in languages:
                languages[key] = []

            languages[key].append(phrase)

    return languages


def look_for_trained_models():
    filename = MODEL_FILENAME
    try:
        loaded_model = pickle.load(open(filename, "rb"))
        print("Modelo carregado!!")
        return loaded_model
    except FileNotFoundError:
        print("Não existem modelos prontos.")
        return None


def main(new_phrase: str = None, save: bool = False):
    model = look_for_trained_models()
    if not model:
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
        print(phrases_metrics[0:10])
        model = svm.SVC().fit(phrases_metrics, phrases_langs)
        if save:
            print("Salvando modelo...")
            pickle.dump(model, open(MODEL_FILENAME, "wb"))

    with open("new_data.json", "r") as file:
        json_new_data = json.loads(file.read())
    
    errors = []
    if new_phrase:
        prediction = model.predict([extract_metrics_from_phrase(new_phrase)])
        print( f"{new_phrase} {prediction}")
    else:
        real_class = []
        predicted_class = []
        for item in json_new_data:
            for key, phrase in item.items():
                prediction = model.predict([extract_metrics_from_phrase(phrase)])
                real_class.append(key)
                predicted_class.append(prediction)
                if prediction != key:
                    errors.append((key, prediction, phrase))

                print( f"{phrase} ({key}): {prediction}")
        
        if len(errors) > 0:
            print("Erros:")
            print("Classe correta: classe predita (frase)")
            for error in errors:
                print(f"{error[0]}: {error[1]} ({error[2]})")

        mat = confusion_matrix(real_class, predicted_class)
        print(mat)
        calculate_success_rate(mat)
        cm_display = ConfusionMatrixDisplay(mat, display_labels=model.classes_)
        cm_display.plot()
        plt.savefig("confusion_matrix.png")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='LangDetector',
                    description='Detecta, entre as linguagens português, inglês e espanhol, a linguagem de um texto.'
                    )
    parser.add_argument('--phrase', required=False, help='Frase a ser analisada.')
    parser.add_argument('--save', help='Se deve salvar o modelo treinado.', action='store_true')
    args = parser.parse_args()
    main(args.phrase, args.save)
