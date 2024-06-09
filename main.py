from Encrypter import Encrypter

if __name__ == "__main__":

    key = input("key :")
    e = Encrypter(key)
    print()
    while True:
        command = input("command :")

        if command.startswith("ex"):
            r1 = int(command.split(" ")[1])
            r2 = int(command.split(" ")[2])

            i = 5 + len(command.split(" ")[1]) + len(command.split(" ")[2])

            print()
            en = e.encrypt(command[i:], r1, r2)
            print(en[0])
            print(en[1], en[2])
            print()

        elif command.startswith("e"):
            print()
            en = e.encrypt(command[2:])
            print(en[0])
            print(en[1], en[2])
            print()

        elif command.startswith("d"):
            print()
            print(e.decrypt(command[2:]))
            print()


        else:
            print("command not found")
