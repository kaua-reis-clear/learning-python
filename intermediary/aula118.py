def add_clients(nome, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(nome)
    return my_list


client1 = add_clients('Kauã')
add_clients('Fallen', client1)
add_clients('Art', client1)
client1.append('Kscerato')

client2 = add_clients('Yuurih')
add_clients('Chelo', client2)

client3 = add_clients('Guerri')
add_clients('Sidde', client3)

print(client1)
print(client2)
print(client3)