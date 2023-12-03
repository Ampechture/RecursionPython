#from 10 to 2< n < 16
#def ten_to_x(x, n):

def convert_base(x, n):

    number = int(x)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEF"
    if number < n:
        return alphabet[number]
    else:
        return convert_base(number // n, n) + alphabet[number % n]

if __name__ == '__main__':
    print(convert_base(422, 16))