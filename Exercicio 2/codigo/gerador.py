
# coding: utf-8

# ## Script para popular o Hbase
# ### Feito a partir do csv já transformado


import pandas as pd
import csv


# ### Extraindo valores do arquivo de configurações

class Gerador:

	def __init__(self,configuracoes):
        	self.configuracoes = configuracoes

	def executar(self):
		print("Configurações Geracao",self.configuracoes)
		NOME_TABELA = self.configuracoes['nome_tabela']
		NOME_ARQUIVO_SCRIPT = "outputs/"+self.configuracoes['nome_arquivo_script']+"_"+NOME_TABELA+".txt"

		# ## criando a tabela
		df_shorturls = pd.read_csv('outputs/shortulrs_usuarios.csv',dtype=object)

		# ### Pegando a lista com urls únicas para criar as famílias de colunas
		url_unicas = df_shorturls['url'].unique().tolist()
		text_file = open(NOME_ARQUIVO_SCRIPT, "w")
		text_file.write("create '"+NOME_TABELA+"','"+"','".join(url_unicas)+"'\n")
		text_file.close()


		# ### Criando registros

		insert_short_url_df = pd.DataFrame()
		insert_acessos_df = pd.DataFrame()


		insert_short_url_df['script'] = "put '"+NOME_TABELA+"','"+df_shorturls['user_id']+"','"+df_shorturls['url']+":shorturl','"+df_shorturls['short_url']+"'"
		insert_acessos_df['script'] = "put '"+NOME_TABELA+"','"+df_shorturls['user_id']+"','"+df_shorturls['url']+":acessos','"+df_shorturls['acessos']+"'"
		insert_table = insert_short_url_df.append(insert_acessos_df, ignore_index=True)
		insert_table = insert_table.sort_values(by=['script'])


		insert_table.to_csv(NOME_ARQUIVO_SCRIPT, header=None, index=None, mode='a',quoting=csv.QUOTE_NONE,escapechar=' ')
		print("Arquivo com script para popular a tabela em:",NOME_ARQUIVO_SCRIPT)

