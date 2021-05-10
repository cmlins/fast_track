#! /bin/bash
CAMINHO_IMAGENS=~/Downloads/imagens-livros

# for [variável] in $@
# do
#     convert $CAMINHO_IMAGENS/$[variável].jpg $CAMINHO_IMAGENS/$[variável].png
# done

converte_imagem(){
cd ~/Downloads/imagens-livros
if [ ! -d png]
then 
    mkdir png
fi

for imagem in *.jpg
do
    local imagem_sem_extensao=$(ls $imagem | awk -F. '{ print $1 }')
    convert $imagem_sem_extensao.jpg png/$imagem_sem_extensao.png
done    
}

# Os descritores de arquivos são indicadores utilizados para acessar um arquivo ou
# fluxos padrões como entrada, saída, e mensagens de erros. Esses fluxos padrões de 
# entrada, saída e mensagens de erro podem ser acessados pelos descritores 0,1 e 2 respectivamente.

converte_imagem 2>erros.txt
if [ $? -eq 0 ]
then
    echo "Conversão realizada com sucesso"
else
    echo "Houve uma falha no processo"
fi



