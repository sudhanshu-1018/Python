import re
pattern=r"[A-Z]+[a-z]+lcome"
text='''i Welcome sudhanshu kumar singh and
 you Zslcome sudhanshu kumar singh
'''
# match=re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])

    

