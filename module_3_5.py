# Напиши функцию get_multiplied_digits, которая принимает аргумент
# целое число number и подсчитывает произведение цифр этого числа.

def getMultipliedDigits(number):
    digit = 0
    number = int(number)
    digit = digit + (number % 10)
    number //= 10
    if digit == 0:
        return getMultipliedDigits(number)
    if number == 0:
        return digit
    return digit * getMultipliedDigits(number)


print(getMultipliedDigits('40203'))
