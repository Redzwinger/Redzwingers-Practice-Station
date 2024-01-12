# Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

sen = input()
letters = [x for x in sen if x.isalpha() == True]
words = len(sen.split())

print(f"LETTERS {len(letters)} DIGITS {words}")