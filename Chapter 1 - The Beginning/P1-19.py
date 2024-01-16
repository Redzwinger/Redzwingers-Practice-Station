# Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score. The priority is that name > age > score. If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use itemgetter to enable multiple sort keys.

from operator import itemgetter

def sort_tuples(tuples_list):
    sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))
    return sorted_tuples

tuples_list = []

while True:
    input_str = input("Enter tuple (name, age, height) or type 'done' to exit: ")
    
    if input_str.lower() == 'done':
        break
    
    input_values = input_str.split(',')
    
    if len(input_values) == 3:
        name, age, height = map(str, input_values)
        tuples_list.append((name, age, height))
    else:
        print("Invalid input! Please enter a valid tuple.")

sorted_tuples = sort_tuples(tuples_list)
print("Sorted Tuples:")
print(sorted_tuples)
