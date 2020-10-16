#------assignment=01 -----------------------------

string1 = str(input("enter your input : "))
print(*string1, sep = ", ")


#------assignment=02---------

string2 = "google"
string3 = "facebook"

arr = []
result = ","
for i in string2 :
    if i in string3 :
        arr.append(i)

for j in string3 :
    if j in string2 :
        arr.append(j)

for x in arr :
    result = x
    print(result )


