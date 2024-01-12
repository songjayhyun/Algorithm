def find_next_greater(numbers):
    stack = []
    result = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            result[stack.pop()] = numbers[i]
        stack.append(i)

    return result

def solution(numbers):
    answer = find_next_greater(numbers)
    return answer