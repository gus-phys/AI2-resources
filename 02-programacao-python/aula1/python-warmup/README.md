# Exercícios

### Python warmup

Para esse conjunto de exercícios vamos utilizar o dataset [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)


Os conjuntos de dados do MovieLens foram coletados pelo GroupLens Research Project na Universidade de Minnesota.
 
Este conjunto de dados consiste em:
* 100.000 classificações (1-5) de 943 usuários em 1.682 filmes.
* Cada usuário classificou pelo menos 20 filmes.
* Informações demográficas simples para os usuários (idade, sexo, ocupação, CEP)

Os dados foram coletados por meio do site MovieLens (movielens.umn.edu) durante o período de sete meses a partir de 19 de setembro, 1997 a 22 de abril de 1998. Estes dados foram limpos - usuários que tiveram menos de 20 avaliações ou não tiveram dados demográficos completos informações foram removidas deste conjunto de dados. Descrições detalhadas de o arquivo de dados pode ser encontrado no final deste arquivo.

Utilizando esse Dataset responda as seguintes perguntas. Você deverá utilizar somente as bibliotecas padrões do python, i.e., nenhuma nova biblioteca deve ser adicionada para implementar suas soluções (**isso é um warmup de python!**)
#### Encontrar:
1. O(s) usuário(s) mais crítico(s) na avaliação de filmes.
    * Encontrar aquele id cujas notas são, em média, as menores;
1. O(s) filme(s) mais mal avaliado(s) pelos usuários.
1. O(s) filme(s) mais bem avaliado(s) pelos usuários.
1. Média de avaliação para cada gênero de filmes;
1. Avaliação média de filmes por ano. 
    * Listar qual o ano com a melhor média de avaliação de filmes;
1. Qual a ocupação mais propensa a dar más avaliações a filmes;
    * Encontrar a média de avaliação para cada ocupação de usuário e mostrar os menores e maiores valores
