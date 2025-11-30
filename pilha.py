class Pilha:
    TAM_max = 1000
    def __init__( self):
        self.__valores =[0]*Pilha.TAM_max
        self.__topo = -1


    #b) 
    def set_valores(self, valores):
        self. __valores = valores
   
    def get_valores(self):
        return self.__valores
    
    def set_topo(self, topo):
        self. __topo = topo
    
    def get_topo(self):
        return self.__topo

    #c)
    def empty(self):
        if self.__topo ==  -1:
            return 1
        return 0
    
    #d)
    def is_full(self):
        return self.__topo == Pilha.TAM_max -1
    
    def push(self, valor):
        if self.is_full():
            print("Erro: A pilha está cheia. Não é possível inserir.")
            return False
        
        self.__topo+=1

        self.__valores[self.__topo] = valor
        return True
    #e)
    def push2(self, num:int):
         i = 0
         espaco_disponivel = Pilha.TAM_max - (self.__topo+1)
         if num > espaco_disponivel:
            print(f"Erro: Espaço insuficiente. Capacidade máxima: {Pilha.TAM_max}. Espaço disponível: {espaco_disponivel}.")
            return 0

         valores_inserir = []
    
         for i in range(num):
            elemento = int(input("elemento : " ))
            valores_inserir.append(elemento)
         
         elementos_inseridos = 0
        #empilha
         for valor in valores_inserir:
            self.__topo +=1
            self.__valores[self.__topo] = valor
            elementos_inseridos +=1

         print(f"{elementos_inseridos} elementos inseridos com sucesso.")
         return elementos_inseridos
        
    def push3(self, outra_pilha):
        base_ao_topo = outra_pilha.__valores[:outra_pilha.__topo +1]

        elementos_inseridos =0
        for valor in base_ao_topo:
            sucesso = self.push(valor)

            if not sucesso:
                print(f"Empilhamento interrompido. A pilha atingiu o limite de {self.TAM_max}.")
                break

            elementos_inseridos +=1
            print(f"{elementos_inseridos} elementos foram transferidos.")
        return elementos_inseridos

    def pop(self):
        if self.empty():                                                            #verifica se a pilha esta vazia, e se estiover, mostra o erro
            print("Pilha vazia!")                                                   # nao mostra mais o erro, com "raise IndexError, agora só da um print
            return None
    
        valor = self.__valores[self.__topo]                                         #caso nao esteja vazia, guardamos o valor removido dela
        self.__valores[self.__topo] = None                                          #"limpamos" a regiao de memoria em que ela estava
        self.__topo -= 1                                                            #e decrementamos o topo da pilha
        print(valor)                                                                #retornamos o valor removido
        return valor                                                                #retornando o valor pedido 

    
    # h)
    def pop2(self, n):
        elementos_removidos = 0                                                         # inicializa contador de quantos elementos já foram removidos
        for i in range(n):                                                              # repete a operação de remoção n vezes (tentativa de remover n elementos)
            if self.pop() is not None:                                                  # chama pop() e verifica se realmente removeu um elemento (não retornou None)
                elementos_removidos += 1                                                # se pop() removeu, incrementa o contador de removidos
            else:
                break                                                                   # se pop() retornou None (pilha vazia), interrompe o laço — não há mais o que remover
        return elementos_removidos                                                      # retorna a quantidade efetivamente removida


    #i)
    def top(self):                                                                  #essa é muito auto explicativa mas vamos lá
        if self.empty():                                                            # verifica se a a pilha ta vazia
            print("Pilha vazia!")                                                   #E se tiver mostra 
        return self.__valores[self.__topo]                                          # retorna o elemento do topo     

   #k) essa ja esta implementada de forma natural, pelo programa estar escrito em python

class Principal: 
    def main():
        #from pilha import Pilha
        a,b,c = 10, 20, 30;
        p = Pilha()

        if p.push(a) :
            print("valor inserido :", a)

        if p.push(b) :
            print("valor inserido :", b)

        if p.push(c) :
            print("valor inserido :", c)

        print("O topo e : ", p.top())

        print("POP")
        p.pop() 
        print("POP") 
        p.pop() 

        print("Topo resultante:", p.top())


# Inícia a execução
Principal.main()