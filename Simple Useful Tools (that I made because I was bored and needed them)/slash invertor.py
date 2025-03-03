def convert_path(path: str, format_type: int) -> str:
    """
    Converts a file path based on user selection:
    1 - Convert `/` to `\`
    2 - Convert `\` to `/`
    3 - Convert single `\` to double `\\`
    4 - Convert double `\\` to single `\`
    """
    if format_type == 1:
        return path.replace("/", "\\")
    elif format_type == 2:
        return path.replace("\\", "/")
    elif format_type == 3:
        return path.replace("\\", "\\\\")
    elif format_type == 4:
        return path.replace("\\\\", "\\")
    else:
        return "Invalid option. Choose a number between 1 and 4."

# Main loop
if __name__ == "__main__":
    while True:
        print("\n================ Path Converter =================")
        test_path = input("Enter the file path: ")
        print("\nChoose a conversion option:")
        print("1 - Convert `/` to `\\`")
        print("2 - Convert `\\` to `/`")
        print("3 - Convert single `\\` to double `\\\\`")
        print("4 - Convert double `\\\\` to single `\\`")
        
        try:
            format_choice = int(input("\nEnter the number of your choice: ").strip())
            converted_path = convert_path(test_path, format_choice)
            print("\n===============================================")
            print(f"Converted Path: {converted_path}")
            print("===============================================\n")
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 4.")
            continue
        
        again = input("Do you want to convert another path? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for using the Path Converter! Goodbye!\n")
            break

# Craftily Crafted By Redzwinger #