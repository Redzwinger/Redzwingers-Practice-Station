# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

def find_stuf():
    numb = []
    for i in range(2000, 3200):
        if ((i % 7 == 0) & (i % 5 !=0)):
            numb.append(i)
            
    return numb

numbe = find_stuf()
print(numbe)
=========
print(numbe)
>>>>>>>>> Temporary merge branch 2
=========
print(numbe)
>>>>>>>>> Temporary merge branch 2
=========
print(numbe)
>>>>>>>>> Temporary merge branch 2

=========
print(numbe)
>>>>>>>>> Temporary merge branch 2
