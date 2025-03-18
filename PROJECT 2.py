import re

def count_words(text: str) -> int:
   
    words = re.findall(r'\b\w+\b', text)  
    return len(words)

def main():
   
    print("\n===== Word Counter Program =====")

    text = input("Enter a sentence or paragraph: ").strip()

    if not text:
        print("\n⚠ Error: No text entered. Please provide a valid sentence or paragraph.")
        return
    
    word_count = count_words(text)

    print(f"\n✅ Total Word Count: {word_count}\n")

if __name__ == "__main__":
    main()
