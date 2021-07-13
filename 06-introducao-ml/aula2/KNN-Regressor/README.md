# Exercícios


### Primeiro algoritmo de regressão

Para esse conjunto de exercícios vamos utilizar o conjunto de dados sobre o
consumo de cerveja na cidade de São Paulo ([Link](https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo)).
Esse dataset contém informações a respeito da temperatura, precipitação e a
quantidade de cerveja consumida na cidade de São Paulo.


Utilizando a biblioteca [Pandas](https://pandas.pydata.org/) e a biblioteca
[Numpy](https://numpy.org/), implemente as seguintes funcionalidades:

1. Implementar o [KNN
   Regressor](https://towardsdatascience.com/the-basics-knn-for-classification-and-regression-c1e8a6c955)
   onde o valor predito de um exemplo desconhecido é dado como a média dos
   valores dos `K` pontos mais próximos. 
1. Faça a avaliação da qualidade das predições realizadas pelo algoritmo
   utilizando o [erro quadrado médio](https://en.wikipedia.org/wiki/Mean_squared_error)
   (*mean squared error* - MSE) como métrica. 
  * Para realizar essa avaliação faça a separação do dataset em uma partição de
    treino e uma para a validação.
1. Avalie o impacto do tamanho do `K` no algoritmo. Crie plots que mostrem o
   valor médio do MSE vs. o valor de `K` escolhido.
  * O que acontece quando o valor de `K` se torna suficientemente grande?
1. Nesse algoritmo, precisamos verificar a proximidade entre o novo ponto e
   todos os pontos no dataset. Para datasets grandes, essa tarefa se torna
   muito lenta. 
  * Faça um pré-processamento no dataset fazendo a separação de grupos
    utilizando o algoritmo K-means. 
      * Esse pré-processamento tem algum impacto no tempo de predição? 
      * E quanto a avaliação da predição? Essa estratégia causa algum impacto
        no valor da métrica escolhida (MSE)?
   
