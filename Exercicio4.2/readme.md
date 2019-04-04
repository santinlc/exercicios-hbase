```
% Universidade Positivo - Especialização Data Science e Big Data
% Hbase 
% LETICIA DE CASSIA SANTIN
% 29/03/2019
```

/****** Exercício 4.2 ********/

• A empresa X possui uma frota de Taxis/Uber/caminhão/bicicleta 
• E se a empresa se internacionalizar? BR, GB, PT – Se as placas puderem se repetir? 
• E se a empresa abrir outras filiais? 
• A frota é composta por 10 individuos de cada tipo 
• Os dados enviados para a central contém o seguinte formato 
	--- • Placa+PosicaoX+PosiçãoY 
	--- • NNTPPPPXXYY 
• Determinar o esquema 
• Desenvolver o script de carga

## Modelagem 

Mapeamento dos dados com família de coluna pelas colunas U (Uber), T (táxi), C (Caminhão), B (bicicleta):

| RowKey |  T-PPPP | Column  | Value |
|--------|---------|---------|-------|
| Family |   NN    | posicao | XX-YY |



### Criar e popular a tabela 
Script para criação das entradas, executar o shell, 
<code>codigo/gerador_entradas.sh 
Parâmetro: quantidade de entras a serem geradas</code>

Após gerar os valores de entrada, deve-se executar o código para gerar as chamadas shell para o hbase:
Script para gerar as chamadas ao hbase no hbase está em: <code>codigo/script.sh</code>

SCRIPT PARA CARGA NO HBASE: <code>carga.txt</code>



