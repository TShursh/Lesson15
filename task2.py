import task01


def main():
    password = str(input("Input your password: "))

    result = task01.check_password(password)

    msg = f"You password is {result}" if isinstance(result, str) else f"User data invalid"

    print(msg)


main()
