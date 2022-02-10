from Stack_code import Stack


def check_stack():
    data = input('Введите строку: ')
    a = Stack()
    flag = True
    for i in data:
        if i in '([{':
            a.push(i)
        elif i in ')]}':
            if a.size() == 0:
                flag = False
                break
            b = a.pop()
            if b == '(' and i == ')':
                continue
            if b == '[' and i == ']':
                continue
            if b == '{' and i == '}':
                continue
            flag = False
            break

    if flag and a.size() == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(check_stack())