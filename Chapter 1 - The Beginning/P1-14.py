# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

sen = input()
HighClass_Letters = [x for x in sen if x.isupper() == True]
LowBorn_Letters = [x for x in sen if x.islower() == True]

print(f"UPPER CASE {len(HighClass_Letters)} LOWER CASE {len(LowBorn_Letters)}")