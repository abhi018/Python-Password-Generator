import random
string = input("Enter data to conver into password :")
string_withoutspace = string.replace(' ','')

mylist = []
for i in string_withoutspace:
    mylist.append(i)
random.shuffle(mylist)



new_pass = ''

for i in mylist:
    new_pass = new_pass + i

print(new_pass)



