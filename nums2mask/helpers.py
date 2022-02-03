def csv2list(s: str) -> list[int]:
    return [int(v.strip()) for v in s.split(',')]


assert csv2list('1,2,3') == [1, 2, 3]
assert csv2list('1, 2,3 , 4 ,5 ') == [1, 2, 3, 4, 5]
