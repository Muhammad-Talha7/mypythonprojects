def reverse(stri):
    n = 0
    j = len(stri) - 1
    str = list(stri)

    def helper():
        nonlocal n, j, str
        if n >= j:
            return "".join(str)
        else:
            str[n], str[j] = str[j], str[n]
            n += 1
            j -= 1
            return helper()
    return helper()

str1 = "Hello!"
print(reverse(str1))
