#-----------------------------------------------------------------------------------------------------------------
# Program name: Evolutionary Strategy 
# Author: Yeana Bond
# Date: 05 / 18 / 2021
# Purpose: To implement polynomial regression using evolutionary strategies 
# Note: A better data representation will mutate integers independently, and this is Evolutionary
#     strategies. In (1+1) Evolutionary Strateiges, we have only one parent whose gens - each gene being a vector
#     of loating point numbers - are independent perturbed by normally distributed noise.
# Reference : https://mathworld.wolfram.com/Box-MullerTransformation.html
#-----------------------------------------------------------------------------------------------------------------

import math
import csv
import random
import numpy as np

mu = 0
sigma = 1

def load_data(filename):
    data = []
    try : 
        thisFile = open(filename, 'rb')
    except IOError :
        print( "\n\nError - data.csv does not exist!\n\n" )
    else :
        with open (filename, newline='') as csvfile:
            datum = csv.reader(csvfile)
            
            for row in datum:
                data.append(row)
                
            for i in range(0, len(data)):
                data[i][0] = float(data[i][0])          # convert data value into float by type-casting
                data[i][1] = float(data[i][1])
       
        return data
    
def parent():
    parent = []
    
    for i in range(4):                                  # we need 4 coefficients
        parent.append(random.randrange(-20,20))
    return parent            


def sample_normal_boxmuller(mu, sigma):
    # sample from a normal distribution using Box-Muller method
    # we need two uniform random variables
    u = np.random.uniform(0, 1, 2)

    # Box-Muller formula returns sample from STANDARD normal distribution
    bm = math.cos(2 * np.pi * u[0]) * math.sqrt(-2 * math.log(u[1]))
    return mu + sigma * bm 


def child(parent):
    child = []
    global mu, sigma
    for i in range(4):
        #child.append(parent[i] + random.random())        # uniform random float [0,1)
        child.append(parent[i] + random.gauss(mu,sigma))  # creating a child by adding some normally distributed noise to each coefficient
        
        #### Comment out above and Uncomment below to test boxmuller function ####
        #child.append(parent[i] + sample_normal_boxmuller(mu, sigma))
    return child

def calc_fit(coeff, data):
     
    sse = 0.0
       
    for i in range(len(data)):
        x = data[i][0]
        y_desired = data[i][1]
        y = (coeff[0] * pow(x,3)) + (coeff[1] * pow(x,2)) + \
            (coeff[2] * pow(x,1)) + coeff[3]
        sse += pow(y_desired - y, 2)                    # Fitness is measured by sum-squared error
    return sse

d = load_data("data.csv")
p = parent()
c = child(p)

for i in range(100):
    parent_sse = calc_fit(p, d)
    child_sse = calc_fit(c, d)
    print("\n  ================= Iteration: " + str(i + 1) + " ================= ")
    print("Coefficients from parent: " + str(p[0]) + " " + str(p[1]) + " " + \
          str(p[2]) + " " + str(p[3]))
    print("SSE of parent: " + str(parent_sse))
    print("\nCoefficients from child: " + str(c[0]) + " " + str(c[1]) + " " + \
          str(c[2]) + " " + str(c[3]))
    print("SSE of child:  " + str(child_sse))

    if parent_sse > child_sse:                         # Only if the fitness of the child is better than that of parent, the child replaces the parent
        p.clear()
        p = c
    c = child(p)
    

input("\n Run complete. Press the Enter key to exit.")



        

