questions=[
["who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First president","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",4],
["Who is the india's First man on space","Mahatma Gandhi","Rakesh sharma","Jawahar lal nehru","Rajendra prasad",2],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
["Who is the india's First prime minister","Mahatma Gandhi","Subhash chandra bosh","Jawahar lal nehru","Rajendra prasad",3],
]


levels=[1000,2000,3000,5000,10000,20000,50000,100000,200000,500000]
money=0

for i in range(0,len(questions)):
    a=questions[i]
    print(f"\n\nQuestion for ₹{levels[i]}")
    print(a[0])
    print(f"a.{a[1]}                    b.{a[2]}")
    print(f"c.{a[3]}                    d.{a[4]}")

    reply=int(input("Enter your answer (1-4) or 0 to qiut\n"))
    if reply==0:
        money=levels[i-1]
        break
    if reply==a[-1]:
        print(f"You Won ₹{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=500000
    else:
        print("You Lose!")
        break
print(f"Your take home money is{money}")    