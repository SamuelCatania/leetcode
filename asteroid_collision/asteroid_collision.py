class Solution:

    def asteroidCollision(self, asteroids: [int]) -> [int]:

        stack = Stack()

        for index in range(0, len(asteroids)):

            if asteroids[index] > 0:
                stack.push(asteroids[index])

            elif not stack.get_length() == 0 and stack.peek() > 0:
                stack = rolling_left(stack, asteroids[index])

            else:
                stack.push(asteroids[index])

        reverse = Stack()

        for index in range(0, stack.get_length()):
            reverse.push(stack.pop())

        final_list = []

        for index in range(0, reverse.get_length()):
            final_list.append(reverse.pop())

        return final_list


class Stack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.insert(0, element)

    def pop(self):
        return self.elements.pop(0)

    def peek(self):
        return self.elements[0]

    def get_length(self):
        return len(self.elements)


def rolling_left(stack, current):

    if stack.get_length() == 0 or stack.peek() < 0:
        stack.push(current)

    else:
        prev = stack.pop()

        if abs(prev) > abs(current):
            stack.push(prev)

        elif abs(prev) < abs(current):
            rolling_left(stack, current)

    return stack
