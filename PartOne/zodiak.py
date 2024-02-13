"""Зодиак"""

zodiak_list = ['Обезьяна',
               'Петух',
               'Собака',
               'Свинья',
               'Крыса',
               'Бык',
               'Тигр',
               'Заяц',
               'Дракон',
               'Змея',
               'Лошадь',
               'Овца']

num_of_year = int(input())
indx = num_of_year % 12

print(zodiak_list[indx])
