from views import *


def main():
    print('1 - CREATE, 2 - LISTING', '3 - RETRIEVE', '4 - UPDATE', '5 - DELETE')
    choice = int(input('action (1,2,3,4,5): '))
    if choice == 1:
        print(create_product())
    elif choice == 4:
        print(update_product())
    elif choice == 5:
        print(delete_product())
    elif choice == 3:
        print(retrieve_product())
    elif choice == 2:
        print(get_data())
        
flag = True
while flag:
    main()
    print()
    continue_ = input('Хотите продолжить работу?(yes/*any_key*)): ')
    print()
    if continue_ == 'yes':
        continue
    else:
        flag = False

