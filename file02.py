def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    d = f.read()
    return len(d)
print(main('data/data02.txt'))
# Read data from file