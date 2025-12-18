def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data)
    d = file.read()
    l = 0
    for i in d:
        if i.isdigit():
            l += int(i)
    return l
print(main('data/data07.txt'))
# Read data from file