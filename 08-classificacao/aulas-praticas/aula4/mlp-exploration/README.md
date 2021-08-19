# Exercícios

<img src="assets/mlp_mnist.png" width=600px>

* Crie uma rede neural com 784 neurônios de entrada, uma camada escondida de 128 unidades e função de ativação ReLU, outra camada escondida com 64 neurônios e novamente a função de ativação ReLU, e finalmente uma camada de saída com a Softmax como função de ativação, como mostrado na figura acima.
Para usar a ReLU, pode usar o módulo nn.ReLU ou a função F.relu.
* Construa um modelo que retorne o log-softmax como saída e calcule a função de loss utilizando o _negative log likelihood_.
Note que para `nn.LogSoftmax` e `F.log_softmax` você precisa setar o parâmetro `dim` de forma apropriada.
`dim=0` computa o softmax pelas linhas (amostras), de forma que as colunas somem 1, enquanto `dim=1` calcula a softmax pelas colunas, de forma que as linhas somem 1.
Pense no que deseja como saída e escolha `dim` de forma apropriada.
* Implemente o treinamento completo de nossa rede. Se for implementada corretamente, você deverá ver o _loss_ diminuindo a cada época.
