  
# Random Forest Classifier

# Importing the libraries
import os 
import sys 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from csv import writer 


part_to_number_dict = {
    'High_pressure_pump': 1,
    'Fuel_filter':2,
    'Injectors':3,
    'Fuel_priming_pump':4,
    'Oil_pump':5,
    'Oil_filter':6,
    'Engine_oil':7,
    'Cooling_fan':8,
    'Coolant_pump':9,
    'Radiator':10,
    'Radiator_cap':11,
    'Expansion_tank':12,
    'Thermostat':13,
    'Pistons':14,
    'Connecting_rod':15,
    'Crankshaft':16,
    'Flywheel':17,
    'Engine_block':18,
    'Cylinder_head':19,
    'Valve':20,
    'Valve_drive':21,
    'Camshaft':22,
    'Shaft_drive':23
} 

file_trainings_name = 'Trainings'
file_results_name = 'Result'

# Read Data file
datasets = pd.read_csv(str(os.getcwd()) + '\\Data.csv')

# Importing the datasets   
X = datasets.iloc[:, [2,3]].values
Y = datasets.iloc[:, 4].values


# Read key arguments(name of part which have some trouble)
# Read key arguments(name of part which have some trouble)
part_name = sys.argv[1]

if (part_name != ''):
    print('Start writing to Data file...')
    
    is_work = int(sys.argv[2])
    estimated_wear_percentage = int(sys.argv[3])

    file_trainings_name = str(part_name) + file_trainings_name
    file_results_name = str(part_name) + file_results_name

    # New data  
    List=[len(X) + 1, "Work" if is_work else "Not work", part_to_number_dict[part_name], estimated_wear_percentage, is_work] 
    with open(str(os.getcwd()) + '\\Data.csv', 'a', newline='') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List) 
        f_object.close() 

    print('Row added')
    print(List)

    # Read Data file
    datasets = pd.read_csv(str(os.getcwd()) + '\\Data.csv')

    # Importing the datasets   
    X = datasets.iloc[:, [2,3]].values
    Y = datasets.iloc[:, 4].values





# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_Train = sc_X.fit_transform(X_Train)
X_Test = sc_X.transform(X_Test)

# Fitting the classifier into the Training set

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 200, criterion = 'entropy', random_state = 0)
classifier.fit(X_Train,Y_Train)

# Predicting the test set results

Y_Pred = classifier.predict(X_Test)

# Making the Confusion Matrix 

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_Test, Y_Pred)

# Visualising the Training set results

from matplotlib.colors import ListedColormap
X_Set, Y_Set = X_Train, Y_Train
X1, X2 = np.meshgrid(np.arange(start = X_Set[:, 0].min() - 1, stop = X_Set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_Set[:, 1].min() - 1, stop = X_Set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'yellow')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

Y_Set_tmp = Y_Set[:-1]

for i, j in enumerate(np.unique(Y_Set_tmp)):
    li1 = []
    li2 = []
    for x in range(len(Y_Set_tmp)):
        if (Y_Set_tmp[x] == j):
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])
        else:
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])

    plt.scatter(li1, li2,
            c = ListedColormap(('blue', 'green', 'black'))(j), label = j)

Y_Set_tmp = Y_Set[-1:]
for i, j in enumerate(np.unique(Y_Set_tmp)):
    li1 = []
    li2 = []
    for x in range(len(Y_Set_tmp)):
        if (Y_Set_tmp[x] == j):
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])
        else:
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])

    plt.scatter(li1, li2,
            c = ListedColormap(('blue', 'green', 'black'))(2), label = 666)

plt.title('Random Forest Classifier (Training set)')
plt.xlabel('Agregat')
plt.ylabel('Integrity percentage')
#plt.legend()
plt.savefig( file_trainings_name + '.png')

# Visualising the Test set results

from matplotlib.colors import ListedColormap
X_Set, Y_Set = X_Test, Y_Test
X1, X2 = np.meshgrid(np.arange(start = X_Set[:, 0].min() - 1, stop = X_Set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_Set[:, 1].min() - 1, stop = X_Set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'yellow')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

Y_Set_tmp = Y_Set[:-1]
for i, j in enumerate(np.unique(Y_Set_tmp)):
    li1 = []
    li2 = []
    for x in range(len(Y_Set_tmp)):
        if (Y_Set_tmp[x] == j):
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])
        else:
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])

    plt.scatter(li1, li2,
            c = ListedColormap(('blue', 'green', 'black'))(j), label = j)

Y_Set_tmp = Y_Set[-1:]
for i, j in enumerate(np.unique(Y_Set_tmp)):
    li1 = []
    li2 = []
    for x in range(len(Y_Set_tmp)):
        if (Y_Set_tmp[x] == j):
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])
        else:
            li1.append(X_Set[x, 0])
            li2.append(X_Set[x, 1])

    plt.scatter(li1, li2,
            c = ListedColormap(('blue', 'green', 'black'))(2), label = 666)

plt.title('Random Forest Classifier (Test set)')
plt.xlabel('Agregat')
plt.ylabel('Integrity percentage')
# plt.legend()
plt.savefig(file_results_name + '.png')
