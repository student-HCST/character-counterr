def word_character_counter():
    print("===== Word & Character Counter =====")
    text = input("Enter your text: ")

    # Count words
    words = len(text.split())

    # Count characters
    characters_with_spaces = len(text)
    characters_without_spaces = len(text.replace(" ", "").replace("\t", "").replace("\n", ""))

    # Count lines
    lines = len(text.splitlines())

    # Display results
    print("\n===== Results =====")
    print("Words:", words)
    print("Characters (with spaces):", characters_with_spaces)
    print("Characters (without whitespace):", characters_without_spaces)
    print("Lines:", lines)


word_character_counter()
