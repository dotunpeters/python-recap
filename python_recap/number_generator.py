def solution(digits: str, num: str) -> int:
    """Return the milliseconds it took to type number
    Milliseconds to type a number == abs(previous_index - number index)
    """
    position_lookup = {digit: index for index, digit in enumerate(digits)}
    milliseconds, start = (0, 0)
    for each in num:
        each_index = position_lookup[each]
        milliseconds += abs(start - each_index)
        start = each_index

    return milliseconds


print(solution("0123456789", "210"))
print(solution("8459761203", "5439"))
