

def longest_substring(s, k):
    temp_str = ""
    temp_set = set()
    for v in range(len(s)):
        for e in range(v, len(s)):
            curr_str = s[v:e+1]
            if len(set(curr_str)) == k:
                if len(curr_str) > len(temp_str):
                    temp_str = curr_str
    return temp_str


if __name__ == "__main__":
    print(longest_substring("dkashhhhhdajskdhh",2))