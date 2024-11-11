from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt


def main():
    # 0 = dog, 1 =cat, 2 = bird
    data_labels = ['dog', 'cat', 'bird']
    # "Run" for images of dogs, cats, and birds
    actual_results = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    prediction = [2, 2, 0, 1, 1, 1, 1, 1, 2, 2, 0, 2]
    ideal_results = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    print(f'Accuracy = {accuracy_score(actual_results, prediction)*100: .2f}%')
    print(f'Confusion matrix:\n{confusion_matrix(actual_results, prediction)}')
    print(f'Classification report:\n{classification_report(
        actual_results, prediction, target_names=data_labels)}')
    # # Generate a confusion matrix
    # cm = confusion_matrix(actual_results, ideal_results)
    # disp = ConfusionMatrixDisplay(
    #     confusion_matrix=cm, display_labels=data_labels)
    # disp.plot()
    # plt.title('Ideal Confusion Matrix')
    # plt.show()

    # # Generate a ideal confusion matrix
    # cm = confusion_matrix(actual_results, prediction)
    # disp = ConfusionMatrixDisplay(
    #     confusion_matrix=cm, display_labels=data_labels)
    # disp.plot()
    # plt.title('Prediction Confusion Matrix')
    # plt.show()


if __name__ == '__main__':
    main()
