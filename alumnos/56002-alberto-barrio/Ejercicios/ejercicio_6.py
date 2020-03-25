def Interface():
    input_to_list(input("Ingrese una lista de numeros separados por coma: "))


def input_to_list(numbers):
    numbers_list = numbers.split(",")
    print(numbers_list)


if __name__ == "__main__":
    Interface()
