import re
def swap_case(s):
    rString = ""
    for _ in s:
        if re.search(r"[a-z]",_):
            rString += _.upper()
        elif re.search(r"[A-Z]",_):
            rString += _.lower()
        else:
            rString += _
    return rString

s = input()
result = swap_case(s)
print(result)