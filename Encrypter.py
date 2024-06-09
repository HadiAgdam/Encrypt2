from random import randint

symbols = "! @ # $ % ^ & *".split(" ")

li = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)] + symbols

li_old = [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]


def get_old(v: int):
    return li_old[v % len(li_old)]


def get(v: int):
    return li[v % len(li)]


def get_index(e):
    for i in range(0, len(li)):
        if e == li[i]:
            return i


class Encrypter:
    def __init__(self, key: str):
        a = 0
        for i in key:
            a += ord(i)
        self.key = a * len(key) + 1

    def encrypt(self, text: str, r1: int = -1, r2: int = -1):

        if r1 == -1:
            r1 = randint(0, len(li) - 1)

        if r2 == -1:
            r2 = randint(0, len(li) - 1)

        result = get(r1)

        for j in range(0, len(text)):
            t = text[j]
            i = get_index(t)
            if not i:
                result += t
                continue
            result += get(i + r1 + self.key - r2 + j)

        result += get(r2)

        return result, r1, r2

    def decrypt(self, text: str):
        result = ""

        if text.lower() == text:  # it means using old method
            print("old method")
            for i in range(0, len(text)):
                if li_old.__contains__(text.lower()[i]):
                    result += get_old(li_old.index(text.lower()[i]) - self.key - i)
                else:
                    result += text[i]

            print(result)
            print()

        result = ""

        r1 = get_index(text[0])
        r2 = get_index(text[len(text) - 1])

        for i in range(1, len(text) - 1):
            t = text[i]
            j = get_index(t)
            if not j:
                result += t
                continue
            result += get(j - r1 - self.key + r2 - i + 1)

        return result
