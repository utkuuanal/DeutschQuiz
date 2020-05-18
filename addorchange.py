import json
deutsch = json.load(open("text.txt"))
def AddOrChange():
    while True:
        global deutsch
        
        print("Type the german word that you want to add to dictionary")
        de=input()
        print("Type what does that mean in english")
        eng=input()
        deutsch[de]=eng
        json.dump(deutsch, open("text.txt",'w'))
    
    
    
    
    
    
    
    
AddOrChange()