def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    d = file.read()
    l = []
    for i in d:
        if i.isdigit():
            l.append(i)
    return l
print(main('data/data03.txt'))

# Read data from file
