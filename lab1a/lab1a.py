def count_character_in_file(filename, character):
    with open(filename, "r") as file:
        text = file.read()
    # Count the number of times the character appears in the text
    char_count = text.count(character)
    # Split text into sentences
    sentences = text.split(".")
    # Filter sentences that begin with an uppercase alphabet
    sentences_with_uppercase = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip() and sentence.strip()[0].isupper()
    ]

    return char_count, sentences_with_uppercase


def main():
    # Accept file name from the user
    filename = input("Enter the file name: ")

    # Accept the character to count from the user
    character = input("Enter the character to count: ")

    # Ensure only one character is entered
    if len(character) != 1:
        print("Please enter only one character.")
        return

    try:
        # Count character and get sentences
        char_count, sentences_with_uppercase = count_character_in_file(
            filename, character
        )

        # Display the character count
        print(f"The character '{character}' appears {char_count} times in the file.")

        # Display sentences that begin with an uppercase alphabet
        print("Sentences beginning with an uppercase alphabet:")
        for sentence in sentences_with_uppercase:
            print(sentence)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
