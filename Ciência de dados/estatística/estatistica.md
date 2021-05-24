# ESTATÍSTICA

## Regressão linear
- Correlação de Pearson: 
  - -1 <= p >= 1
  - Não existe causalidade  

## Regressão logística
- -infinito até +infinito

![Regressão linear x Regressão logística](maxresdefault.jpg)

## Árvore de decisão, Random Forest e Gradient Boosting
  ### Árvore de decisão
    - Assertivo
    - Acurado: erram menos
    - Instável: qq mudança pode gerar alteração grande nos resultados
  ### Random Forest
    - comunicação de árvares que são independentes entre si
  ### Gradient Booster
    - árvores sequenciais, uma amostra depende da anterior
    - modelo com acurácia maior
  
## Overfitting
- modelo mt específico
- perde a capacidade de generalizar

## Métricas de avaliação
- matriz de confusão
  - sucesso: false positive e true positive
  - fracasso: true negative e false negative

Decisão:
- **misclassification**
- accuracy
- Precision: qts vc diz q acertou, qts eram certos?
- Recall: qt eu acerto de quem eu realmente quero acertar

Ordenação:
- quartis
- **lift**

Estimativa:
- **ASE**:  average squared error

## Distribuição binomial
- distribuição de Bernoulli: tem 2 possibilidades do evento acontecer
- distribuição binomial: são combinação de Bernoulli, independentes e a probabilidade de acontecer em cada evento é igual


![algoritmos](estatistica.jpg)
