# x = float(input('x = '))
# print(f'进行测试，你输入了x = {x:.2f}，测试通过')
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print(f'{y = }')

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area_2 = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'面积: {area}, {area_2}')
else:
    print('不能构成三角形')

