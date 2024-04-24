
thing = input("\n Enter The Things: ")
thing2 = float()
stuff = []

for i in thing.split(', '):
    stuff.append(float(i))
    thing2 += float(i)
    
print("\n This is what came up:\n", ' + '.join(str(n) for n in stuff), f"= {thing2}")

print("\n\t --------------------------------\n\t This program was brought to you\n\t\t    by Boredom\n\t\t  (& Redzwinger)\n\t --------------------------------\n")

# Crafted By Redzwinger #