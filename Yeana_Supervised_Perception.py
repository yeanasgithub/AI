
#----------------------------------------------------------------------------------------------------------------
# Program name: Perceptron algorithm
# Author: Yeana Bond
# Date: 04/26/2021
# Purpose: To implement a perceptron algorithm on a simplified version of Fisher's Iris Dataset
# Perceptron is a supervised learning algorithm:
# The dataset contains samples, and each sample consists of a 2-tuple. The x vector is an observation
# that has measurements for a sample and Yd is the correct decision, which is also called label or ground truth.
# The x vector must be a vector of numbers of the same length for all samples, though it is possible
# to have other types ( such as categories )  and/or missing values in reality that lead us to handle exceptions.
# One epoch : each time you feed the entire dataset to the machine learning algorithm
# Training : the phase where you feed a sample to the algorithm. Then, algorithm adjusts the model
#           if there is an error.
# Accuracy = number of correct cases / number of samples in the dataset
#----------------------------------------------------------------------------------------------------------------


import csv
from random import seed
from random import random
seed(1) # Seed random number generator


weight_set = [random() for i in range(4)]
print("\nRandom weight values to start: ", weight_set)

learning_rate = 0.1

def load_data_and_convert_to_float(filename):
    data_set = []
    try : 
        thisFile = open(filename, 'rb')
    except IOError :
        print( "\n\nError - iris.csv does not exist!\n\n" )
    else :
        with open (filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
        
    data_category = data[0]       # first row contains the name of the variables of the data set
    print("\nNominal variables of the data set: ", data_category)
    for row in range(1, len(data)):
        data_set.append(data[row])

    # convert datt to float by using type-casting    
    for i in range(0, len(data_set)):
        sL, sW, pL, pW, spec = data_set[i]
        for j in range(len(data_set[i])):
            data_set[i][j] = float(data_set[i][j])      # data_set is a 2-D array
    return data_set


def perform_epoch(filename):
    
    error = 0.0
    theta = 0.0
    
    data = load_data_and_convert_to_float(filename)
    
    epoch_num = 1    
    for epoch in range(100):
        tally = 0  # tally and count_correct_case should be reset to zero after one each epoch
        count_correct_case = 0
        for row in data:
            y_desired = row[4]  # yd in each row of the sample
         
            x = row[:4]  # feature vectors in each row of the sample
            charge = 0.0
        
            for weight, feature_vector in zip(weight_set, x):   # zip the two sets and re-form it as an iteratable 2-tuple to pair up
                charge = charge + (weight * feature_vector)
            charge = charge - theta

            if charge > 0:    
                y_guessed = 1      # sign function is applied as the activation function
            else:
                y_guessed = -1

            error = y_desired - y_guessed
            
            if abs(error) > 0:
                for weight, feature_vector in zip(weight_set, x):
                    weight = weight - (learning_rate * feature_vector * error)
                    #print(weight)
                theta = theta - (learning_rate * error)
            else:
                count_correct_case += 1   # if error is zero, that means the y_guessed value was the same with y_desired

            tally += 1  # to keap track of the total number of samples
            #print(tally)  # tally should be 150 per each epoch
            
    
        accuracy = count_correct_case / tally
          
        
        format_accuracy(accuracy, epoch_num)
        epoch_num += 1
   
def format_accuracy(accuracy, epoch_num):

    #print(accuracy)
    
    accuracy_percent = round(accuracy, 4)
    print("\nAccuracy percentage after epoch " + str(epoch_num) + ": " +  str(accuracy_percent * 100) + "%" + "\n")
     



## This is Pre-lab practice functions                       
##def print_5th_column():
##    data_set = load_data()
##    species = []
##    petal_width = []
##    predicted_spec = 1
##    predicted_s = []
##    for i in range(0, len(data_set)):
##        sL, sW, pL, pW, spec = data_set[i]
##        species.append(float(spec))  # cast the input as a float
##        petal_width.append(float(pW))
##
##        if petal_width[i] > 0:
##            predicted_spec = -1  # -1 means it is not Iris Virginica
##            #predicted_s.append(predicted_spec)
##        else:
##            predicted_spec = 1
##
##        predicted_s.append(predicted_spec)
##    #print("petal width: ", petal_width)
##
##    #print("predicted spec: ", predicted_s)
##    return petal_width, species, predicted_s
##
##
#### accuracy is correct decisions / num of samples
##def calc_accuracy():
##    petal_width, species, predicted_s = print_5th_column()
##    count = 0.0
##    percent_val = 0
##    accuracy = 0
##    if len(species) == len(predicted_s):
##        for i in range(len(species)):
##        
##            if species[i] == predicted_s[i]:
##                count = count + 1
##            else:
##                count = count
##    percent_val = count / len(species)
##    accuracy = ('%.2f' % percent_val).rstrip('.')
##    print(str(accuracy) + "%")
## End of Pre-lab   

def main():
                
    filename = "iris.csv" 
    perform_epoch(filename)
    input("\nRun complete. Press the Enter key to exit.")
    
main()
##print_5th_column()
##calc_accuracy()
        
    


