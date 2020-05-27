import random
import json

deutsch = json.load(open("text.txt"))


print("Hello quiz started \n While in quiz you can type 'stopquiz' to stop the quiz\n  'pass' to pass to the next question\n   's' to show the current question's answer\n    hatalar olabilir yağmur :-)")

def quiz():
    global deutsch
    while len(deutsch)>0:
        question={}
        a=random.choice(list(deutsch))
        question[a]=deutsch.pop(a)
        
        values_view = question.values()
        value_iterator = iter(values_view)
        answer = next(value_iterator)
         
        print(answer+"=?")
        
        while True:
            try:
                x=input()
                question[x]==answer and x=="stopquiz"
                print("correct")
                break     
            except:
                if x=="pass":
                    break
                if x=="s":
                    print(a+' '*10 +"<--NOW TYPE IT >:| ")
                elif x=="stopquiz":
                    raise KeyboardInterrupt("help me enlarge the quiz dictionary... type help for help while in you are in quiz ")
                else:
                    print ("close but not close enough, try again")
                


quiz()

