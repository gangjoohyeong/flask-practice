def type_checker(func):
    def wrapper(digit1, digit2):
        # digit1, digit2 모두 정수형일 때 func 리턴
        if type(digit1) == int and type(digit2) == int:
            return func(digit1, digit2)
        else:
            # 하나라도 정수형이 아니면 메시지 출력후 리턴
            print('only integer support')
            return
    return wrapper

@type_checker
def divide(digit1, digit2):
    return digit1 / digit2

@type_checker
def mul(digit1, digit2):
    return digit1 * digit2


print(divide(10, 2))
print(mul(10, 2))