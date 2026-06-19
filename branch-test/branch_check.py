def sample(number):
    total = 0
    for num in range(1, number + 1):
        total += num
    return total


if __name__ == "__main__":
    res = sample(5)
    print(res)
