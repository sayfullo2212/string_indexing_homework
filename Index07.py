def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    i=0
    while i<len(n) :
        if i==n :
            return s[i]
        else :
            return False
    i+=1
    return s[i]
