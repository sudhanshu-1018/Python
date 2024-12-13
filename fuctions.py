a="sudhanshu kumar singh"
b="suman singh"
print(len(a))
print(a.upper())
print(b.lower())

# Remove
c="!!!sudhanshu!!!"
print(c.rstrip("sudhanshu!!!"))

# Replace
d="sudhanshu---sudhanshu"
print(d.replace("sudhanshu","suman"))

# seprate
e="sudhanshu suman rinshu"
print(e.split(" "))

#uppar case 1st letter ,remaining lowercase
f="introduction to js"
print(f.capitalize())

# center
g="welcome"
print(g.center(50))
print(f.center(50,","))

# count word
h="hello hello"
print(h.count("hello"))

# '''check''' letter/word endswith
i="welcome to console!!!"
print(i.endswith("!!!"))
print(i.endswith("to",4,10))

# find
j="he's name is dan.he is a good boy."
print(j.find("is"))
print(j.find("ishh"))

# must find or error
print(j.index("is"))

#'''check'''only consist of A-Z,a-z,0-9
k="Welcome to The Concole"
print(k.isalnum())

#'''check'''only consist of A-Z,a-z
l="welcome"
print(l.isalpha())

#'''check'''all letter are in lower case
m="welcome in india"
print(m.islower())

#'''check''' all letter are in upper case
n="WELCOME TO INDIA"
print(n.isupper())

#'''check'''all the value within string are printable
o="hi I am sudhanshu"
print(o.isprintable())

#'''check''' space
p="how are  you"
print(p.isspace())

#'''check''' first letter of each word is capital
q="World Health Organisation"
print(q.istitle())

#'''check''' letter/word startswith
r="python is language"
print(r.startswith("python"))
print(r.startswith(p))

# interchange uppercase to lower and viseversa
s="Python Is a Language"
print(s.swapcase())

# capitalized each letter of the word
t="his name is dan"
print(t.title())

