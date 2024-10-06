# Opprett en klassifikator
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Last inn datasettet
cancer = load_breast_cancer()

# Navn på trekk og målklasser
print("Navn på trekk:", cancer.feature_names)
print("Målklasser:", cancer.target_names)

# Dimensjonene på dataene
print("Dimensjoner på dataene:", cancer.data.shape)


# Splitt dataene opp i treningssett og testsett
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=42)

# Dimensjonene til trenings- og testsett
print("Dimensjoner på treningssett:", x_train.shape)
print("Dimensjoner på testsett:", x_test.shape)

# Opprett en klassifikator
classifier = LogisticRegression(max_iter=5000)

# Tren klassifikatoren med treningsdataene
classifier.fit(x_train, y_train)

# Gjør klassifiseringer med testsettet
y_pred = classifier.predict(x_test)

# Regn ut nøyaktigheten til klassifikatoren
accuracy = accuracy_score(y_test, y_pred)

print(f"Modellens nøyaktighet: {accuracy:.2f}")

print("Klassifikasjonsrapport:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))
