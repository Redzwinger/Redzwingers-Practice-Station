# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

yaay = []

for n in range(1000, 3001):
    not_a_num = str(n)
    
    if (int(not_a_num[0])%2 == 0 and int(not_a_num[1])%2 == 0 and int(not_a_num[2])%2 == 0 and int(not_a_num[3])%2 == 0):
        yaay.append(not_a_num)
        
print(",".join(yaay))