def quarter_of(month):
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    else:
        return 4
print(quarter_of(2)) # 1
print(quarter_of(6)) # 2
print(quarter_of(11)) # 4
print(quarter_of(13)) # None

# Хорошо, вот немного иная запись
def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
