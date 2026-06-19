def sample(number):
    is_int = isinstance(number, int)
    if not is_int:
        return f"{number}は数値ではありません"
    else:
        total = 0
        for num in range(1, number + 1):
            total += num
        return total


if __name__ == "__main__":
    res = sample("5")
    print(res)
