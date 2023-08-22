#Numeric Type: int, float, complex
x = int(20)
print("Integer number example ",+x)

y= float(13.4)
print("Float number example:",+y)

z = complex(1j)
print("Complex number is like: ",+z)

#String
#an example of a string
a = "hello world"
print(a)

#multiline string: we can add multiline string by placing multiple words inside """" """
multiline = """What is your name?
            I am Anil Bikram Thapa.
            I am 25 years old.
            """
print(multiline)

#we can loop through the letters as well
for x in "banana":
    print(x)

#we can check the string as well.
txt = "My name is Anil Bikram Thapa"
if "Anill" in txt:
    print("Yes, Anil is present in the text.")
elif "Sagar" not in txt:
    print("No, Sagar is not in the text.")

#string methods
text = txt.split()
for x in text:
    print(x)

#Sequence Type: list, tuple, range

#List
print("Items in lists are:")
namelist = ["Anil","Sagar","Suresh","Roshan"]
newlist = namelist.copy()

newlist.remove("Sagar")
for names in newlist:
    print(names)




#Mapping Type: dict



#Set Types: set, frozenset



#Boolean Type: bool

