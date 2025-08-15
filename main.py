def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def reverse_string(s):
    return s[::-1]

def main():
    print("Factorial of 5:", factorial(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Prime numbers up to 30:", primes_up_to(30))
    print("Reverse of 'Python':", reverse_string("Python"))
    for i in range(1, 11):
        print(i, "factorial is", factorial(i))

if __name__ == "__main__":
    main()
