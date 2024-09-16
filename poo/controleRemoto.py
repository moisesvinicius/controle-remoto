class ControleRemoto:
    def __init__(self, cor, volume=50, ligado=False):
        self.cor = cor
        self.volume = volume
        self.ligado = ligado
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Controle remoto ligado.')
        else:
            print('O controle remoto já está ligado.')
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('Controle remoto desligado.')
        else:
            print('O controle remoto já está desligado.')
        
    def mostrar_cor(self):
        print(f'Cor - {self.cor}')
        
    def mais_volume(self):
        if self.ligado:
            if self.volume < 100:
                self.volume += 1
                print(f'Volume aumentado para {self.volume}')
            else:
                print('Volume já está no máximo.')
        else:
            print('O controle remoto está desligado.')

    def menos_volume(self):
        if self.ligado:
            if self.volume > 0:
                self.volume -= 1
                print(f'Volume diminuído para {self.volume}')
            else:
                print('Volume já está no mínimo.')
        else:
            print('O controle remoto está desligado.')
            
# Instanciando o controle remoto
controle = ControleRemoto('Preto', volume=50, ligado=False)

# Testando os métodos
controle.ligar()
controle.mais_volume()
controle.menos_volume()
controle.mostrar_cor()
controle.desligar()
