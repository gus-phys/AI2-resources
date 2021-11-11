# Exercicios

Considerando o seguinte dataset:

```python
from sklearn.datasets import make_circles
X, y = make_circles(100, factor=.1, noise=.1)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
```

1. Transforme o dataset a seguir usando KPCA. Encontre o valor de `gamma` que maximiza a separabilidade.
1. Transforme o mesmo dataset para uma menor dimensionalidade utilizando PCA e LDA. Utilize as transformacoes para alimentar um algoritmo de classificação linear (Perceptron, regressão logística, etc). Compare os resultados com o KPCA otimizado.
