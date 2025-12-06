def daily_temperatures(temperatures):
    answer = [0 for _ in range(len(temperatures))]
    stack = []

    for index, temp in enumerate(temperatures):
        if stack:
            for i in range(len(stack) - 1, -1, -1):
                top = stack[i]
                if top[1] < temp:
                    stack.pop()
                    answer[top[0]] = index - top[0]
        stack.append((index, temp))

    return answer

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
