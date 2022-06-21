class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        while pushed:
            stack.append(pushed[0])
            pushed = pushed[1:]
            while popped and stack and stack[-1] == popped[0]:
                stack.pop()
                popped = popped[1:]

        while popped and stack and stack[-1] == popped[0]:
            stack.pop()
            popped = popped[1:]

        if not pushed and not popped:
            return True
        return False
