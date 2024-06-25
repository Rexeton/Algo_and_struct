def num_decodings(s: str) -> int:
    ...
    d = {str(i) for i in range(1, 27)}
    if s[0] == '0' or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    sum = 1
    fib1 = 1
    fib2 = 1
    i = 1
    while i < len(s):
        if s[i - 1] + s[i] not in d:
            sum *= max((fib1),1)
            fib1 = 1
            fib2 = 1
            i += 1
        elif s[i] == '0':
            fib1 = 1
            fib2 = 1
            i += 1
        else:
            fib2, fib1 = fib2 + fib1, fib2
        i += 1
    return sum * fib2



print(num_decodings("1201234"))
print(num_decodings("226"))

print(num_decodings("101"))

print(num_decodings("11106"))
print(num_decodings("12"))
print(num_decodings("0"))



# self.assertEqual(num_decodings("12"), 2)
# self.assertEqual(num_decodings("226"), 3)
# self.assertEqual(num_decodings("0"), 0)
# self.assertEqual(num_decodings("10"), 1)
# self.assertEqual(num_decodings("101"), 1)