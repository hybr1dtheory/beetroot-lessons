from sequences import lukas

if __name__ == '__main__':
    print('Welcome to the Lukas sequence calculator!')
    num = int(input('Enter the number of the element:\n'))
    l_0 = int(input('Enter the start element of sequence (L0):\n'))
    l_1 = int(input('Enter the next element of sequence (L1):\n'))
    print(f'The {num} element is:', lukas(num, l_0, l_1))
