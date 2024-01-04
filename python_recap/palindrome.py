
def pali(val_str: str) -> bool:
    if len(val_str) <= 1:
        return True
    return val_str[0] == val_str[-1] and pali(val_str[1:-1])


if __name__ == '__main__':
    print(pali("noon"))
