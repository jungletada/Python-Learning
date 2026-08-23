import math


# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print(f'周长: {perimeter:.5f}')
# print(f'面积: {area:.5f}')

year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')