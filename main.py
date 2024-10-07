import math

def valid_number(text):
    while True:
        try:
            number = float(input(text))
            if number < 0:
                print('Введите число больше 0')
            return (number)
        except ValueError:
            print('Введите число!')
def valid_triangle(a,b,c):
    return a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a)

def type_triangle(a,b,c):
    sides = [a,b,c]
    sides.sort()
    if a == b and b == c:
        return('Равносторонний треугольник')
    elif a == b or b == c and a == c:
        return("Равнобедренный треугольник")
    elif sides[2]**2 == sides[0]**2 + sides[1]**2:
        return('Прямоугольный треугольник')
    elif sides[0]**2 + sides[1]**2 > sides[2]**2:
        return('Остроугольный треугольник')
    else:
        return("Тупоугольный треугольник")


def calculateArea(a, b, c):
  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return(area)


a = valid_number("Введите длину первой стороны треугольника: ")
b = valid_number("Введите длину второй стороны треугольника: ")
c = valid_number("Введите длину третьей стороны треугольника: ")


def all_func(a,b,c):
    if not valid_triangle(a, b, c):
        print("Такой треугольник не существует")
        return('Такой треугольник не существует')
    else:
        triangle = type_triangle(a, b, c)
        area = calculateArea(a, b, c)

        print(f"Вид треугольника: {triangle}")
        print(f"Площадь треугольника: {area:.2f}")
        return(triangle,f'{area:.2f}')

print(all_func(a,b,c))

