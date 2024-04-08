# Creating a list
my_list = ["apple", "banana", "cherry", "date"]

# Accessing elements in a list
print(my_list[0])  # Output: apple
print(my_list[2])  # Output: cherry

# Modifying elements in a list
my_list[1] = "grape"
print(my_list)  # Output: ["apple", "grape", "cherry", "date"]

# Adding elements to a list
my_list.append("elderberry")
print(my_list)  # Output: ["apple", "grape", "cherry", "date", "elderberry"]

# Removing elements from a list
my_list.remove("cherry")
print(my_list)  # Output: ["apple", "grape", "date", "elderberry"]

# Checking if an element exists in a list
if "banana" in my_list:
    print("Yes, banana exists in the list.")

# Length of a list
print(len(my_list))  # Output: 4

# Slicing a list
print(my_list[1:3])  # Output: ["grape", "date"]

# Looping through a list
for item in my_list:
    print(item)

