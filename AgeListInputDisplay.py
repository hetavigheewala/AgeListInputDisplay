
# Define an empty list named students
students = []

# Ask the user to input age values for 5 people into the list
for i in range(5):
    age = int(input(f"Enter the age for person {i+1}: "))  # Ask for age input
    students.append(age)  # Add the entered age to the list

# Display the contents of the list, one item per line
print("Age values entered:")
for age in students:  # Loop through the list
    print(age)  # Print each age value on a new line
