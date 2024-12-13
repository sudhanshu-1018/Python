
print("Let star the game snake,water,gun:\n where type:\nS for snake\nW for water\nG for gun")
k=input("Enter your option(S/W/G):\nYOU- ")
l=["snake","water","gun","snake","water","gun","snake","water","gun"]
import random
word=random.choice(l)

# def check(word,k):
#        if (word=="snake"and k=="S") or (word=="water" and k=="W") or (word=="gun" and k=="G"):
#               return 0
#        if (word=="snake"and k=="W") or (word=="water" and k=="G") or (word=="gun" and k=="S"):
#               return -1
#        if (word=="snake"and k=="G") or (word=="water" and k=="S") or (word=="gun" and k=="W"):
#               return 1

for i in k,word:
    if k=="S"or k=="W"or k=="G":
        print(f"COMPUTER- {word}")
        if k=="S" and word=="snake":
            print("DRAW")        
        elif k=="S" and word=="water":
                print("you won")            
        elif k=="S" and word=="gun":
                    print("you lose")
                    
        
        if k=="W" and word=="snake":
            print("you lose")        
        elif k=="W" and word=="water":
                print("you draw")            
        elif k=="W" and word=="gun":
                    print("you won")
                    
        
        if k=="G" and word=="snake":
            print("you won")        
        elif k=="G" and word=="water":
                print("you lose")            
        elif k=="G" and word=="gun":
                    print("draw")
                    break
        else:
               break
    else:
            print("Enter invalid input")
            break