def dig(n):
    if n<10:
        return 1
    else:
        return 1+dig(n/10)
