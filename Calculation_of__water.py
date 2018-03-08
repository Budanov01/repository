# coding=utf-8
Time = input('расчётое время в минутах ')
water_volume = input('ср.V(л) воды в минуту ')


def calculation_of_water(Time, water_volume):
    if Time < 0 and water_volume < 0:
        return 'Ошибка, значения не могут быть < 0'
    elif Time < 0 or water_volume < 0:
        return 'Ошибка, значение не может быть < 0'
    elif Time - int(Time) > 0 or water_volume - int(water_volume) > 0:
        return 'значения должны быть целочисленными'
    elif Time - int(Time) == 0:
        V = Time * water_volume * 2
        return 'кол-во полулитровых бутылок ' + str(V)


print(calculation_of_water(Time, water_volume))
