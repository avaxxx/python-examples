def even(n):
    sum = 0
    while n > 0:
        sum = sum + (4*n*n)
        n = n - 1
    return sum
def main():
    assert even(1) == 4
    assert even(2) == 20
    assert even(3) == 56
    assert even(4) == 120
    assert even(10) == 1540
    assert even(134) == 3244140

if __name__ == "__main__":
    main()