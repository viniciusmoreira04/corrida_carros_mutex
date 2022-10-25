#Aluno: Vinícius de Oliveira Moreira | Matrícula:497533   -   Corrida de carros utilizando mutex.
import threading, time, random                   #Importando as bibliotecas
 
mutex = threading.Lock()
class Thread1(threading.Thread):                 #Criando uma classe chamada Thread1
	def run(self):
		global mutex                             #Definindo mutex global
		print ("O primeiro carro está parado.")
		time.sleep(random.randint(1, 5))
		print("O primeiro carro terminou a viagem.")
		mutex.release()                           #Altera o estado para desbloqueado 
 
class Thread2(threading.Thread):                #Criando uma classe chamada Thread2
	def run(self):
		global mutex                            #Definindo mutex global
		print ("O segundo carro está parado.")
		time.sleep(random.randint(1, 5))
		mutex.acquire()                         #Altera o estado para bloqueado
		print("O segundo carro terminou a viagem.")
  
mutex.acquire()
t1 = Thread1()
t2 = Thread2()
t1.start()                                  #Iniciando a thread 1
t2.start()                                  #Iniciando a thread 2