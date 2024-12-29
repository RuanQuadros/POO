class Registro_passagem:
    def __init__(self,nome,destino,valor,hora,saida):
        self.nome = nome
        self.destino = destino
        self.valor = valor
        self.hora = hora
        self.saida = saida

        
    def informacoes(self):
        print(f'Passageiro: {self.nome}')
        print(f'Destino da viagem: {self.destino}')
        print(f'Valor da passagem: {self.valor}')
        print(f'Horario de compra da passagem: {self.hora}')
        print(f'Saida do avião: {self.saida}')