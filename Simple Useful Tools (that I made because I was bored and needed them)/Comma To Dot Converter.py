while True:
    user_input = input("\n C O M M A S: ")
    modified_string = user_input.replace(',', '.')
    
    print(" D O T S:", modified_string)
    
    choice = input("\n Do you want to continue? (y/whatever): ")
    
    if choice.lower() != 'y':
        break

# Carelessly Crafted By Redzwinger #