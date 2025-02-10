from abc import ABC, abstractmethod
from time import sleep
import itertools
import random
import os
import matplotlib.pyplot as plt


def BaseMachine(ABC):
    @abstractmethod
    def _gen_permutations(self):
        ...

    @abstractmethod
    def _get_final_results(self):
        ...

    @abstractmethod
    def _display(self):
        ...

    @abstractmethod
    def _check_result_user(self):
        ...

    @abstractmethod
    def _update_balance(self):
        ...

    @abstractmethod
    def emojize(self):
        ...

    @abstractmethod
    def gain(self):
        ...

    @abstractmethod
    def gain(self):
        ...

    @abstractmethod
    def play(self, amount_bet, player):
        ...

class Player: 
    def __init__(self, balance=0):
        self.balance = balance
        

class SlotMachine:

    def __init__(self, level = 1, balance = 0):
        self.SIMBOLOS = {
           'face_screaming_in_fear': '1F631',
            'skull':'1F480',
            'happy_face':'1F600',
            'index_pointing_at_the_viewer':'1FAF5',
            'monkey':'1F412'
        }
        self.level = level
        self.permutations = self.gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance


    def gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS:
                permutations.append((i,i,i))
        return permutations
        


    def _get_final_result(self):

        if not hasattr(self, 'permutations'):
            self.permutations = self.gen_permutations()

        result = list(random.choice(self.permutations))

        if len(set(result)) == 3 and random.randint(0,5) >=2:
            result[1] = result [0]

        return result
        
    def _display(self, amount_bet, result, time = 0.1):
        seconds = 2
        
        for i in range(0,int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            os.system('cls')

        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Voce venceu e recebeu: {amount_bet*3}')
        else:
            print('Foi quase! Tente novamente.')

    def _emojize(self,emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16))for code in emojis))
    
    def _check_result_user(self, result):
        x = [result[0] == x for x in result]

        return True if all(x) else False

    def _update_balance(self, amount_bet, result, player : Player): 
        if self._check_result_user(result):
            self.balance -= (amount_bet * 3)
            player.balance += (amount_bet*3)
        else: 
            self.balance += amount_bet
            player.balance -= amount_bet

    def play(self, amount_bet, player: Player):
        result = self._get_final_result()
        #self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)

    @property
    def gain(self):
        return self.initial_balance + self.balance

machine_1 = SlotMachine(level=4)
player_1 = Player()
machine_1.play(15, player_1)

#abaixo é um gráfico disso tudo. 

JOGADORES_POR_DIA = 30
APOSTAS_POR_DIA = 5
DIAS = 5
VALOR_MAXIMO = 200

saldo = []

players = [Player() for i in range(JOGADORES_POR_DIA)]

for i in range(0,DIAS):
    for j in players:
        for k in range(1, random.randint(2, APOSTAS_POR_DIA)):
            machine_1.play(random.randint(5,VALOR_MAXIMO),j)
    saldo.append(machine_1.gain)


plt.figure()

x = [i for i in range(1, DIAS+1)]

plt.plot(x, saldo)
plt.show()

plt.plot([i for i in range(JOGADORES_POR_DIA)], [i.balance for i in players])
plt.grid(True)
plt.show()


