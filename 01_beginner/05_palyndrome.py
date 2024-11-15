def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        xstring = str (x)
        for i in range (0,len(xstring)):
                print (i)
                if xstring[i] != xstring[len(xstring)-i - 1]:
                        return False
                
        return True
def isPalindromeV2(x):
        """
        :type x: int
        :rtype: bool
        """
        xstring = list(str (x))
        print (xstring)
        xstring_reversed = list(str(x))[::-1]
        print (xstring_reversed)
        return xstring_reversed == xstring



print(isPalindromeV2 (121))
print(isPalindromeV2 (1211))