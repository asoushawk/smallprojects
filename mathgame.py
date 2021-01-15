from random import randint
import time
import signal
print("Addition Game")
global result
global p
global left1
global left2
p = 1
a = 0
number = 5
player1numbers = []
player2numbers = []

for _ in range(number):
    randomnumber = randint(1500,3333)
    player1numbers.append(randomnumber)
   
for _ in range(number):
    randomnumber = randint(0,100)
    player2numbers.append(randomnumber)



left1 = len(player1numbers)
left2 = len(player2numbers)
def gameon():
    

    global left1
    global left2
    global p
    global a
    for _ in range(number):

        print("Turno", p)
        time.sleep(2)
        print("Player 1's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left1)
        time.sleep(2)
        print("Digite dois números cuja soma resulte em:")
        print(player1numbers[a])

        
        print("Número 1:")
        number1_input = input()
        print("Número 2:")
        number2_input = input()
        result1 = int(number1_input)
        result2 = int(number2_input)
    
        if result1 + result2 == player1numbers[a]:
         time.sleep(2)
         print(":D")
         time.sleep(2)
         player1numbers.pop(a)
         left1 = len(player1numbers)

         print("Acertos restantes para vencer:", left1)
        else:
          time.sleep(2)
          print("Poxa, boa sorte na próxima, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player1numbers.pop(randomnumber)
          left1 = len(player1numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left1)
        if left1 == 0:
          print("O Jogador número 1 venceu!! :D")
          quit()
          

     #jogador 2

      
        time.sleep(2)
        print("Player 2's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left2)
        time.sleep(2)
        print("Digite dois números cuja soma resulte em:")
        time.sleep(2)
        print(player2numbers[a])

        
        print("Número 1:")
        time.sleep(2)
        number1_input = input()
        print("Número 2:")
        number2_input = input()
        result1 = int(number1_input)
        result2 = int(number2_input)
        
        if result1 + result2 == player2numbers[a]:
          time.sleep(2)
          print(":D")
          player2numbers.pop(a)
          time.sleep(2)
          print(player2numbers)
          left2 = len(player2numbers)
          print("Acertos restantes para vencer:", left2)
        else:
          time.sleep(2)
          print("Poxa, boa sorte na próxima, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player2numbers.append(randomnumber)
          left2 = len(player2numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left2)     
        if left2 == 0:
          print("Jogador número 2 venceu!")
          quit()
           
        p = p + 1
        a = a +1  
      


def gameon2():
    

    global left1
    global left2
    global p
    global a
    for _ in range(number):

        print("Turno", p)
        time.sleep(2)
        print("Player 1's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left1)
        time.sleep(2)
        print("Digite o resultado da multiplicação:")
        randomnumber1 = randint(1,9)
        randomnumber2 = randint(1,9)
        print(randomnumber1, "*", randomnumber2)
        print("Resultado:")
        number1_input = input()
        result1 = int(number1_input)
    
        if randomnumber1 * randomnumber2 == result1:
         time.sleep(2)
         print(":D")
         time.sleep(2)
         player1numbers.pop(a)
         left1 = len(player1numbers)

         print("Acertos restantes para vencer:", left1)
        else:
          time.sleep(2)
          print("Poxa, boa sorte na próxima, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player1numbers.pop(a)
          left1 = len(player1numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left1)
        if left1 == 0:
          print("O Jogador número 1 venceu!! :D")
          quit()
          

     #jogador 2

      
        time.sleep(2)
        print("Player 2's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left2)
        time.sleep(2)
        print("Digite o resultado da multiplicação:")
        randomnumber1 = randint(1,9)
        randomnumber2 = randint(1,9)
        print(randomnumber1, "*", randomnumber2)
        print("Resultado:")
        number1_input = input()
        result1 = int(number1_input)
    
        if randomnumber1 * randomnumber2 == result1:
         time.sleep(2)
         print(":D")
         time.sleep(2)
         player2numbers.pop(a)
         left2 = len(player2numbers)

         print("Acertos restantes para vencer:", left2)
        else:
          time.sleep(2)
          print("Poxa, boa sorte na próxima, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player2numbers.append(randomnumber)
          left2 = len(player2numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left2)     
        if left2 == 0:
          print("Jogador número 2 venceu!")
          quit()
           
        p = p + 1
        a = a +1  
    


print("Digite 1 para Adição e 2 para Multiplicação:")
choice = input()
if choice == "1":
  gameon()
elif choice == "2":
  gameon2()  

