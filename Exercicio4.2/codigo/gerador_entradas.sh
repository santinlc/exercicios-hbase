#!/bin/bash
export valoresPlacas=(A B C D E F G H I J K L 1 2 3 4 5 6 7 8 9 0)
export tipos=(U T C B)
export nacionalidades=("BR" "EN" "GB" "PT")
export padraoPlacas=(${valoresPlacas[@]} ${numeros[@]})
export padraoTipos=(${tipos[@]})
export padraoNacionalidades=(${nacionalidades[@]})
export permutacaoPlaca=$((${#valoresPlacas[@]}+${#numeros[@]}))
export permutacaoTipo=$((${#tipos[@]}))
export permutacaoNacionalidades=$((${#nacionalidades[@]}))
quantidadePlacas=$1


         
for((placa=1;placa <=$quantidadePlacas;placa++)) 
do
	valorAtual="${padraoNacionalidades[$(((RANDOM%$(($permutacaoNacionalidades)))))]}"
	valorAtual=$valorAtual${padraoTipos[$(((RANDOM%$(($permutacaoTipo)))))]}
	for (( i=1; i<=4; i++ ))
		do
			valorAtual="$valorAtual${padraoPlacas[$(((RANDOM%$(($permutacaoPlaca)))))]}" ;
		done
	echo "$valorAtual$(( $RANDOM % 89 + 10))$(( $RANDOM % 89 +10 ))" >> "../entradas.txt"
done
echo
