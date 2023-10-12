def sea(n: int) -> str:
    match n:
        case 12 | 1 | 2:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Лето"
        case 9 | 10 | 11:
            return "Осень"
        case _:
            return "Неправильный формат"
print(sea(int(input())))

    