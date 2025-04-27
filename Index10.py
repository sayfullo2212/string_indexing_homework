def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    i = 0
    sum = 0
    while i < 5:
        if s[i].isdigit():
            sum += int(s[i])
        i += 1
    return  sum