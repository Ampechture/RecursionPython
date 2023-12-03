def function1(n, div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            return 0
        else:
            return function1(n, div-1)
    else:
        return 1

if __name__ == '__main__':
    print(function1(4))