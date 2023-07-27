weight = float(input('insert your weight (kg): '))
height = float(input('insert you height (m): '))
bmi = weight / height ** 2

if bmi < 18.5:
    print(f'your bmi is {bmi} you are underweight')
elif 18.5 < bmi < 23:
    print(f'your bmi is {bmi} you are normal-weight')
elif 23 < bmi < 25:
    print(f'your bmi is {bmi} you are overweight')
elif 25 < bmi < 30:
    print(f'your bmi is {bmi} you are moderately obese')
elif bmi > 30:
    print(f'you bmi is {bmi} you are severely obese')
