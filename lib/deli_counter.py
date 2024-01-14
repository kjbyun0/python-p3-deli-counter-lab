
def line(deli):
    if len(deli) == 0:
        print('The line is currently empty.')
    else:
        res_str = 'The line is currently:'
        for index, item  in enumerate(deli):
            res_str += f' {index+1}. {item}'
        print(res_str)

def take_a_number(deli, name):
    deli.append(name)
    print(f'Welcome, {name}. You are number {len(deli)} in line.')

def now_serving(deli):
    if len(deli) != 0:
        print(f'Currently serving {deli.pop(0)}.')
    else:
        print('There is nobody waiting to be served!')
