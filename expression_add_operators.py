class Solution:
    def addOperators(self, num, target):
        result = []

        def backtrack(index, expression, value, previous):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break

                current = num[index:i + 1]
                current_value = int(current)

                if index == 0:
                    backtrack(i + 1, current, current_value, current_value)
                else:
                    backtrack(i + 1, expression + "+" + current,
                              value + current_value, current_value)

                    backtrack(i + 1, expression + "-" + current,
                              value - current_value, -current_value)

                    backtrack(i + 1, expression + "*" + current,
                              value - previous + previous * current_value,
                              previous * current_value)

        backtrack(0, "", 0, 0)
        return result
