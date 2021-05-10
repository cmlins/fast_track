#! /bin/bash


#    | |        estamos customizando a saída dos processos para termos
#    | |        somente o valor do pid, além disso estamos redirecionando
#    | |        essa saída para termos as 11 primeiras linhas dos processos
#  __| |__      (uma será o cabeçalho PID) e as outras serão os 10 processos. 
#  \    /       Feito isso, estamos redirecionando a saída para o grep que irá 
#   \  /        trazer somente as linhas que contém números
#    \/ 
processos=$(ps -e -o pid --sort -size | head -n 11 | grep [0-9])
for pid in $processos
do
    nome_processo=$(ps 0p $pid -o comm=)
    echo -n $(date +%F,%H:%M:%S, ) >> $nome_processo.log
done


# Quando usamos o símbolo >arquivo.txt estamos escrevendo as informações em um arquivo. 
# Se esse arquivo tiver algum conteúdo todo ele será perdido, 
# caso o comando seja executado novamente. Como esse comando foi executado duas vezes, 
# na primeira vez teríamos como resultado no arquivo.txt o nome teste e ao executar novamente esse comando, 
# o resultado anterior será perdido e estaremos reescrevendo o conteúdo novamente com o nome teste. Com isso, 
# teremos no final somente o nome teste escrito uma vez. 
# Já o símbolo >> irá juntar a informação com o conteúdo pré existente no arquivo.txt, como o comando foi 
# executado duas vezes, teremos o nome teste escrito duas vezes.


# -n não quebra linha