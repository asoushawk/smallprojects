from random import randint
import time
import signal
import os


from inputimeout import inputimeout, TimeoutOccurred

global result
global p
global left1
global left2
global amountoftime
global number1_input


p = 1
a = 0
number = 5


player1numbers = []
player2numbers = []


for _ in range(number):
    randomnumber = randint(0,99)
    player1numbers.append(randomnumber)
   
for _ in range(number):
    randomnumber = randint(0,99)
    player2numbers.append(randomnumber)



left1 = len(player1numbers)
left2 = len(player2numbers)


def gameon2():
    

   global result
   global p
   global left1
   global left2
   global amountoftime
   global number1_input
   global a
   global tempo

   tempo = 10

   for _ in range(number):
         
        tempo = number
        print("Turno", p)
        time.sleep(2)
        print("Player 1's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left1)
        time.sleep(2)
        randomnumber1 = randint(4,9)
        randomnumber2 = randint(4,9)

    
        print("Tempo para responder:", tempo)

        
        
        while tempo > 0:
            
            global randomnumber
            print("Digite o resultado da multiplicação:", randomnumber1, "*", randomnumber2, "\n", "Tempo restante:", tempo)

             
            try:
               
               result1 = inputimeout(prompt="Resultado:", timeout=1)
               break

            
            except TimeoutOccurred:
                 error = 1
                 tempo = tempo - 1 

        if tempo == 0:
          time.sleep(2)
          print("Poxa, acabou o tempo, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player1numbers.append(a)
          left1 = len(player1numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left1)
        
        try:

          result = (float(result1))

        
          if randomnumber1 * randomnumber2 == result:
             time.sleep(2)
             print(":D")
             time.sleep(2)
             player1numbers.pop(a)
             left1 = len(player1numbers)
          if randomnumber1 * randomnumber2 != result:
             time.sleep(2)
             print("Poxa, resposta errada, vc vai ter que acertar uma vez a mais")
             randomnumber = randint(0,100)
             player1numbers.append(a)
             left1 = len(player1numbers)
             time.sleep(2)
             print("Acertos restantes para vencer:", left1)
        except:
          pass     
        
        if left1 == 0:
          print("Jogador 1 venceu!!")
          quit()


        
         
     #jogador 2

      
        print("Turno", p)
        time.sleep(2)
        print("Player 2's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left2)
        time.sleep(2)
        randomnumber1 = randint(4,9)
        randomnumber2 = randint(4,9)

        tempo = number

        print("Tempo para responder:", tempo)


        
        while tempo > 0:
            
            
            print("Digite o resultado da multiplicação:", randomnumber1, "*", randomnumber2, "\n", "Tempo restante:", tempo)

             
            try:
               
               result1 = inputimeout(prompt="Resultado:", timeout=1)
               break

            
            except TimeoutOccurred:
                 error = 1
                 tempo = tempo - 1 

        if tempo == 0:
          time.sleep(2)
          print("Poxa, acabou o tempo, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player2numbers.append(a)
          left2 = len(player2numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left1)
        
        try:

          result = (float(result1))

        
          if randomnumber1 * randomnumber2 == result:
             time.sleep(2)
             print(":D")
             time.sleep(2)
             player2numbers.pop(a)
             left2 = len(player2numbers)
          if randomnumber1 * randomnumber2 != result:
             time.sleep(2)
             print("Poxa, resposta errada, vc vai ter que acertar uma vez a mais")
             randomnumber = randint(0,100)
             player2numbers.append(a)
             left2 = len(player1numbers)
             time.sleep(2)
             print("Acertos restantes para vencer:", left1)
        except:
          pass     
        if left2 == 0:
          print("Jogador número 2 venceu!")
          quit()
           
        p = p + 1
        a = a +1  
        number + 1



print("Jogo da Multiplicação")
time.sleep(1)
print("Configurações")
time.sleep(1)
print("Tempo limite para resposta:")
number = int(input())
print("Número de Jogadores")
time.sleep(1)
njg = input()



def gameon1():

    

   global result
   global p
   global left1
   global left2
   global amountoftime
   global number1_input
   global a
   global tempo

   tempo = 10

   for _ in range(number):
         
        tempo = number
        print("Turno", p)
        time.sleep(2)
        print("Player 1's turn:")
        time.sleep(2)
        print("Acertos restantes para vencer:", left1)
        time.sleep(2)
        randomnumber1 = randint(4,9)
        randomnumber2 = randint(4,9)

    
        print("Tempo para responder:", tempo)

        
        
        while tempo > 0:
            
            global randomnumber
            print("Digite o resultado da multiplicação:", randomnumber1, "*", randomnumber2, "\n", "Tempo restante:", tempo)

             
            try:
               
               result1 = inputimeout(prompt="Resultado:", timeout=1)
               break

            
            except TimeoutOccurred:
                 error = 1
                 tempo = tempo - 1 

        if tempo == 0:
          time.sleep(2)
          print("Poxa, acabou o tempo, vc vai ter que acertar uma vez a mais")
          randomnumber = randint(0,100)
          player1numbers.append(a)
          left1 = len(player1numbers)
          time.sleep(2)
          print("Acertos restantes para vencer:", left1)
        
        try:

          result = (float(result1))

        
          if randomnumber1 * randomnumber2 == result:
             time.sleep(2)
             print(":D")
             time.sleep(2)
             player1numbers.pop(a)
             left1 = len(player1numbers)
          if randomnumber1 * randomnumber2 != result:
             time.sleep(2)
             print("Poxa, resposta errada, vc vai ter que acertar uma vez a mais")
             randomnumber = randint(0,100)
             player1numbers.append(a)
             left1 = len(player1numbers)
             time.sleep(2)
             print("Acertos restantes para vencer:", left1)
        except:
          pass     
        
        if left1 == 0:
          print("Jogador 1 venceu!!")
          quit()

if int(njg) == 1:
  
  gameon1()

if int(njg) == 2:

   gameon2()


