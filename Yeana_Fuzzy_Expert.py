
#----------------------------------------------------------------------------------------------------------------
# Program name: From Fuzzy set problem set-up to rule application
# Author: Yeana Bond
# Date: 04/06/2021
# Purpose: To understand fuzzy set theory and monotonic inference,
#          To implement fuzzy set connectives
# Fuzzy variables: variables in a fuzzy expert system ( = liguistic variables)
# Fuzzy values: in each fuzzy variable, there are more than one fuzzy values ( = liguistic values)
#-------------------------------------------------------------------------------------------------------------
print("Task 1: Problem Set-up")
# amount of water variables in Liters
none_water = [[1.0, 0.0], [0.75, 0.1], [0.50, 0.20], [0.25, 0.30], [0.0, 0.40]]
bottle_water = [[0.0, 0.2], [0.5, 0.5], [1.0, 1.0], [0.5, 1.5], [0.0, 2.0]]
a_Lot_water = [[0.0, 1.0], [0.25, 1.25], [0.5, 1.5], [0.75, 1.75], [1.0, 2.0]]

# temperature variables in Fahrenheight
moderate_temp = [[0.0, 40], [0.5, 50], [1.0, 60], [1.0, 70], [1.0, 75]]
hot_temp = [[0.0, 40], [0.0, 50], [0.0, 60], [0.0, 70], [0.5, 75], [1.0, 80]]

# distance(travel) variables in Kilo-meters

short_dist = [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]]
medium_dist = [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0], [0.5, 1.5], [0.0, 2.0]]
long_dist = [[0.0, 1.0], [0.5, 2.0], [0.75, 3.0], [1.0, 4.0]]

print("none_water: ", none_water, " --- half-triagle shape\n")
print("bottle_water: ", bottle_water, " --- full-triagle\n")
print("a_Lot_water: ", a_Lot_water, " --- trapezoid\n")
print("moderate_temp: ", moderate_temp, " --- trapezoid\n")
print("hot_temp: ", hot_temp, " --- trapezoid\n")
print("short_dist: ", short_dist, " --- half-triangle\n")
print("medium_dist: ", medium_dist, " --- full-triagle\n")
print("long_dist: ", long_dist, " --- trapezoid\n")

# Task 2: Implementation of Fuzzy Membership


def calc_dist(a, fuzzySet):
    
    min_ds = []
    for i in range(0, len(fuzzySet)):
        ds = abs(a - fuzzySet[i][1])    
        min_ds.append(ds)
        
    index_ds = min_ds.index(min(min_ds))

    return index_ds
    min_ds.clear()

def match_for_inverse(b, fSet):
    min_ds_inverse_mem = []
    for i in range(0, len(fSet)):
        dst = abs(b - fSet[i][0])
        min_ds_inverse_mem.append(dst)
        
    index_dst =  min_ds_inverse_mem.index(min(min_ds_inverse_mem))
    #print("match fn ", index_dst)
    return index_dst
    min_ds_inverse_mem.clear()

def inverseMembership(inputVal, fSet):
    for q in fSet:
        fuzzyVal, crisp = q
        if fuzzyVal == inputVal:
            return crisp
        else:
            updated_idx = match_for_inverse(inputVal, fSet)
            nearest_fuzzy_val = fSet[updated_idx][1]
            return nearest_fuzzy_val
        

def membership(inputVal, fuzzySet):
    for p in fuzzySet:
        fuzzyVal, crisp = p
        if crisp == inputVal:
            return fuzzyVal
        # if the inputVal is not identical with values in the set
        # you have to get the nearest value
        # iterate over each 2-tuple noting the distance in calc_dist function
        else:
            updated_index = calc_dist(inputVal, fuzzySet)
            nearest_crisp_val = fuzzySet[updated_index][0]
            return nearest_crisp_val
            

print("\nTest with value, 1.3")    
print(membership(1.3, bottle_water))
print("\nTask 2 - Printing membership function test results")   
print(membership(-3,bottle_water))
print(membership(1.0,bottle_water))
print(membership(0.3,bottle_water))
print(membership(0.712321345,bottle_water))
print(membership(10000,bottle_water))

print("\nTask 3 - Printing inverseMembership function test results")
print(inverseMembership(0.0,bottle_water))
print(inverseMembership(0.2,bottle_water))
print(inverseMembership(0.5,bottle_water))
print(inverseMembership(0.8,bottle_water))
print(inverseMembership(1.0,bottle_water))

