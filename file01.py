def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    d = f.read()
    return d
print(main('data/data01.txt'))
    

# Read data from file