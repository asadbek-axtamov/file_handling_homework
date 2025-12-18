def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    d = file.readlines()
    l = []
    for i in d:
        l.append(len(i)-1)
    return l
print(main('data/data06.txt'))


    
# Read data from file