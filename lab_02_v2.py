from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 6, 6)
    c = Circle("зеленого", 6)
    s = Square("красного", 6)
    print(r)
    print(c)
    print(s)
    input('Нажмите ENTER для выхода')

if __name__ == "__main__":
    main()
