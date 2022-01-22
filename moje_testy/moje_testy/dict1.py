from collections import defaultdict


def reverse_dict(data: dict) -> dict:
    rd = defaultdict(list)
    for k, v in data.items():
        print(rd)
        rd[v].append(k)
        print(rd)
    return rd


if __name__ == "__main__":
    from collections import Counter

    data = "aaa bbb ccc ddd aaa bbb ccc aaa"
    c = Counter(data.split())
    print(c)
    # Counter({'aaa': 3, 'bbb': 2, 'ccc': 2, 'ddd': 1})
    rd = reverse_dict(c)
    print(rd)
    # defaultdict(<class 'list'>, {3: ['aaa'], 2: ['bbb', 'ccc'], 1: ['ddd']})

    print('\n')

print(rd.keys())

print(rd.values())

print(rd.items())