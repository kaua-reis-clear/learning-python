# my_list = [
#     {'first_name': 'Kauã', 'last_name': 'Drar'},
#     {'first_name': 'Cintia', 'last_name': 'Ribeiro'},
#     {'first_name': 'André', 'last_name': 'Luís'},
#     {'first_name': 'Vitória', 'last_name': 'Rossi'},
#     {'first_name': 'João', 'last_name': 'Bosco'},
# ]
# my_list = [4, 32, 1, 34, 5, 6, 6, 21, ]
# my_list.sort(reverse=True)
# sorted(my_list)
my_list = [
    {'first_name': 'Kauã', 'last_name': 'Drar'},
    {'first_name': 'Cintia', 'last_name': 'Ribeiro'},
    {'first_name': 'André', 'last_name': 'Luís'},
    {'first_name': 'Vitória', 'last_name': 'Rossi'},
    {'first_name': 'João', 'last_name': 'Bosco'},
]


def show(my_list):
    for item in my_list:
        print(item)
    print()


l1 = sorted(my_list, key=lambda item: item['first_name'])
l2 = sorted(my_list, key=lambda item: item['last_name'])

show(l1)
show(l2)