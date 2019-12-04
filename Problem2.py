
def Problem2(num1: int, num2: int) -> int:
    answer = num1 ** 2 + num2 ** 2
    print("The answer is: ", answer)
    return answer


print("num1: ")
num1 = int(input())
print("num2: ")
num2 = int(input())
Problem2(num1, num2)
