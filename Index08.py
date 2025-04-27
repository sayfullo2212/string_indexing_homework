def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    i=0
    while i<5 :
        if s[i]=='*' :
            return i
        else :
            return False
    return i
        