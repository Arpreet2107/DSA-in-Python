from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store grouped anagrams
        groups = {}

        # Loop through each word
        for word in strs:
            # Sort the word to get the key
            key = ''.join(sorted(word))

            # If key not present, create a new list
            if key not in groups:
                groups[key] = []

            # Add the word to its anagram group
            groups[key].append(word)

        # Return all the grouped anagrams as a list of lists
        return list(groups.values())


# ------------------ MAIN FUNCTION ------------------
def main():
    # User inputs words separated by commas
    user_input = input("Enter words separated by commas: ")

    # Convert input into list
    words = [w.strip() for w in user_input.split(",")]

    # Create an object of Solution
    sol = Solution()

    # Get the result
    result = sol.groupAnagrams(words)

    # Print output
    print("\nGrouped Anagrams:")
    for group in result:
        print(group)


# Run main when executed directly
if __name__ == "__main__":
    main()
