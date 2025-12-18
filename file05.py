def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    d = file.read()
    digits = 0
    string = 0
    for i in d:
        if i.isdigit():
            digits += 1
        else:
            string += 1
    return [digits, string]
print(main('data/data05.txt'))
# Read data from file