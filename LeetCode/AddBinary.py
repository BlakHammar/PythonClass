class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Process both strings from the least significant bit
        while i >= 0 or j >= 0 or carry:
            # Get the current bits (0 if we've exhausted the string)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Sum = bit_a + bit_b + carry
            total = bit_a + bit_b + carry
            result.append(str(total % 2))   # current bit
            carry = total // 2              # new carry
            
            i -= 1
            j -= 1
        
        # Since we built the result backwards, reverse it before returning
        return ''.join(reversed(result))
