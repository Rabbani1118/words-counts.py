def count_words(text):
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The text to be processed.
        
    Returns:
        int: The number of words in the text.
    """
    # Split the text into words using spaces as a delimiter
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the word counting program.
    """
    # Prompt the user for input
    text = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not text:
        print("Error: Input cannot be empty. Please enter some text.")
        return
    
    # Call the function to count words
    word_count = count_words(text)
    
    # Display the result
    print(f"The number of words in the given text is: {word_count}")

# Run the program
if __name__ == "__main__":
    main()
