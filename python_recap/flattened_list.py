from typing import List, Any

result = list()


def flatten_list(lst: list[Any]) -> list[int | str]:
    for each in lst:
        if isinstance(each, list):
            flatten_list(each)
        else:
            result.append(each)
    return result


def main():
    flattened_list = flatten_list([1, [2, 3, 4, [5, [6, 7]]], 8])
    print(flattened_list)


if __name__ == "__main__":
    main()
