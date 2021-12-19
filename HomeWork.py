#Create a list that contains all the even numbers between 1 and 299.

list = []
for i in range (1,299):
    if (i % 2) == 0 :
        list.append(i)

print("\nThe list is : ",list)

#Iterate through the previously created list and print first the length of the list then all the squared values of the list.

print("\nThe length of the list is : ",len(list))

for j in list:
    if (j**0.5 == int(j**0.5)) :
        print("\nThe number ",j," is a sequare")

#In one line check if 57 is in the list using one line of python.

print(57 in list) # Returns true if 57 is in the list and False if not


