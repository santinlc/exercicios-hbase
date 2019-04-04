NOME_TABELA='frota'
NOME_ARQUIVO='../carga.txt'
echo "create '$NOME_TABELA' ,{NAME=> 'T', VERSIONS=>50000},{NAME=> 'U', VERSIONS=>50000},{NAME=> 'C', VERSIONS=>50000},{NAME=> 'B', VERSIONS=>50000}" >> $NOME_ARQUIVO

# Lendo arquivo de entradas
input="../entradas.txt"
while IFS= read -r var
do
  echo "$var"
  tipo=${var:0:1}
  placa=${var:1:4}
  posicaoX=${var:5:2}
  posicaoY=${var:7:2}
  echo "put '$NOME_TABELA','$placa','$tipo:posicao','$posicaoX-$posicaoY'" >> $NOME_ARQUIVO
done < "$input"
