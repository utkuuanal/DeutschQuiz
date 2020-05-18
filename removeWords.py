import json
deutsch = json.load(open("text.txt"))

def Remove():
    while True:
        try:
            
            print("Which german word you want to remove from the dictionary")
            deutsch.pop(input())
            print("Word removed")
            json.dump(deutsch, open("text.txt",'w'))
        except:
            print("That word doesnt exist in the dictionary, you should add it")
        
        
Remove()