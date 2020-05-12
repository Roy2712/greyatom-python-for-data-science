# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Manson','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print('Marks scored by Geoffrey Hinton:',courses)

# Slice the dict and stores  the all subjects marks in variable
Math=courses['Math']
English=courses['English']
History=courses['History']
French=courses['French']
Science=courses['Science']
# Store the all the subject in one variable `Total`
total=Math+English+History+French+Science
# Print the total
print(total)
# Insert percentage formula
percentage=(total/500)*100
# Print the percentage
print('percentage:',percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Bengio':50,'Hilary Manson':70,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)

# Given string


# Create variable first_name 
first_name=topper.split()[0]
# Create variable Last_name and store last two element in the list
Last_name=topper.split()[1]
# Concatenate the string
full_name=Last_name+" "+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name= full_name.upper()
print(certificate_name)
# Code ends here


