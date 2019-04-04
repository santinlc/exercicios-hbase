NOME_TABELA='frota-internacional'
NOME_ARQUIVO='../carga.txt'
echo "create '$NOME_TABELA' ,{NAME=> 'BR', VERSIONS=>50000},{NAME=> 'EN', VERSIONS=>50000},{NAME=> 'GB', VERSIONS=>50000},{NAME=> 'PT', VERSIONS=>50000}" >> $NOME_ARQUIVO

# Lendo arquivo de entradas
input="../entradas.txt"
while IFS= read -r var
do
  echo "$var"
  nacionalidade=${var:0:2}
  tipo=${var:2:1}
  placa=${var:3:4}
  posicaoX=${var:7:2}
  posicaoY=${var:9:2}
  echo "put '$NOME_TABELA','$tipo-$placa','$nacionalidade:posicao','$posicaoX-$posicaoY'" >> $NOME_ARQUIVO
done < "$input"
