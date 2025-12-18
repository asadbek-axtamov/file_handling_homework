def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data)
    d = file.read()
    l = []
    for i in d:
        if i.isdigit():
            l.append(i)
    return min(l)
print(main('data/data09.txt'))

# Read data from file