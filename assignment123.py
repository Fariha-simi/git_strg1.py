#------assignment=01 -----------------------------

string1 = str(input("enter your input : "))
#print(*string1, sep = ", ")
print("[string1]")

#------assignment=02---------

string2 = str(input("enter 1st string : "))
string3 = str(input("enter 2nd string : "))
string4 = ""
for i in string2 :
    if i in string3 :
        string4 = i
        print(string4)

print(*string4, sep = "," )


#---------assignment=03-----------------

string5 = str(input("enter 1st string : "))
string6 = str(input("enter 2nd string : "))
string7 = ""
for i in string5 :
    if i not in string6 :
        string7 = i
        print(string7)
