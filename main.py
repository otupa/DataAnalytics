import re
import os
import pandas as pd

class SoftG4:

	dir_csv = 'data_csv/'
	dir_conversas = 'conversas/'
	data_frame = []

	# Função usada para filtrar e tratar as informações.
	def filtrar_conversa(self, arg):

		# Separa apenas as informações desejadas
		data = re.findall(r"\d+/\d+/\d+", arg) 
		hora = re.findall(r"\d+\:\d+", arg)
		valor = re.findall(r"\d+\sreais", arg)
		r = [data, hora, valor]

		# Remove caracteres indesejados
		for i, j in enumerate(r):
			r[i] = j[0].replace(',','').replace('!','').replace('.','')

		# Incere os dados em uma lista usada pelo Pandas
		data_frame.append(r)

	def filtrar(self, file):
		
		# Abre a conversa e cria uma lista que separa cada linha.
		conversa = open(dir_conversas+file, 'r', encoding = 'utf-8').read().splitlines()

		# Captura o nome que será usado para salvar o arquivo
		nome_csv = os.path.basename(dir_conversas+file)[:-4][25:]

		# Filtra apenas as as mensagens desejadas.
		data_conversa = [linha for linha in conversa if 'reais' in linha]

		# Estrutura de laço que invoca a função filtrar.
		filtro = [filtrar_conversa(str(i)) for i in data_conversa]

		# Cria e salva um DataFrame Pandas em um arquico csv.
		df = pd.DataFrame(data_frame).to_csv(dir_csv+nome_csv+'.csv', header=['data', 'hora', 'valor'], encoding='utf-8', index=False)
		data_frame.clear() #Fecha o DataFrame

if __name__ == '__main__':


