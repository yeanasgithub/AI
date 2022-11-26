# Case #2 with Collision
#----------------------------------------------------------------------------------------------------------------
# Program name: Fifth coding lab - Calculating certainty factors with efficient forward chaining
# Author: Yeana Bond
# Date: 03/30/2021
# Purpose: Implement to obtain certainty factors with or without dealing with collisions
# Note 1: Where a collision can occur varies. It can occur within KB, which this code shows with the first set of
#       FACTS and KB. It can occur between KB and FACTS, which this code demonstrates with the second set of
#       FACTS and KB. The last set of KB and FACTS do not have any collisions,
#       which is the case this code also works perfectly in.
#       No matter where a collision occurs, it comes down to comparing inferred with DB.
#       inferred is for existing CF, and DB is for the most recently-inferred CF. Both CF values are used to
#       calculate final CF after one time of collision.
# Node 2: Because dict in Python do not allow duplicates, after calculating for collisions, tuples will be
#        converted into dictionary format.
#-------------------------------------------------------------------------------------------------------------

## Uncomment to test sets with collisons

##First Set of FACTS and KB
##FACTS = [["A", 1.0], 
##["B", -0.70], 
##["C", 0.75], 
##["D", 0.8], 
##["E", 0.50], 
##["M", -1.0]]
##
##
##
##KB = [[["Y", "D"], "Z", 0.70], 
##[["A", "B", "E"], "Y", 0.95], 
##[["A"], "X", 1.0], 
##[["C"], "L", 0.85], 
##[["L", "M"], "N", 1.0],
##[["B"], "Z", -0.8]]
count = [2, 3, 1, 1, 2, 1] ## count is same for first and second set
##Second Set of FACTS and KB 
FACTS = [["A", 1.0], 
["B", 0.70], 
["C", -0.75],  # for testing collision
["D", 0.8], 
["E", 0.50], 
["M", -1.0]]

KB = [[["Y", "D"], "Z", 0.70], 
[["A", "B", "E"], "Y", 0.95], 
[["A"], "X", 1.0], 
[["C"], "L", 0.85], 
[["L", "M"], "N", 1.0],
[["C"], "M", 0.2]] # new rule for testing collision

##Third set of FACTS and KB
##FACTS = [["A", 1.0], 
##["B", 0.70], 
##["C", 0.75],  
##["D", 0.8], 
##["E", 0.50], 
##["M", -1.0]]
##
##count = [2, 3, 1, 1, 2]
##
##KB = [[["Y", "D"], "Z", 0.70], 
##[["A", "B", "E"], "Y", 0.95], 
##[["A"], "X", 1.0], 
##[["C"], "L", 0.85], 
##[["L", "M"], "N", 1.0]]



inferred = []
DB = []

def certainty_factor(KB, FACTS):
    while FACTS:
        popped_facts = FACTS.pop(0)
        lit_from_facts, val_from_facts = popped_facts
        
        # DB collects what is poped from FACTS
        # DB is where collision is dealt in
        DB.append(popped_facts)
  
        for i in range(0, len(KB)):
            antecedent, consequent, cf_KB = KB[i]
            if lit_from_facts in antecedent:
                print(antecedent)
                count[i] -= 1
                
                # By replacing the literals to values, it becomes convinient
                # to get mininum of antecedent literals
                antecedent.remove(lit_from_facts)
                antecedent.append(val_from_facts)

                if count[i] == 0:
                    product_of_cfs = cf_KB * min(antecedent)
                    newfact = [consequent, product_of_cfs]
                    FACTS.append(newfact)

                    # inferred acts like an assistant for DB to keep history records of CF values
                    # So, newfact itself will be added to inferred since product_of_cfs is what makes newfact different
                    # even if there is a same consequent member in inferred
                    if newfact not in inferred:
                        inferred.append(newfact)
                 

                            
    print("inferred now: ", inferred)
    print("\nDB now: ", DB)
    for j in range(0, len(inferred)):
        lit_ifd, val_ifd = inferred[j]
        for k in range(1, len(DB)):
            lit, val_existing = DB[k]
            if lit_ifd == lit and val_ifd != val_existing:
       
                        
                print("Collision ", DB[k])
                print(k, j)
                if val_ifd >= 0 and val_existing >= 0:
                    print(" \n In first if condition" )
                    new  = val_existing + val_ifd*(1 - val_existing)

                if val_ifd < 0 and val_existing < 0:
                    print(" \n In second if condition" )
                    new  = val_existing + val_ifd * (1 + val_existing)
                    
                if (val_ifd < 0 and val_existing >= 0) or (val_ifd >= 0 and val_existing < 0):
                    print(" \n In third if condition" )
                    new  = (val_existing + val_ifd) / (1 - min(abs(val_existing), abs(val_ifd)) )

                print("New Value ", new)
                DB[k].remove(val_existing)
                DB[k].append(new)
              
                # Before converting DB to dict format, where literlas are the same, new value replaces
                # the old value, val_DB
                for h in range(0, len(DB)):
                    lit_DB, val_DB = DB[h]
                    if lit_ifd == lit_DB and new!= val_DB:
                        DB[h].remove(val_DB)
                        DB[h].append(new)
            
                         
                

                
    print("\nDB before transformed to dict: ", DB)
    s = dict(DB)
    print("\n\nFINAL DB in dictionary form:")
    
    print(s)



certainty_factor(KB, FACTS)
input("\nRun complete. Press the Enter key to exit.")
