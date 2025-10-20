# 🧩 LeetCode 412. Fizz Buzz
# 📘 Problem Statement
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
## 💡 Real-World Analogy
# Think of FizzBuzz like announcing a roll call:
# - Every 3rd person says "Fizz"
# - Every 5th person says "Buzz"
# - Every 15th person (both) says "FizzBuzz"
# - Everyone else just says their own number.
class Solution:
    def fizzBuzz(self,n:int) -> list[str]:
        answer = []
        for i in range (1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0 :
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

def main():
    n = int(input("Enter a number: "))
    
    solution = Solution()  # create an object of the Solution class
    result = solution.fizzBuzz(n)  # call fizzBuzz using that object
    
    print("\nFizzBuzz Result:")
    print(result)


# ✅ Run the main function when this file is executed directly
if __name__ == "__main__":
    main()
