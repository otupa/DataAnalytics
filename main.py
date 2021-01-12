import re
import os
import pandas as pd

dir_csv = 'data_csv/'
dir_conversas = 'conversas/'
data_frame = []

class SoftG4:


	# Função usada para filtrar e tratar as informações.
	def filtrar_conversa(self, arg):

		# Separa apenas as informações desejadas
		data = re.findall(r"\d+/\d+/\d+", arg) 
		hora = re.findall(r"\d+\:\d+", arg)
		valor = re.findall(r"\d+\sreais", arg)
		r = [data, hora, valor]

		# Remove caracteres indesejados
		[r[i] is j[0].replace(',','').replace('!','').replace('.','') for i, j in enumerate(r)]

		# Incere os dados em uma lista usada pelo Pandas
		data_frame.append(r)

	def filtrar(self, file):
		
		# Abre a conversa e cria uma lista que separa cada linha.
		conversa = open(dir_conversas+file, 'r', encoding = 'utf-8').read().splitlines()

		# Captura o nome que será usado para salvar o arquivo
		nome_csv = os.path.basename(dir_conversas+file)[:-4][25:]

		# Filtra apenas as mensagens com G4 MOBILE.
		data_conversa_mobile = [linha for linha in conversa if 'G4 MOBILE:' in linha]

		# Filtra apenas as mensagens com reais.
		data_conversa_reais = [linha for linha in data_conversa_mobile if 'reais' in linha]


		print(data_conversa_reais)
		# Estrutura de laço que invoca a função filtrar.
		[self.filtrar_conversa(str(i)) for i in data_conversa_reais]

		# Cria e salva um DataFrame Pandas em um arquico csv.
		df = pd.DataFrame(data_frame).to_csv(dir_csv+nome_csv+'.csv', header=['data', 'hora', 'valor'], encoding='utf-8', index=False)
		data_frame.clear() #Fecha o DataFrame

	def execute_csv(self):
		diretorio = os.listdir(dir_conversas)
		[self.filtrar(file) for file in diretorio]
		
		


if __name__ == '__main__':
	soft = SoftG4()
	soft.execute_csv()