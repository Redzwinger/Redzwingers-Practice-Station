# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

dumINP = input()

one = int("%s" % dumINP)
two = int("%s%s" % (dumINP, dumINP))
three = int("%s%s%s" % (dumINP, dumINP, dumINP))
four = int("%s%s%s%s" % (dumINP, dumINP, dumINP, dumINP))

thingy = one + two + three + four

print(thingy)