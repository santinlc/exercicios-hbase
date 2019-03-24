
# coding: utf-8

# ## Script para fazer a extração dos dados do banco e gerar csv com as informações necessárias
# ### <b>Script fake</b> para extração. Valores gerados aleatoriamente


import random
import hashlib
import pandas as pd
import configparser



class Extracao:
    
    def __init__(self,configuracoes):
        self.configuracoes = configuracoes

    # RANDOMIZA A ESCOLHA DAS URLS DO USUARIO
    def escolher_urls(self,qtde):
        if qtde > len(self.LISTA_URLS):
            qtde = len(self.LISTA_URLS)
        random.shuffle(self.LISTA_URLS)
        return self.LISTA_URLS[:qtde]


    ''' 
    CONVERTE O NUMERO DE USUÁRIO CONCATENADO COM A URL EM UM NÚMERO INTEIRO DE 8 DIGITOS 
    PARA QUE FIQUE ÚNICA 
    '''
    def gerar_short_url(self,user_id, url):
        s = str(user_id)+url
        hash_s = (int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8)
        return "www.myshorturl/"+str(hash_s)


    def get_qtde_urls_visitadas(self):
        return random.randint(1,len(self.LISTA_URLS))

    ##GERANDO LISTA DE COM OS USUARIO E SHORTURLS
    def executar(self):
        lista_acessos = []
        print("Configurações Extração",self.configuracoes)
        QUANTIDADE_USUARIOS = int(self.configuracoes['qtde_usuarios'])
        self.LISTA_URLS = self.configuracoes['lista_urls'].split(',')
        MAX_RANDOM_ACESSO = int(self.configuracoes['maximo_random_acessos'])
        for x in range(1,QUANTIDADE_USUARIOS+1):
            user_id = "user_"+str(x)
            lista_acessos_usuario = []
            lista_urls_usuario = self.escolher_urls(self.get_qtde_urls_visitadas())
            for url_usuario in lista_urls_usuario:
                short_url = self.gerar_short_url(user_id,url_usuario)
                qtde_acessos = str(random.randint(0,MAX_RANDOM_ACESSO))
                lista_acessos_usuario.append({'user_id':user_id,'url':url_usuario,'short_url':short_url,'acessos':qtde_acessos})
            lista_acessos = lista_acessos+lista_acessos_usuario
        df_salvar = pd.DataFrame(lista_acessos)    
        df_salvar.to_csv('outputs/shortulrs_usuarios.csv',index=False)    
