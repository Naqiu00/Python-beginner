# if __name__ == '__main__'
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# python interpreter sets "special variables" one of it : if __name__ = '__main__'
# python will assign the __name__ variable value of '__main' if it's the initial value being run

def main():
    print("Hello")

if __name__ == '__main__':
    main()
