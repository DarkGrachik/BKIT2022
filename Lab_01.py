import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while True:
        try:
        # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
        # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
            break
        except ValueError:
            print(f"{coef_str} не является числом")
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root > 0.0:
            root1=-math.sqrt(root)
            root2=math.sqrt(root)
            result.append(root1)
            result.append(root2)
        if root == 0.0:
            result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1_1 = (-b + sqD) / (2.0*a)
        if root1_1 > 0.0:
            root1=-math.sqrt(root1_1)
            root2=math.sqrt(root1_1)
            result.append(root1)
            result.append(root2)
        if root1_1 == 0.0:
            result.append(root1_1)
        root2_1 = (-b - sqD) / (2.0*a)
        if root2_1 > 0.0:
            root3=-math.sqrt(root2_1)
            root4=math.sqrt(root2_1)
            result.append(root3)
            result.append(root4)
        if root2_1 == 0.0:
            result.append(root2_1)
    return result


def main():
    '''
    Основная функция
    '''
    a=0
    while a==0:
        print("A не может быть равным 0")
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    input('Нажмите ENTER для выхода')
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
