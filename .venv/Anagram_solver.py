from itertools import permutations

if __name__ == "__main__":
    scrambled_word = "rescue"

    print(f"--- Anagram Permutation Generator ---")
    print(f"Generating all possible combinations for the letters in '{scrambled_word}':\n")

    # Generate all unique permutations of the letters
    # The 'set' is used to remove duplicates caused by the two 'e's
    possible_words = set([''.join(p) for p in permutations(scrambled_word)])

    # Print all possibilities
    count = 0
    for word in sorted(list(possible_words)):
        print(word, end='  ') # Print with two spaces
        count += 1
        if count % 10 == 0: # Start a new line every 10 words
            print()

    print(f"\n\nGenerated {len(possible_words)} unique permutations.")
    print("Look through the list above to find the real word.")