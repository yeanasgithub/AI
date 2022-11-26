#-----------------------------------------------------------------------------------------------------------------
# Program name: Neural Network
# Author: Yeana Bond
# Date: 05/09/2021
# Purpose: To implement a multi-layer neural network which contains a single hidden layer with three hidden layer
#         neurons and an outputlayer with three output neurons using the iris.csv.
# MAD: Mean Absolute Deviation means average error of each sample for the entire epoch. Thus, sume of magnitude
#    of difference in y_desired and y_guessed of each sample per epoch divded by the number of samples in epoch
#    In this lab's data set, "row" indicates the number of samples. In other words, the length of data set is
#    the number of rows that translates to the number of samples. 
# Note: The class, prepare_Epoch_and_Backpropagation contains values which are not going to change while the
#     class, one_Neuron deals with values which are going to change per instance object which represents a neuron.
# Check-off: Demonstrate MAD value decreases from epoch to epoch. It is expected that an accuracy close to 100%
#           can be acheived with the Iris data set.
#-----------------------------------------------------------------------------------------------------------------

import csv
import math
from random import random

learning_rate = 0.1
data_set = []

def load_data_and_convert_to_float(filename):
    
    try : 
        thisFile = open(filename, 'rb')
    except IOError :
        print( "\n\nError - iris.csv does not exist!\n\n" )
    else :
        with open (filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
        
    data_category = data[0]       # first row contains the name of the variables of the data set
    #print("\nNominal variables of the data set: ", data_category)
    for row in range(1, len(data)):
        data_set.append(data[row])
    

    # convert data to float by using type-casting    
    for i in range(0, len(data_set)):
        sL, sW, pL, pW, spec1, spec2, spec3 = data_set[i]
        for j in range(len(data_set[i])):
            data_set[i][j] = float(data_set[i][j])      # data_set is a 2-D array
    return (data_set)


class prepare_Epoch_and_Backpropagation:
    def __init__(self):
        
  
        self.data_set = load_data_and_convert_to_float("iris.csv")
        self.data_set_size = len(self.data_set)
        self.x = []
        self.y_desired_set = []
        for i in range(self.data_set_size):
            self.x.append(self.data_set[i][:4])

    def get_data_set(self):
        return self.data_set

    def get_data_set_size(self):
        return self.data_set_size
    
    def get_y_desired_from_data_set(self):
        for i in range(self.data_set_size):
            self.y_desired_set.append(self.data_set[i][4:7])
            
        return self.y_desired_set
        

class one_Neuron(prepare_Epoch_and_Backpropagation):
    def __init__(self, number_of_incomings):
        
        prepare_Epoch_and_Backpropagation.__init__(self)
        self.whole_data = self.data_set # inherited
        self.feature_vectors = self.x   # inherited
        self.num_weights = number_of_incomings
        self.weights = [random() for i in range(self.num_weights)] # number of incomings varies per neuron, so is number of weights 
        self.theta = random()


    def sigmoid(self, value):
        return 1 / (1 + (math.exp(-value))) # Sigmoid function
    

    def feed_forward_to_hidden(self, row):
                
        charge = 0
        #print(self.feature_vectors) # to test class inheritance 

        for feature_vector, weight in zip(self.feature_vectors[row], self.weights):
            charge += feature_vector * weight
        
        self.y = self.sigmoid(charge - self.theta)
        
            
    def feed_forward_to_output(self, y_from_hidden):
        charge = 0
        for y_value_from_hidden, weight in zip(y_from_hidden, self.weights):
            charge += y_value_from_hidden * weight
        self.y = self.sigmoid(charge - self.theta)
  

    def calc_delta_of_output_neurons(self, row, column, y_from_hidden):
        
        y_desired = self.whole_data[row][column]
        self.delta = self.y * (1 - self.y) * (y_desired - self.y)

        if self.delta != 0:
            self.train_weights(y_from_hidden, self.delta)


    def calc_delta_of_hidden_neurons(self, row, sum_of_delta_X_weight):
        self.delta = self.y * (1 - self.y) * sum_of_delta_X_weight
        
        if self.delta != 0:
            self.train_weights(self.feature_vectors[row], self.delta)
            
    def train_weights(self, incomings, delta):
        for weight, ins in zip(self.weights, incomings):
            weight = weight + (learning_rate * ins * delta)
        self.theta = self.theta - (learning_rate * delta)


        
def main():

    start = prepare_Epoch_and_Backpropagation()
    y_desired = start.get_y_desired_from_data_set()
    num_rows_in_data_set = start.get_data_set_size()
    #print(num_rows_in_data_set)

    # number of incomings toward each neuron is parameterized
    hidden_0 = one_Neuron(4)
    hidden_1 = one_Neuron(4)
    hidden_2 = one_Neuron(4)
    output_0 = one_Neuron(3)
    output_1 = one_Neuron(3)
    output_2 = one_Neuron(3)

   
    temp = 0.0
    for epoch in range(0, 30):
        total_magnitude_deviation = 0.0
        mean = 0.0
        
        for row in range(num_rows_in_data_set):
            
            hidden_0.feed_forward_to_hidden(row)
            hidden_1.feed_forward_to_hidden(row)
            hidden_2.feed_forward_to_hidden(row)

            # each hidden neuron's y value is passed for feed-foward toward output layer

            hidden_y0_y1_y2 = [hidden_0.y, hidden_1.y, hidden_2.y]
            

            output_0.feed_forward_to_output(hidden_y0_y1_y2)
            output_1.feed_forward_to_output(hidden_y0_y1_y2)
            output_2.feed_forward_to_output(hidden_y0_y1_y2)

            # 4, 5, and 6 in the parameter mean the column for each location of y_desired per output

            output_0.calc_delta_of_output_neurons(row, 4, hidden_y0_y1_y2)
            output_1.calc_delta_of_output_neurons(row, 5, hidden_y0_y1_y2)
            output_2.calc_delta_of_output_neurons(row, 6, hidden_y0_y1_y2)

            # Step 3 (b): weight training p.180,  Negnevitsky's

            sum_of_delta_X_weight_0 = output_0.delta * output_0.weights[0] +  \
                                      output_1.delta * output_1.weights[0] +  \
                                      output_2.delta * output_2.weights[0]
            
            sum_of_delta_X_weight_1 = output_0.delta * output_0.weights[1] +  \
                                      output_1.delta * output_1.weights[1] +  \
                                      output_2.delta * output_2.weights[1]

            sum_of_delta_X_weight_2 = output_0.delta * output_0.weights[2] +  \
                                      output_1.delta * output_1.weights[2] +  \
                                      output_2.delta * output_2.weights[2]
            

            hidden_0.calc_delta_of_hidden_neurons(row, sum_of_delta_X_weight_0) 
            hidden_1.calc_delta_of_hidden_neurons(row, sum_of_delta_X_weight_1)
            hidden_2.calc_delta_of_hidden_neurons(row, sum_of_delta_X_weight_2)

            
            y_desired_per_row = y_desired[row]
            
            # formatting values to the 2-decimal places as shown in the lab manual's mock outputs
            y_guessed = [float("{:.2f}".format(output_0.y)), float("{:.2f}".format(output_1.y)), float("{:.2f}".format(output_2.y))]

            for y_d, y_g in zip(y_desired_per_row, y_guessed):
                total_magnitude_deviation += abs(y_d  - y_g)

            # comment below NOT to see the prediction values per sample within the each epoch
            print("Epoch ", epoch + 1, " Iteration: ", row + 1, " Prediction is ", y_guessed)
        
        mean = total_magnitude_deviation / num_rows_in_data_set

            
        print("Epoch ", epoch + 1, " Result: MAD = ", mean)
        trend = float("{:.8f}".format(temp - mean))
        
        temp = mean

        # I noticed that the total magnitude can increase after a certain number of epochs,
        # especially when line #198 is commented out.
        # Thus, I made this if-block. Please, comment the block if you do not desire to detect
        # where the trend of MAD changes. The change of the trend may be temporary, and I
        # do not know how significantly this change indicates anything in a simulation.
        
        # if previous mean, temp is smaller than the current mean, stop epoch automatically
        # once the trend change occurs.
        
        if trend < 0 and epoch > 1:
            print("The trend of MAD change per epoch detected!")
            break
            
   


main()
print("\n(Un)/comment line #198 to see the (detail)/fewer outputs.")
input("\n Run complete. Press the Enter key to exit.")











