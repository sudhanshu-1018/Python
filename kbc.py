y=input("Press ENTER to start KBC:")
for i in y:
    
    if (y== ""):
        print("hello ,lets start the game")
    else:
        print("exit")
        break
    q=input("Press 1 for first question on you screen for  ₹1000:")
    for s in q:
        
        if (q=="1"):
            print("hello ,lets start the game")
        else:
            print("exit")
            break

        print("1.On which day Republic day is celebrated")
        print("a.26th January","b.2nd October\n""c.15th August","d.25th December",sep="               ")
        choice=input("Enter the option:\na\nb\nc\nd\nwrite Anwer here:")
        if choice in ("a","b","c","d"):
            if choice=="a":
                print("Correct Answer\n'YOU WON ₹1000' ")
            else:
                print("Wrong Answer\n'BETTER LUCK NEXT TIME")
