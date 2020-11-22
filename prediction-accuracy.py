import pandas as pd
from model import read

def accuracy_of_model(n):
    sample_data = pd.read_csv('data/insurance.csv')
    sum = 0

    #print(sample_data)

    for i in sample_data.head(n).itertuples():
        sex = i[2]
        smoker = i[5]
        location = i[6]
        age = i[1]
        bmi = i[3]
        kids = i[4]
        expenses = float(i[7])
        #print(sex, smoker, location, age, bmi, kids)
        predicted = float(read(sex, smoker, location, age, bmi, kids))
        accuracy = abs(predicted - expenses) / expenses
        sum += accuracy
        print(accuracy)
        #print(predicted)
    avg_accuracy = 100 - (sum / n)
    print(avg_accuracy)
    return avg_accuracy
accuracy_of_model(50)
