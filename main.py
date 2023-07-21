def isomorphic(s: str, t: str) -> bool:
    list_s = {}
    list_t = {}

    for s_elem, t_elem in zip(s, t):
        if s_elem in list_s:
            if list_s[s_elem] != t_elem:
                return False
        else:
            list_s[s_elem] = t_elem

        if t_elem in list_t:
            if list_t[t_elem] != s_elem:
                return False
        else:
            list_t[t_elem] = s_elem
    return True


if __name__ == '__main__':
    print("Complete")
