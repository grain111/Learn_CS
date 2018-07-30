def find_string(string, text):
    p = 151

    hs = hash(string, p)
    ls = len(string)
    ht = hash(text[:ls], p)
    lt = len(text)

    for i in range(lt - ls + 1):
        if hs == ht:
            if string == text[i:i+ls]: return True
        if (i + ls) != lt:
            ht = next(ht, text[i], text[i+ls], p)

    return False


def hash(s, p):
    ans = 0
    for char in s:
        ans += ord(char)
    return ans % p

def next(hash, first, new, p):
    hash -= ord(first)
    hash += ord(new)
    return hash % p
