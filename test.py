help = """ 
help - Напечатать справку о программе
add - Добавить задачу в список
show - Напечатать все добавленные задачи
"""
my_task =[]

run = True

while run:
 command = input('Введите команду: ')
 if command == 'help':
    print(help)
 elif command == 'show':
    print(my_task)
 elif command == 'add':
    task = input('Введите задачу: ')
    my_task.append(task)
    print('Задача', my_task, 'внесена в список')
 else:
    print('Not nown')
    break
print('Повторите снова')

