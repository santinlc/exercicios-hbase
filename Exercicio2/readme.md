```
% Universidade Positivo - Especialização Data Science e Big Data
% Hbase 
% LETICIA DE CASSIA SANTIN
% 22/03/2019
```

/****** Exercício 2 ********/

Objetivos:
– Dado determinada url, devolver a shortUrl
– Dado determinado usuário, devolver todas Url's e shortUrl's
– Dado determinado usuário, devolver todas Url's e shortUrl's e os acessos realizados
• De-normalizar
• Definir as Column Families
• Definir as Row Keys
• Criar a tbl
• Popular com pelo menos 40 “linhas”

### Definições
#### Mapeamento dos dados:
| <br>RowKey</b> | user_id | Column   | Value      |
|--------|---------|----------|------------|
| <b>Family</b> | 'urls'     | shorturl | bit.ly/123 |
|        |         | acessos  | 25         |

### Criar e popular a tabela 
Dados utilizados, criado via script em: <code>outputs/shortulrs_usuarios.csv</code>
Saída do script utilizado se encontra em 
<code>outputs/script_hbase_popular_tabela_ex2_shorturl.txt</code>

### Consultas
#### – Dado determinada usuário e uma url, devolver a shortUrl
<code>hbase(main):002:0> get 'tabela_ex2_shorturl', 'user_9', 'www.youtube.com:shorturl'</code>
Resultado
<code>COLUMN            CELL                                                                                   
		 www.youtube.com:shorturl        timestamp=1553271797923, value=www.myshorturl/23042910                                     
		1 row(s) in 0.3580 seconds</code>
</code>
#### – Dado determinado usuário, devolver todas Url ́s e shortUrl ́s
#### – Dado determinado usuário, devolver todas Url ́s e shortUrl ́s e os acessos realizados
Mapeamento realizado, onde uma consulta responde as duas questões
<code>	hbase(main):003:0> get 'tabela_ex2_shorturl','user_14'</code>
Resposta
<code>COLUMN                 CELL                                                                                       
 www.copel.com:acessos           timestamp=1553271796737, value=194                                                         
 www.copel.com:shorturl          timestamp=1553271796751, value=www.myshorturl/43653389                                     
 www.vk.com:acessos              timestamp=1553271796755, value=388                                                         
 www.vk.com:shorturl             timestamp=1553271796765, value=www.myshorturl/16506                                        
4 row(s) in 0.2650 seconds
</code>
	

