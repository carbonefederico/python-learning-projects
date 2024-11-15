def longestCommonPrefix(strs):
    

    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 0:
        return ""
    
    if len(strs) == 1:
        return strs[0]

    longest_prefix = ""

    for prefix in range (1,len(strs[0]) + 1):
        current_prefix = strs[0][:prefix]
        prefixFound = True
        for string in strs[1:]:
            if not (string.startswith(current_prefix)):
                prefixFound = False
                break

        if (prefixFound):
            longest_prefix = current_prefix
        else:
            return longest_prefix
    
    return longest_prefix


print(longestCommonPrefix(["ab", "a"]))
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
