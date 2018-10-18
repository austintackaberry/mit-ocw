def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0: return False
    if len(aStr) == 1:
        if aStr == char: return True
        return False
    mid = len(aStr) // 2
    print(mid)
    print(aStr[mid])
    print(ord(aStr[mid]))

    if ord(char) < ord(aStr[mid]):
        return isIn(char, aStr[:mid]
    if ord(char) > ord(aStr[mid]):
        return isIn(aStr[mid+1:]
    if ord(char) == ord(aStr[mid]): return True

print(isIn('a', 'random'))
