def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    count = 0
    if s[0].isdigit():
        count += 1
    if s[1].isdigit():
        count += 1
    if s[2].isdigit():
        count += 1
    if s[3].isdigit():
        count += 1
    if s[4].isdigit():
        count += 1
    return count