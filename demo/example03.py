height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')

if bmi < 18.5: 
    print(f'你的体重过轻！bmi = {bmi:.1f}')
elif bmi < 24: # 18.5 <= bmi < 24
    print(f'你的身材很棒！bmi = {bmi:.1f}')
elif bmi < 27: # 24 <= bmi < 27
    print(f'你的体重过重！bmi = {bmi:.1f}')
elif bmi < 30: # 27 <= bmi < 30
    print(f'你已轻度肥胖！bmi = {bmi:.1f}')
elif bmi < 35: # 30 <= bmi < 35
    print(f'你已中度肥胖！bmi = {bmi:.1f}')
else: # bmi >= 35
    print(f'你已重度肥胖！bmi = {bmi:.1f}')
