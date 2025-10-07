def fibonacci_recursive(n):
    """Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: # n > 1
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def Ifibonacci():
    """Programm interface for calculating Fibonacci numbers."""
    choose: int = 0
    while choose != 3:
        print("\nChoose an option:")
        print("1. Calculate Fibonacci (Recursive)")
        print("2. Calculate Fibonacci (Iterative)")
        print("3. Exit")
        choose = int(input("Enter your choice (1-3): "))
        if choose == 1:
            n = int(input("Enter a positive integer: "))
            result = fibonacci_recursive(n)
            print(f"The {n}th Fibonacci number (Recursive) is: {result}")
        elif choose == 2:
            n = int(input("Enter a positive integer: "))
            # result = fibonacci_iterative(n)
            print(f"The {n}th Fibonacci number (Iterative) is: {result}")
        elif choose == 3:
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")
def main():
    Ifibonacci()

if __name__ == "__main__":
    main()