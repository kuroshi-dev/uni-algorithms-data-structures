def sum_until_negative():
    total = 0.0
    while True:
        try:
            x = float(input())
        except (ValueError, EOFError):
            break
        if x < 0:
            break
        total += x
    print("Sum: ")
    return int(total) if total.is_integer() else total

def main():
    print("Enter numbers to sum (negative number to stop):")
    print(sum_until_negative())
if __name__ == "__main__":
    main()