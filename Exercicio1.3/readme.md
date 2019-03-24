```
% Universidade Positivo - Especialização Data Science e Big Data
% Hbase 
% LETICIA DE CASSIA SANTIN
% 22/03/2019
```

/****** Exercício 1.3 ********/

## Modelagem 1, utilizando 3 modelos de dados

##### Mapeamento dos dados com família de coluna por sexo:
| RowKey | ID_EMP | Column  | Value                    |
|--------|--------|---------|--------------------------|
| Family |  M     |  NOME   | José                     |
|        | F      |  SOBREN | da Silva                 |
|        |        | RG      | 24535357                 |
|        |        | DT_NASC | 25/02/70                 |
|        |        | ENDER   | Rua Floriano Peixoto, 25 |
|        |        | SAL     | 7000                     |
|        |        | DEPTO   | 1                        |
|        |        | ID_GER  | -                        |

##### Mapeamento dos dados com família de coluna por departamento:
| RowKey | ID_EMP | Column  | Value                    |
|--------|--------|---------|--------------------------|
| Family |   D1   |  NOME   | José                     |
|        | D3     |  SOBREN | da Silva                 |
|        | D4     | RG      | 24535357                 |
|        |        | DT_NASC | 25/02/70                 |
|        |        | ENDER   | Rua Floriano Peixoto, 25 |
|        |        |  SEXO   | M                        |
|        |        | SAL     | 7000                     |
|        |        | ID_GER  |                          |



##### Mapeamento dos dados com família de coluna por ID do gerente:
| RowKey | ID_EMP    | Column  | Value                    |
|--------|-----------|---------|--------------------------|
| Family |   17206-2 |  NOME   | José                     |
|        | 12584-7   |  SOBREN | da Silva                 |
|        | 16764-5   | RG      | 24535357                 |
|        |  -        | DT_NASC | 25/02/70                 |
|        |           | ENDER   | Rua Floriano Peixoto, 25 |
|        |           |  SEXO   | M                        |
|        |           | SAL     | 7000                     |
|        |           | DEPTO   |  1                       |




### Criar e popular a tabela 
Script para popular o banco está em: <code>codigo/popular_modelo1.txt</code>


## Modelagem 2, utilizando 1 modelo de dados

##### Mapeamento dos dados com família de coluna por sexo,depto e ID do gerente:
| RowKey | ID_EMP         | Column     | Value                    |
|--------|----------------|------------|--------------------------|
| Family |   SEXO-M       |  NOME      | José                     |
|        | SEXO-F         |  SOBREN    | da Silva                 |
|        | DEPTO-1        | RG         | 24535357                 |
|        |   DEPTO-3      | DT_NASC    | 25/02/70                 |
|        | DEPTO-4        | ENDER      | Rua Floriano Peixoto, 25 |
|        | ID_GER--       |  SEXO      | M                        |
|        | ID_GER-17206-2 | SAL        | 7000                     |
|        | ID_GER-12584-7 | DEPTO      | 1                        |
|        | ID_GER-16764-5 | ID_GERENTE |   -                      |

### Criar e popular a tabela 
Script para popular o banco está em: <code>codigo/popular_modelo2.txt</code>
