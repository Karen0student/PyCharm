hours = int(input())
minutes = int(input())
add_minutes = int(input())

minutes += add_minutes
res_minutes = minutes // 60
hours += res_minutes
print_minutes = minutes % 60
print_hours = hours % 24

if print_hours < 10:
    print(f'0{str(print_hours)}:', end="")
else:
    print(f'{str(print_hours)}:', end="")
    
if print_minutes < 10:
    print(f'0{str(print_minutes)}')
else:
    print(f'{str(print_minutes)}')
