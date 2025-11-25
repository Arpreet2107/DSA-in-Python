from typing import List

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Count of substrings having 3 distinct characters
        count = 0

        # Loop through all possible substrings of length 3
        for i in range(len(s) - 2):
            substring = s[i:i+3]  # Take 3 characters

            # Check if all 3 characters are different
            if len(set(substring)) == 3:
                count += 1

        return count


# ------------------ MAIN FUNCTION ------------------
def main():
    # Take input string
    s = input("Enter a string: ")

    # Create object of Solution class
    sol = Solution()

    # Call function
    result = sol.countGoodSubstrings(s)

    # Print output
    print("Number of good substrings of size 3:", result)


# Run main when executed directly
if __name__ == "__main__":
    main()
