import re

def count_words(text: str) -> int:
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The input text provided by the user.
    
    Returns:
        int: The total number of words in the text.
    """
    words = re.findall(r'\b\w+\b', text)  # Extract words using regex
    return len(words)

def main():
    """
    Main function to run the word counter program.
    
    Features:
    - Prompts the user for input.
    - Validates the input to ensure it's not empty.
    - Counts the words in the input.
    - Displays the word count in a user-friendly manner.
    """
    print("\n===== Word Counter Program =====")

    # Prompt the user to enter a sentence or paragraph.
    text = input("Enter a sentence or paragraph: ").strip()

    # Error Handling: Check if the input is empty.
    if not text:
        print("\n⚠ Error: No text entered. Please provide a valid sentence or paragraph.")
        return  # Exit the function if input is empty
    
    # Word Counting Logic
    word_count = count_words(text)

    # Output Display: Print the word count.
    print(f"\n✅ Total Word Count: {word_count}\n")

if __name__ == "__main__":
    main()
