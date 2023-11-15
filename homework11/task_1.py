
if __name__ == '__main__':
    with open('myfile.txt', 'w', encoding='UTF-8') as fw:
        fw.write('Hello, file world!\n')

    with open('myfile.txt', 'r', encoding='UTF-8') as fr:
        text = fr.read()
        print(text)
