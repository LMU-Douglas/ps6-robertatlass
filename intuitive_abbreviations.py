def is_intuitive(element, abreviation):
    """
    Brandon is learning the periodic table!
    
    However, he doesn’t like some of the elements because the symbol of the element contains letters which are not present in the name of the element.
    He finds this to be unintuitive, especially because in other contexts, he expects abbreviations to not introduce random letters.

    Given a string and a proposed abbreviation, determine if Brandon would find it intuitive.

    Brandon finds an abbreviation intuitive if and only if:

    Every letter that appears in the abbreviation appears in the original string.

    Any letter could be lower or uppercase to start, but your return statement will be case sensitive.

    The first paramater of the function will be a string with an element name. The second will be a proposed abbreviation.

    TODO: For each test case, if all the letters in the abbreviation appear in the name, return a line containing the string “YES”. Otherwise, return a line containing the string “NO”.
    """
    element = element.lower()
    abreviation = abreviation.lower()

    for letter in abreviation:
        if letter not in element:
            return "NO"
    return "YES"

    return None # TODO: Implement this function

