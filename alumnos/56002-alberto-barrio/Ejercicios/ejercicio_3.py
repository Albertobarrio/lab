def interface():
    print("Ingrese un numero (use una letra para terminar): ")
    histogram(list_input())


def list_input():
    numbers = []
    while True:
        number = input()
        if number.isalpha():
            break
        numbers.append(number)
    return numbers


def histogram(numbers):
    for i in range(1, 10):
        print(str(i) + ": " + numbers.count(str(i)) * "#")


if __name__ == "__main__":
    interface()
