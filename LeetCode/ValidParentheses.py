class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # If it's an opening bracket, push to stack
            if ch in pairs.values():
                stack.append(ch)
            else:
                # If closing bracket but stack empty or mismatch → invalid
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
    
        # Valid only if no unmatched openings remain
        return len(stack) == 0
