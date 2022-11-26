#----------------------------------------------------------------------------------------------------------------
# Program name: Media Advisor
# Author: Yeana Bond
# Date: 03/09/2021
# Purpose: Using Forward Chaining and/or Backward Chaining to carry out inference, implement Media Advisor 
#----------------------------------------------------------------------------------------------------------------


# Rules in stimulus situation  ([environment], stim_stuation)
ss_rule = [(["papers","manuals","documents","textbooks"], "verbal"),
             (["pictures","illustrations","photographs","diagrams"], "visual"),
             (["machines","buildings","tools"], "physical object"),
             (["numbers","formulas","computer programs"], "symbolic")]
 
    
# Rules in stimulus response  ([job], stim_resp)
    
sr_rule = [(["lecturing","advising","counselling"], "oral"),
             (["building","repairing","troubleshooting"], "hands-on"),
             (["writing","typing","drawing"], "documented"),
             (["evaluating","reasoning","investigating"], "analytical")]

# Rules in feedback ([feedback], response)
fb_rule = [(["yes"], "yes"),
           (["no"], "no")]

# Rules in Medium ([stim_sit, stim_resp, feedback], medium)
    
m_rule = [(["physical object","hands-on","yes" ], "workshop"),
            (["symbolic","analytical","yes"], "lecture-tutorial"),
            (["visual","documented","no"], "videocassette"),
            (["visual","oral","yes"], "lecture-tutorial"),
            (["verbal","analytical","yes"], "lecture-tutorial"),
            (["verbal","oral","yes"], "role-play exercises")]


def main():
   
    goal = "workshop"

    print( "\n------- Case # 01 --------" )

    print( "Press, 9, 5, 1 to test this case." )
    display_environment_option()
    environ = input("\nChoose one option: ")
    environment = convert_environ_to_string(environ)
    display_job_option()
    j = input("\nChoose one option: ")
    job = convert_j_to_string(j)
    display_feedback_option()
    fb = input("\nChoose one option: ")
    feedback = convert_fb_to_string(fb)

    medium_backward_chaining(goal, environment, job, feedback)

    goal = "lecture-tutorial"
    
    print( "\n------- Case # 02 --------" )

    print( "Press, 1, 10, 1 to test this case." )
    display_environment_option()
    environ = input("\nChoose one option: ")
    environment = convert_environ_to_string(environ)
    display_job_option()
    j = input("\nChoose one option: ")
    job = convert_j_to_string(j)
    display_feedback_option()
    fb = input("\nChoose one option: ")
    feedback = convert_fb_to_string(fb)

    medium_backward_chaining(goal, environment, job, feedback)

def medium_backward_chaining(goal, environment, job, feedback):
    print( "\n Calling Propositional Logic Backward Chainig fucntion with ", '"', goal, '"'" as goal", sep='')
     
    medium_ante = []
    conseq = []

    # Medium Rules are investigated first and antecedents of a found goal are stored in medium_ante[]

    for i in range(0, len(m_rule)):
        antecedent_m_rule, consequent_m_rule = m_rule[i]
        if goal in consequent_m_rule:
            print( " Found a goal, ", '"', goal, '"', " as a consequent." )
            for literal_m in antecedent_m_rule: 
                print(literal_m) 
                medium_ante.append(literal_m)
          
    # user's answer for environment is compared with literals in stimulus situation (ss_rule) of antecedents
    
    for i in range(0, len(ss_rule)):
        antecedent_ss_rule, consequent_ss_rule = ss_rule[i]
        if environment in antecedent_ss_rule:
            for literal_ss in antecedent_ss_rule:
                if literal_ss == environment:
                    print( " Found ", environment, " in ", consequent_ss_rule )
                    conseq.append(consequent_ss_rule) # Matched literal is appended to conseq[]
            
    # user's answer for job is compared with literals in stimulus response (sr_rule) of antecedents
    
    for i in range(0, len(sr_rule)):
        antecedent_sr_rule, consequent_sr_rule = sr_rule[i]
        if job in antecedent_sr_rule:
            for literal_sr in antecedent_sr_rule:
                if literal_sr == job:
                    print( " Found ", job, " in ", consequent_sr_rule )
                    conseq.append(consequent_sr_rule) # Matched literal is appended to conseq[]
                    
    # user's answer for feedback is compared with literals in feedback (fb_rule) of antecedents
                    
    for i in range(0, len(fb_rule)):
        antecedent_fb_rule, consequent_fb_rule = fb_rule[i]
        if feedback in antecedent_fb_rule:
            for literal_fb in antecedent_fb_rule:
                if literal_fb == feedback:
                    print( " Found ", feedback, " in ", consequent_fb_rule )
                    conseq.append(consequent_fb_rule) # Matched literal is appended to conseq[]

    print( "\n-----Conclusion-----Conclusion-----Conclusion-----Conclusion-----" )
    print( " Final medium_ante list ", medium_ante )
    print( conseq )

    # If final medium_ante[] has an item matching with an every item of conseq[],
    # goal is the medium
    # Otherwise, it is impossible to conclude
    
    if conseq[0] in medium_ante and conseq[1] in medium_ante and conseq[2] in medium_ante:
        print( "\nMedium is ", goal )
        
    else:
        print( "\nI am unable to draw any conclusions on the basis of the data." )
        
    conseq.clear()
    medium_ante.clear()
    

def display_environment_option():
     print( "\n Q1. What sort of environment is a trainee dealing with on the job?" )
     
     print( " 1 = papers" )
     print( " 2 = manuals" )
     print( " 3 = documents" )
     print( " 4 = textbooks" )
     print( " 5 = pictures" )
     print( " 6 = illustrations" )
     print( " 7 = photographs" )
     print( " 8 = diagrams" )
     print( " 9 = machines" )
     print( " 10 = buildings" )
     print( " 11 = tools" )
     print( " 12 = numbers" )
     print( " 13 = formulas" )
     print( " 14 = computer programs" )

def convert_environ_to_string(ss_answer):

     stimulus_situations = { '1': "papers", '2':"manuals", '3': "documents", '4': "textbooks",
                             '5':"pictures", '6':"illustrations", '7':"photographs", '8':"diagrams",'9': "machines",
                             '10':"buildings", '11':"tools", '12':"numbers", "13":"formulas",'14':"computer programs" }
     
     return stimulus_situations.get(ss_answer)

 

def display_job_option():
     print( "\n Q2. In what way is a trainee expected to act or respond on the job?" )
     
     print( " 1 = lecturing" )
     print( " 2 = advising" )
     print( " 3 = counselling" )
     print( " 4 = building" )
     print( " 5 = repairing" )
     print( " 6 = troubleshooting" )
     print( " 7 = writing" )
     print( " 8 = typing" )
     print( " 9 = drawing" )
     print( " 10 = evaluating" )
     print( " 11 = reasoning" )
     print( " 12 = investigating" )

def convert_j_to_string(sr_answer):

     stimulus_responses = { '1': "lecturing", '2':"advising", '3': "counselling", '4': "building",
                            '5':"repairing", '6':"troubleshooting", '7':"writing", '8':"typing",'9': "drawing",
                            '10':"evaluating", '11':"reasoning", '12':"investigating" }
     
     
     return stimulus_responses.get(sr_answer)


def display_feedback_option():
     print( "\n Q3. Is feedback on the trainee's progress required during training?" )
     
     print( " 1 = yes or 2 = no" )
     
def convert_fb_to_string(fb_answer):

     feedback_responses = { '1':"yes", '2':"no" }
     return feedback_responses.get(fb_answer)
     

main()

input("\nRun complete. Press the Enter key to exit.")
