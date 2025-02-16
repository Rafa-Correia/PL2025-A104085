import sys

def main ():
    total = 0
    current = 0
    is_behaviour_on = True
    on_off_buffer = ""
    for line in sys.stdin:
        for c in line:
            if c == "\n":
                continue
            on_off_buffer = (on_off_buffer + c).lower()[-3:]
            if on_off_buffer == "off":
                is_behaviour_on = False
            if "on" in on_off_buffer:
                is_behaviour_on = True
            if c in "0123456789" and is_behaviour_on:
                current = (current * 10) + int(c)
            else:
                total = total + current
                current = 0
            if c == "=":
                print(f">>{total}")
    print(f">>{total}")

if __name__ == "__main__":
    main()