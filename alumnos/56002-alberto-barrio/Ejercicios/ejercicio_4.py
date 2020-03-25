
def file_to_list():
    numbers = []
    filename = "number.txt"
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            numbers.append(line.rstrip())
        file_object.close()
    return(numbers)


def histogram(numbers):
    for i in range(1, 10):
        print(str(i) + ": " + numbers.count(str(i)) * "#")


if __name__ == "__main__":
    histogram(file_to_list())
