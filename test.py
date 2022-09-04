help = """ 
help - Напечатать справку о программе
add - Добавить задачу в список
show - Напечатать все добавленные задачи
exit - Выход из программы
"""
my_task = []
run = True
task_today = []
task_tomorrow = []
task_other = []

while run:
 command = input('Введите команду: ')
 if command == 'help':
    print(help)
 elif command == 'show':
    print(my_task)
 elif command == 'add':
    task = input('Введите задачу: ')
    task_day = input('Введите параметр исполнения задачи: ')
    if task_day == 'Сегодня':
        task_today.append(task_day)
        print('Задача внесена в список', task_today)
    elif task_day == 'Завтра':
        task_tomorrow.append(task)
        print('Задача внесена в список', task_tomorrow)
    elif task_day == 'Иное':
        task_other.append(task)
        print('Задача внесена в список', task_other)
 elif command == 'exit': 
    print('Спасибо за использование')
    break
 else:
    print('Not nown')
    break
print('Повторите снова')



# Заведите 3 списка: today, tomorrow, other (вы можете назвать переменные по-другому).
# Измените блок кода, который выполняет команду add:
# Дополнительно запросите у пользователя дату выполнения задачи.
# В зависимости от введенной даты добавьте задачу в один из списков по следующим правилам:
# Если пользователь ввел "Сегодня", добавьте задачу в список today.
# Если пользователь ввел "Завтра", добавьте задачу в список tomorrow.
# Если пользователь ввел любое другое значение, добавьте задачу в список other.