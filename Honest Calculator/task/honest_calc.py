msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0


def get_equation() -> str:
    print(msg_0)
    return input()


def is_one_digit(v: float) -> bool:
    return v.is_integer() and -10 < v < 10


def parse_equation(calc: str):
    parts = calc.split()
    if len(parts) != 3:
        return None
    return parts[0], parts[1], parts[2]


def convert_number(value: str):
    global memory
    if value == "M":
        return memory
    try:
        return float(value)
    except ValueError:
        return None


def validate_numbers(x: str, y: str):
    x_val = convert_number(x)
    y_val = convert_number(y)
    if x_val is None or y_val is None:
        print(msg_1)
        return None
    return x_val, y_val


def validate_operator(oper: str) -> bool:
    if oper not in ("+", "-", "*", "/"):
        print(msg_2)
        return False
    return True


def calculate(x: float, oper: str, y: float) -> float | None:
    if oper == "+":
        return x + y
    if oper == "-":
        return x - y
    if oper == "*":
        return x * y
    if oper == "/":
        if y == 0:
            print(msg_3)
            return None
        return x / y
    return None


def check(v1: float, v2: float, v3: str) -> None:
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and v3 in ("*", "+", "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


def ask_store(result: float) -> None:
    global memory
    print(msg_4)
    ans = input().lower()
    if ans == "y":
        if is_one_digit(result):
            messages = [msg_10, msg_11, msg_12]
            for m in messages:
                print(m)
                ans = input().lower()
                if ans == "y":
                    continue
                elif ans == "n":
                    return
            memory = result
        else:
            memory = result


def main() -> None:
    while True:
        calc = get_equation()
        parsed = parse_equation(calc)

        if not parsed:
            continue

        x_str, oper, y_str = parsed
        numbers = validate_numbers(x_str, y_str)

        if not numbers:
            continue

        x, y = numbers
        if not validate_operator(oper):
            continue

        check(x, y, oper)

        result = calculate(x, oper, y)
        if result is None:
            continue

        print(result)

        ask_store(result)

        print(msg_5)
        ans = input().lower()
        if ans == "y":
            continue
        elif ans == "n":
            break


if __name__ == "__main__":
    main()