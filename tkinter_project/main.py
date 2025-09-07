from calculator import calculator

if __name__ == '__main__':
    try:
        print(calculator())
    except ValueError:
        print("Invalid inputs")

