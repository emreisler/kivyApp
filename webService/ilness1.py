import csv
import sys
import calendar

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

class _Ilness1:
    def __init__(self):
        self.main()

    def main(self):

        # Load data from spreadsheet and split into train and test sets
        evidence, labels = self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(
            evidence, labels, test_size=TEST_SIZE
        )
        # Train model and make predictions
        self.model = self.train_model(X_train, y_train)
        predictions = self.model.predict(X_test)
        sensitivity, specificity = self.evaluate(y_test, predictions)

        # Print results
        print(f"Correct: {(y_test == predictions).sum()}")
        print(f"Incorrect: {(y_test != predictions).sum()}")
        print(f"True Positive Rate: {100 * sensitivity:.2f}%")
        print(f"True Negative Rate: {100 * specificity:.2f}%")


    def load_data(self):
        evidence_list = list()
        label_list = list()

        with open("disiase1.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                evidence_list.append(
                    [float(row["meas1"]),
                     float(row["meas2"]),
                     float(row["meas3"]),
                     float(row["meas4"]),
                     float(row["meas5"])
                     ]
                )
                label_list.append(1 if row["harmful"] == "TRUE" else 0)


        loaded_data = (evidence_list, label_list)
        #print(len(evidence_list),len(label_list),len(evidence_list[0]),len(evidence_list[750]))


        return loaded_data
        """
        Load shopping data from a CSV file `filename` and convert into a list of
        evidence lists and a list of labels. Return a tuple (evidence, labels).
    
        evidence should be a list of lists, where each list contains the
        following values, in order:
            - Administrative, an integer 0 OK
            - Administrative_Duration, a floating point number 1 OK
            - Informational, an integer 2 OK
            - Informational_Duration, a floating point number 3 OK
            - ProductRelated, an integer 4 OK
            - ProductRelated_Duration, a floating point number 5 OK
            - BounceRates, a floating point number 6 OK
            - ExitRates, a floating point number 7 OK
            - PageValues, a floating point number 8 OK
            - SpecialDay, a floating point number 9 OK
            - Month, an index from 0 (January) to 11 (December) 10 
            - OperatingSystems, an integer 11
            - Browser, an integer 12 
            - Region, an integer 13
            - TrafficType, an integer 14
            - VisitorType, an integer 0 (not returning) or 1 (returning) 15 
            - Weekend, an integer 0 (if false) or 1 (if true) 16
    
        labels should be the corresponding list of labels, where each label
        is 1 if Revenue is true, and 0 otherwise.
        """



    def train_model(self,evidence, labels):

        trainModel = KNeighborsClassifier(n_neighbors=1)
        fittedModel = trainModel.fit(evidence,labels)
        return fittedModel
        """
        Given a list of evidence lists and a list of labels, return a
        fitted k-nearest neighbor model (k=1) trained on the data.
        """



    def evaluate(self,labels, predictions):
        total_true = 0
        total_false = 0
        sensitivity = 0
        specificty = 0

        for i in range(len(labels)):
            if labels[i] == 1:
                total_true += 1
                if predictions[i] == labels[i] :
                    sensitivity += 1
            elif labels[i] == 0:
                total_false += 1
                if predictions[i] == labels[i]:
                    specificty += 1

        sensitivity = sensitivity/total_true
        specificty = specificty/total_false
        return sensitivity, specificty

        """
        Given a list of actual labels and a list of predicted labels,
        return a tuple (sensitivity, specificty).
    
        Assume each label is either a 1 (positive) or 0 (negative).
    
        `sensitivity` should be a floating-point value from 0 to 1
        representing the "true positive rate": the proportion of
        actual positive labels that were accurately identified.
    
        `specificity` should be a floating-point value from 0 to 1
        representing the "true negative rate": the proportion of
        actual negative labels that were accurately identified.
        """

_instance = None

def Ilness1():
    global _instance
    if _instance is None:

        _instance = _Ilness1()

    return _instance


