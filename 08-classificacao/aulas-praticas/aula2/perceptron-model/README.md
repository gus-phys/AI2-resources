# Perceptron

## Exercício

Suponha que no final de semana haverá um festival de queijos e você queira modelar um Perceptron para predizer se vai ou não nesse festival. Para tomar a decisão, utilizará 3 variáveis (features) binárias:

* x_1: O tempo está bom?
* x_2: Seu namorado/a quer te acompanhar?
* x_3: Tem transporte público por perto? (Você não tem carro)

Considere o bias como a feature x_0 com valor 1 e seu peso como sendo o quanto você está disposto a ir nesse festival.
Note que o seu valor cresce no sentido negativo, ou seja, quanto mais próximo de zero, mais você gosta de queijo e está disposto a ir, enquanto valores negativos grandes indicam que não tem tanto desejo de ir.

Nessas condições, modele o perceptron de forma que:

1. Você adora queijo e vá mesmo que seu/ua namorado/a não vá e não exista transporte público próximo.
No entanto, se chover fica muito ruim e com certeza não irá.
2. Você vai ao festival se o tempo estiver bom OU se seu/ua namorado/a quiser ir E tiver transporte público.
