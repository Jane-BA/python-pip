'''
Juego de piedra, papel o tijera......
'''
import random

### .... ELECCION .... ###
def chooses():
    options = ('piedra', 'papel', 'tijera')
### Eleccion Usurario
    user = input("piedra, papel o tijera ?  ")
    user = user.lower()
    if not user in options:
        print('Opcion no valida')
        return None, None

### Eleccion Maquina
    machine = random.choice(options)

    print('😁 = ', user)
    print('🤖 = ', machine)
    return user, machine

### .... REGLAS .... ###
def rules(user, machine, user_Wins, machine_Wins):
#Empate
    if user == machine:
        print("Empate")

#Piedra
    elif user == 'piedra':
        if machine == 'papel':
            print("win MACHINE 🤖🤖🤖")
            machine_Wins += 1
            print('MACHINE: ', machine_Wins)
        else:
            print("win USER 😁😁😁")
            user_Wins += 1
            print('USER: ', user_Wins)

#Papel
    elif user == 'papel':
        if machine == 'tijera':
            print("win MACHINE 🤖🤖🤖")
            machine_Wins += 1
            print('MACHINE: ', machine_Wins)
        else:
            print("win USER 😁😁😁")
            user_Wins += 1
            print('USER: ', user_Wins)

#Tijera
    elif user == 'tijera':
        if machine == 'piedra':
            print("win MACHINE 🤖🤖🤖")
            machine_Wins += 1
            print('MACHINE: ', machine_Wins)
        else:
            print("win USER 😁😁😁")
            user_Wins += 1
            print('USER: ', user_Wins)
    return user_Wins, machine_Wins

### .... GANADOR .... ###
def win(user_Wins, machine_Wins):
    if machine_Wins == 2:
        print('*' * 10)
        print('¡¡¡ MACHINE WIN !!!')
        print('🤖 ', machine_Wins, '😁 ', user_Wins)
        exit()

    if user_Wins == 2:
        print('*' * 10)
        print('¡¡¡ USER WIN !!!')
        print('😁 ', user_Wins, '🤖 ', machine_Wins, )
        exit()

### .... CORRELA !!! .... ###
def game():
    machine_Wins = 0
    user_Wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        rounds += 1

        user, machine = chooses()
        
        user_Wins, machine_Wins = rules(user, machine, user_Wins, machine_Wins)
        win(user_Wins, machine_Wins)

game()