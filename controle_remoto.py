class ControleRemoto:
	def __init__(self, cor, altura, profundidade, largura):
		self.cor = "preto"
		self.altura = "10cm"
		self.profundidade = "2cm"
		self.largura = "2cm"

	metodos do controle remoto:
		passar canal
		mexer no volume
		abrir netflix
		desligar a tv

class Cliente:
	def __init__(self, nome, email, plano):
		self.nome = nome
		self.email = email
		lista_planos = ["basic", "premium"]
		if plano in lista_planos:
			self.plano = plano
		else:
			raise Exception("Plano inválido")

cliente = Cliente("Lira", "lira@gmail.com", "blabla")
print(cliente)
