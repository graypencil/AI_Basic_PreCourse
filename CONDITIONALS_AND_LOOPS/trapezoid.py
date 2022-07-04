def addition(x, y):
    return x + y + 100

def multiply(x, y):
    return x * y

def divided_by_2(x):
    return x / 2

def main():
    print(15 == addition(10, 5))
    print(addition(10, 100) == 110)


if __name__ == "__main__": # shell 에서 실행 시 위 main 코드는 작용하지 않음.
    main()