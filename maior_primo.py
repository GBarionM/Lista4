def primo(k):
    i = 2
    x = 1
    while x != 0 and i < k:
        x = k % i
        i = i + 1
    if x == 0:
        return False
    else:
        return True

def maior_primo(n):
    i = n
    while i > 1:
        if primo(i):
            return i
            break
        else:
            i = i - 1
