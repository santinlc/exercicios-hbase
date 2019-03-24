#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:28:28 2019

@author: leticia
"""

from extracao import Extracao
from gerador import Gerador
import configparser
import os

def get_configuracoes(nome_secao):
    config = configparser.RawConfigParser()
    config.read('script.ini')
    return dict(config.items(nome_secao))


path = "./outputs"

try:  
    if os.path.exists(path):
        print("Dirtórios %s já criado" % path)
    else:
        os.mkdir(path)
except OSError:  
    print ("Falha ao criar o diretório %s " % path)
    
configuracoes_extracao = get_configuracoes('configs_extracao')
ext = Extracao(configuracoes_extracao)
ext.executar()

configuracoes_gerador = get_configuracoes('configs_popular_tabela')
ger = Gerador(configuracoes_gerador)
ger.executar()

