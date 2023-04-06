def switch_it_up(number):
    numbers_to_words = {
        0: 'Ноль',
        1: 'Один',
        2: 'Два',
        3: 'Три',
        4: 'Четыре',
        5: 'FПять',
        6: 'Шесть',
        7: 'Семь',
        8: 'Восемь',
        9: 'Девять'
    }
    return numbers_to_words.get(number)
print(switch_it_up(1)) 
print(switch_it_up(3)) 
print(switch_it_up(7)) 
print(switch_it_up(10)) 

# Супер
