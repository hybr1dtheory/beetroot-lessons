def get_sub(s: str) -> str:
    sub = ""
    for i in range(len(s) // 2):
        sub += s[i]
        if (s.count(sub) * len(sub)) == len(s):
            return sub
    return s


def gcd(a: int, b: int) -> int:
    return abs(a) if b == 0 else gcd(b, a % b)


def gcd_of_strings(str1, str2):
    sub = get_sub(str1)
    if (str2.count(sub) * len(sub)) == len(str2):
        a = str1.count(sub)
        b = str2.count(sub)
        k = gcd(a, b)
        return sub * k
    else:
        return ""


res = gcd_of_strings("AAAAAAAAA", "AAACCC")
print(res)
