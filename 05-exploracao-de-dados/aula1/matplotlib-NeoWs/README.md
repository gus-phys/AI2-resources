# Exercícios


### Análise Gráfica

Para esse conjunto de exercícios vamos utilizar o conjunto de dados
disponibilizado na API da NASA: [NeoWs (Near Earth Object Web Service)](https://api.nasa.gov/)

NeoWs (Near Earth Object Web Service) é um serviço da web RESTful para
informações de asteróides próximos à Terra. Com os NeoWs, um usuário pode:
pesquisar asteróides com base em sua data de aproximação mais próxima à Terra,
pesquisar um asteróide específico com sua identificação de corpo pequeno (small
body ID - NASA JPL), bem como navegar no conjunto de dados geral.


Utilizando a biblioteca [Pandas](https://pandas.pydata.org/) e a biblioteca
[Matplotlib](https://matplotlib.org/), implemente uma função que faça o
seguinte:

1. Criar um dataset que contenha informações sobre os objetos próximos à terra,
   contendo informações das aproximações (esse deve ser um segundo `DataFrame`
   além do que contém informações básicas sobre os objetos);
  * Você deve fazer requisições às primeiras *200* páginas do Serviço;

Em seguida implemente as seguintes visualizações:

* Gráfico de linhas mostrando a quantidade de objetos perigosos que tiveram
  aproximações com a terra entre os anos 2000 e 2021 (agrupe os objetos por ano
  e mostre a média da menor aproximação no período);
* Histograma de tamanhos de objetos que são perigosos sobreposto com Histograma
  de tamanhos de objetos não perigosos;
* Gráfico de bolhas, onde o eixo x seja a data da aproximação, o eixo y seja a
  distância (média) da aproximação, o tamanho do ponto seja o tamanho do objeto
  e a cor do ponto seja a classificação entre **perigoso** e **não perigoso**.
* Gráfico de dispersão entre variáveis:
  * X: tamanho do asteróide e Y: distância mínima de encontro;
  *
