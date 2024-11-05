def intro(): 
    print("Загадайте число от 1 до 1000.")

def guess():
    low = 1 
    high = 1000
    while True:
        mid = (low + high) // 2 
        print(f'{low, mid, high}') #нижняя середина верхняя
        response = input(f"Ваше число больше, меньше или равно {mid}? (введите '>', '<' или '='): ")
        if low == mid:
            print(f'Вы сузили границы поиска до одного числа и это число {mid}')
            break 
        if response == '=':
            print(f"Угадано! Ваше число: {mid}")
            break
        elif response == '>': 
            low = mid + 1
        elif response == '<': 
            high = mid - 1
        else: 
            print("Пожалуйста, введите '>', '<' или '='.")

def again():
    while True:
        answer = input('Сыграем еще раз? да/нет: ')
        if answer.lower() == 'да':
            return True
        elif answer.lower() == 'нет':
            print(f'Спасибо за игру.')
            return False
        else:
            print(f'Напишите "да" или "нет".')

def main():
    while True:
        intro()
        guess()
        if not again(): 
            break
    
    
if __name__ == "__main__":
    main()