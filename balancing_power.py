def is_power_balanced(n, party):
    """
    There are n legislators in the State of Confusion, each representing one of the three major parties:

    Future One, Two-gether, and Triple Harmony.

    The founders of the State envisioned a healthy society where the three parties maintain
    the balance of power and no party gets a dictatorial position by having too many legislators.

    Formally, we say that the balance of power is achieved when no one party has strictly
    more legislators than the other two parties combined.

    The function input will have 2 paramaters. The first will be the total number of legislators (n), 
    the second will be n space-separated integers, representing the party aﬃliation of each elected person,
    1 being Futre One, 2 being Two-gether, 3 being Triple Harmony.

    The function will output a string on a single line, representing the headline of the article you will write.

    TODO: If the balance of power is achieved, then print only “Power Balanced” without quotation marks. 
    Otherwise, print only “[Party] Dominates” without quotation marks, where “[Party]” is replaced with the name of the winning party. 
    
    Note that the output is case-sensitive, and must match the format exactly without leading or trailing whitespace.
    """

    future_one = 0
    two_gether = 0
    triple_harmony = 0

    for p in party.split():
        if p == '1':
            future_one += 1
        elif p == '2':
            two_gether += 1
        elif p == '3':
            triple_harmony += 1

    if future_one > two_gether + triple_harmony:
        return "Future One Dominates"
    elif two_gether > future_one + triple_harmony:
        return "Two-gether Dominates"
    elif triple_harmony > future_one + two_gether:
        return "Triple Harmony Dominates"
    else:
        return "Power Balanced"

    return None # TODO: Implement this function

