def isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict_s = {}
    dict_t = {}

    for s_elem, t_elem in zip(s, t):
        if s_elem in dict_s:
            if dict_s[s_elem] != t_elem:
                return False
        else:
            dict_s[s_elem] = t_elem

        if t_elem in dict_t:
            if dict_t[t_elem] != s_elem:
                return False
        else:
            dict_t[t_elem] = s_elem
    return True
