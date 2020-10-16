#---------assignment=03-----------------


string4 = "google"
string5 = "facebook"
arr1 = []
result1 = ""
for i in string4 :
    if i not in string5 :
        arr1.append(i)

for j in string5 :
    if j not in string4 :
        arr1.append(j)

for y in arr1 :
    result1 = y
    print(result1,end =" " )

    
