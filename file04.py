def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    d = file.read()
    l = []
    for i in d:
        l.append(i)
    return l
print(main('data/data04.txt'))
# Read data from file