import math


def half_adder(a, b, carry=0, verbose=False):
    """
    Iterate until there is no carry.
        carry = a & b
        a = a ^ y
        b = carry << 1

    Ref.: https://en.wikipedia.org/wiki/Adder_(electronics)
    """
    assert a >= 0 and b >= 0
    if verbose:
        print('\t=> {:s}\t[carry = {:b}]'.format(pretty_bin(a), carry))

    # Operator
    if b == 0:
        return a
    else:
        carry = a & b
        return half_adder(a ^ b, carry << 1, carry)


def half_subtractor(a, b, borrow=0, verbose=False):
    """
    Iterate until there is no carry.
        borrow = (~x) & y
        x = x ^ y
        y = borrow << 1

    Ref.: https://en.wikipedia.org/wiki/Subtractor
    """
    assert a >= 0 and 0 <= b <= a
    if verbose:
        print('\t=> {:s}\t[borrow = {:b}]'.format(pretty_bin(a), borrow))

    if b == 0:
        return a
    else:
        borrow = (~a) & b
        return half_subtractor(a ^ b, borrow << 1, borrow)


def multiply(a, b):
    result = 0
    while b > 0:

        # Add a when b is odd
        if isOdd(b):
            result = half_adder(result, a)

        a = a << 1  # Make double
        b = b >> 1  # Make half

    return result


def divide(dividend, divisor):
    assert a >= 0 and b >= 0

    # Initialize the quotient
    quotient = 0
    while dividend >= divisor:
        dividend = half_subtractor(dividend, divisor)
        quotient = half_adder(quotient, 1)

    return quotient


def power(a, b):
    assert a >= 0 and b >= 0

    if b == 0:
        return 1

    # Initialize the quotient
    result = int(a)
    while b > 1:
        result = multiply(result, a)
        b = half_subtractor(b, 1)

    return result


def sqrt(a):
    x = int(a)
    y = 1
    while x > y:
        x = half_adder(x, y) >> 1
        y = divide(a, x)
    return x


def isOdd(a):
    return a & 1


def pretty_bin(a, size_block=4):
    bin_str = '{:b}'.format(a)
    spaces = math.ceil(len(bin_str)/size_block)*size_block  # Number of spaces
    diff = spaces - len(bin_str)
    bin_str = '0'*diff + bin_str
    text = ' '.join([bin_str[i:i + size_block] for i in range(0, len(bin_str), size_block)])
    return text


if __name__ == '__main__':
    a = 15
    b = 3
    c = 25

    print("Values: **************************************")
    print('a = {:d} = {:s}'.format(a, pretty_bin(a)))
    print('b = {:d} = {:s}'.format(b, pretty_bin(b)))

    print("")
    print("Operations: **********************************")

    # [Addition] Half Adder
    res = half_adder(a, b, verbose=False)
    print('[Addition] Half Adder: {:d} + {:d} = {:s} = {:d}\n'.format(a, b, pretty_bin(res), res))

    # [Subtraction] Half Subtractor
    res = half_subtractor(a, b, verbose=False)
    print('[Subtraction] Half Subtractor: {:d} - {:d} = {:s} = {:d}\n'.format(a, b, pretty_bin(res), res))

    # [Multiplication]
    res = multiply(a, b)
    print('[Multiplication]: {:d} x {:d} = {:s} = {:d}\n'.format(a, b, pretty_bin(res), res))

    # [Division]
    res = divide(a, b)
    print('[Division]: {:d} ÷ {:d} = {:s} = {:d}\n'.format(a, b, pretty_bin(res), res))

    # [Power]
    res = power(a, b)
    print('[Power]: {:d}^{:d} = {:s} = {:d}\n'.format(a, b, pretty_bin(res), res))

    # [Sqrt]
    res = sqrt(c)
    print('[Sqrt]: sqrt({:d}) = {:s} = {:d}\n'.format(c, pretty_bin(res), res))

    # is odd?
    print('is {} odd? {}'.format(a, bool(isOdd(a))))
    print('is {} odd? {}'.format(b, bool(isOdd(b))))
    print('')
