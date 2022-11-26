#----------------------------------------------------------------------------------------------------------------
# Program name: Introduction to backward chaining and python3 functions
# Author: Yeana Bond
# Date: 02/23/2021
# Purpose: To understand a lower level implementation to solve logic problems using PL backward chaining
#----------------------------------------------------------------------------------------------------------------


# DB  =  ["looks","swims","quacks"]  #  A  set  of  facts
agenda = ["barks", "hoots", "looks", "swims", "quacks"]
KB = [(["looks","swims","quacks"],"duck"),(["barks"],"dog"), (["hoots","flies"],"owl")] # A set of rules

q = "duck" # our goal
count = [3, 1 ,2] # count per rule 
                # rule 0 = count[0], rule 1 = count[1], rule 2 = count[2]

inferred =[] # declaring an empty set

while agenda:
    # changes = False # Set the flag that there have been no changes to false
    
    p = agenda.pop(0)
    if p == q:
        print( "Goal is entailed!" )
        break
    if p not in inferred:
        inferred.append( p )

        for i in range(0, len(KB)):
            premise, consequent = KB[i]
            print( "\nConsider a rule where: " )
            print( premise )
            print( "implies: " )
            print( consequent )

            if p in premise:
                count[i] -= 1 # decrement count[i]
                print(" ", i, " " + p )
                
                if count[i] == 0:
                    agenda.append( consequent )

##------------------------------------------------------
## below is not erased out to compare the length of the code of the first coding lab with the second lab

        # Determine if all literals in antecedent are also in KB
##        satisfied = True # Flag for entire premise being satisfied
 
##        for q in antecedent:
            # q will be string
            # KB is a list of strings
##            if q not in DB:
##                satisfied = False
                # Flag as false, all clauses must be inferred
                
	# If it passes the above, then antecedent is satisfied
	# ...and consequent should be entailed
##        if satisfied and consequent not in DB:
##            DB.append ( consequent )
##            changes = True
##            print( "Antecedent is in DB, consequent is implied, DB is now: " )
##        elif satisfied and consequent in DB:
##            print( "Consequent is implied, but was already in DB" )
##        else:
##            print( "Consequent is not implied" )

##    count = count + 1
#----------------------------------------------------------
print("\nNo more counts. inferred is now: ")
print( inferred )
   
print("\nagenda is now: ")
print( agenda )

