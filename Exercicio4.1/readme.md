```
% Universidade Positivo - Especialização Data Science e Big Data
% Hbase 
% LETICIA DE CASSIA SANTIN
% 29/03/2019
```

/****** Exercício 4.1 ********/

• A empresa X possue uma frota de Taxis/Uber/caminhão/bicicleta 
• Cada individuo possui um gps que envia sua posição a cada segundo. 
• A frota é composta por 10 individuos de cada tipo 
• Os dados enviados para a central contém o seguinte formato:
	---• Placa+PosicaoX+PosiçãoY 
	---• TPPPPXXYY 
• Determinar o esquema 
• Desenvolver o script de carga

## Modelagem 

Mapeamento dos dados com família de coluna pelas colunas U (Uber), T (táxi), C (Caminhão), B (bicicleta):

| RowKey | PPPP | Column  | Value |
|--------|------|---------|-------|
| Family |   U  | posicao | XX-YY |
|        | T    |         |       |
|        | C    |         |       |
|        | B    |         |       |




### Criar e popular a tabela 
Script para criação das entradas, executar o shell, 
<code>codigo/gerador_entradas.sh 
Parâmetro: quantidade de entras a serem geradas</code>

Após gerar os valores de entrada, deve-se executar o código para gerar as chamadas shell para o hbase:
Script para gerar as chamadas ao hbase no hbase está em: <code>codigo/script.sh</code>

SCRIPT PARA CARGA NO HBASE: <code>carga.txt</code>