# Task 4: Your rules must have only ONE output value as the consequent.
# You may use any combination of input values using either conjunctions or disjunctions
# in the premise
#Driver Code for Task 4
print("\nTask 4 - Printing all rules and recommendations")

# For the disjuction (or), max() function can be used
# for the conjuction (and), min() can be used


# Rule 1: If distance, short, OR temperature is moderate, Then water is bottle
# The user is traveling 0.4km and it is 62F
km = 0.4
temp = 62
fuzzyDistance = membership(km, short_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)

print("--------------------  Variable : short(dist), moderate(temp)   -------------------")
print("\n 1 - Rule 1 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")



# Rule 2: If distance, short, AND temperature is moderate, Then water is none
# The user is traveling 1km and it is 60F
km = 0.4
temp = 60
fuzzyDistance = membership(km, short_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, none_water)
print("\n 2 - Rule 2 testing result - conjuntion")
print( "The user walked " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.\n\n\n" )









# Rule 3: If distance, long, OR temperature is hot, Then water is a lot
# The user is traveling 3km and it is 78F

km = 3.0
temp = 78
fuzzyDistance = membership(km, long_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, a_Lot_water)
print("--------------------  Variable : long(dist), hot(temp)   -------------------")
print("\n 3 - Rule 3 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle water to bring." )



# Rule 4: If distance, long, AND temperature is hot, Then water is a lot
# The user is traveling 7km and it is 91F
km = 7.0
temp = 91
fuzzyDistance = membership(km, long_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, a_Lot_water)
print("\n 4 - Rule 4 testing result - conjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.\n\n\n")








# Rule 5: If distance, medium, OR temperature is hot, Then water is a lot
# The user is traveling 1.9km and it is 100F
km = 1.4
temp = 100
fuzzyDistance = membership(km, long_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, a_Lot_water)
print("--------------------  Variable : medium(dist), hot(temp)   -------------------")
print("\n 5 - Rule 5 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")

# Rule 6: If distance, medium, AND temperature is hot, Then water is bottle   
# The user is traveling 1.6km and it is 100F
km = 1.6
temp = 100
fuzzyDistance = membership(km, medium_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)
print("\n 6 - Rule 6 testing result - conjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.\n\n\n")








# Rule 7: If distance, medium, OR temperature is moderate, Then water is bottle
# The user is traveling 7km and it is 44F
km = 0.76
temp = 49
fuzzyDistance = membership(km, medium_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)
print("--------------------  Variable : medium(dist), moderate(temp)   -------------------")
print("\n 7 - Rule 7 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")



# Rule 8: If distance, medium, AND temperature is moderate, Then water is bottle ---------
# The user is traveling 1.3km and it is 55F

km = 1.3
temp = 55
fuzzyDistance = membership(km, medium_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)
print("\n 8 - Rule 8 testing result - conjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.\n\n\n" )








# Rule 9: If distance, short, OR temperature is hot, Then water is bottle
# The user is traveling 0.3km and it is 88F
km = 0.3
temp = 88
fuzzyDistance = membership(km, short_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)
print("--------------------  Variable : short(dist), hot(temp)   -------------------")
print("\n 9 - Rule 9 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")



# Rule 10: If distance, short, AND temperature is hot, Then water is none
# The user is traveling 0.3km and it is 88F
km = 0.3
temp = 88
fuzzyDistance = membership(km, short_dist)
fuzzyTemp = membership(temp, hot_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, none_water)
print("\n 10 - Rule 10 testing result - conjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.\n\n\n")









# Rule 11: If distance, long, OR temperature is moderate, Then water is a lot
# The user is traveling 7km and it is 40F
km = 7.0
temp = 40
fuzzyDistance = membership(km, long_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, a_Lot_water)
print("--------------------  Variable : long(dist), moderate(temp)   -------------------")
print("\n 11 - Rule 11 testing result - disjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")




# Rule 12: If distance, long, AND temperature is moderate, Then water is bottle
# The user is traveling 3.75km and it is 40F
km = 3.75
temp = 40
fuzzyDistance = membership(km, long_dist)
fuzzyTemp = membership(temp, moderate_temp)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle_water)
print("\n 12 - Rule 12 testing result - conjunction")
print( "The user is going to " + str(km) + "km, and it is " + str(temp) +
       "F. \n Fuzzy system recommends " + str(crispOutput) + " liters of bottle of water to bring.")




input("\nRun complete. Press the Enter key to exit.")







