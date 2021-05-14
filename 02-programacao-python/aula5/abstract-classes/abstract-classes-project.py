from abc import ABC, abstractclassmethod
import math

class FormaGeometrica(ABC):
    """Classe FormaGeometrica.

        Imprime a posição inicial da forma geométrica."""
    @abstractclassmethod
    def desenhe(self):
        pass

class Forma2D(FormaGeometrica):
    """Classe Forma2D. Herda da FormaGeometrica.

        Calcula o perímetro.
        Calcula a área.
        Imprime a posição inicial, perímetro e área da forma geométrica.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y."""
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    @abstractclassmethod
    def calcule_perimetro(self):
        pass

    @abstractclassmethod
    def calcule_area(self):
        pass

    def desenhe(self):
        print(f"O(a) {type(self).__name__} está centrado(a) em ({self.x}, {self.y}).\n"\
             f"Seu perímetro é de {round(self.perimetro, 2)} e sua área é de {round(self.area, 2)}.")

class Forma3D(FormaGeometrica):
    """Classe Forma3D. Herda de FormaGeometrica.

        Calcula a área.
        Calcula o volume.
        Imprime a posição inicial, area superfícial e volume da forma geométrica.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - z : coordenada inicial em z."""
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    @abstractclassmethod
    def calcule_area(self):
        pass

    @abstractclassmethod
    def calcule_volume(self):
        pass

    def desenhe(self):
        print(f"A(o) {type(self).__name__} está centrada(o) em ({self.x}, {self.y}, {self.z}).\n"\
             f"Sua área superficial é de {round(self.area, 2)} e seu volume é de {round(self.volume, 2)}.")

class Poligono(Forma2D):
    """Classe Poligono. Herda de Forma2D."""
    pass

class Quadrado(Poligono):
    """Classe Quadrado. Herda de Poligono.

        Calcula o perímetro.
        Calcula a altura.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - largura : comprimento dos lados."""
    def __init__(self, x=0, y=0, largura=1):
        super().__init__(x, y)
        self.largura = largura

    def calcule_perimetro(self):
        self.perimetro = 4*self.largura
        return round(self.perimetro, 2)

    def calcule_area(self):
        self.area = self.largura**2
        return round(self.area, 2)

# Double Dispatching
    def compara_retangulo(self, retangulo): return False
    def compara_circulo(self, circulo): return False
    def compara_esfera(self, esfera): return False
    def compara_cubo(self, cubo): return False
    def compara_cilindro(self, cilindro): return False
    def compara_quadrado(self, outro_quadrado):
        return self.x == outro_quadrado.x and self.y == outro_quadrado.y and self.largura == outro_quadrado.largura
    def __eq__(self, outro):
        return outro.compara_quadrado(self)


class Retangulo(Quadrado):
    """Classe Retangulo. Herda de Quadrado.

        Calcula o perímetro.
        Calcula a área.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - largura : comprimento ao longo de x.
            - altura : comprimento ao longo de y."""
    def __init__(self, x=0, y=0, largura=1, altura=1):
        super().__init__(x, y, largura)
        self.altura = altura

    def calcule_perimetro(self):
        self.perimetro = 2*(self.largura+self.altura)
        return round(self.perimetro, 2)

    def calcule_area(self):
        self.area = self.largura*self.altura
        return round(self.area,2)

# Double Dispatching
    def compara_quadrado(self, quadrado): return False
    def compara_circulo(self, circulo): return False
    def compara_esfera(self, esfera): return False
    def compara_cubo(self, cubo): return False
    def compara_cilindro(self, cilindro): return False
    def compara_retangulo(self, outro_retangulo):
        return self.x == outro_retangulo.x and self.y == outro_retangulo.y and self.largura == outro_retangulo.largura and self.altura == outro_retangulo.altura
    def __eq__(self, outro):
        return outro.compara_retangulo(self)


class Circulo(Forma2D):
    """Classe Circulo. Herda de Forma2D.

        Calcula o perímetro.
        Calcula a área

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - raio : raio do círculo."""
    def __init__(self, x=0, y=0, raio=1):
        super().__init__(x, y)
        self.raio = raio

    def calcule_perimetro(self):
        self.perimetro = 2*math.pi*self.raio
        return round(self.perimetro, 2)

    def calcule_area(self):
        self.area = math.pi*self.raio**2
        return round(self.area, 2)

# Double Dispatching
    def compara_quadrado(self, quadrado): return False
    def compara_retangulo(self, retangulo): return False
    def compara_esfera(self, esfera): return False
    def compara_cubo(self, cubo): return False
    def compara_cilindro(self, cilindro): return False
    def compara_circulo(self, outro_circulo):
        return self.x == outro_circulo.x and self.y == outro_circulo.y and self.raio == outro_circulo.raio
    def __eq__(self, outro):
        return outro.compara_circulo(self)


class Esfera(Forma3D):
    """Classe Esfera. Herda de Forma3D.

        Calcula a área superficial.
        Calcula o volume.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - z : coordenada inicial em z.
            - raio : raio da esfera."""
    def __init__(self, x=0, y=0, z=0, raio=1):
        super().__init__(x, y, z)
        self.raio = raio

    def calcule_area(self):
        self.area = 4*math.pi*self.raio**2
        return round(self.area, 2)

    def calcule_volume(self):
        self.volume = (4/3)*math.pi*self.raio**3
        return round(self.volume, 2)

# Double Dispatching
    def compara_quadrado(self, quadrado): return False
    def compara_retangulo(self, retangulo): return False
    def compara_circulo(self, circulo): return False
    def compara_cubo(self, cubo): return False
    def compara_cilindro(self, cilindro): return False
    def compara_esfera(self, outra_esfera):
        return self.x == outra_esfera.x and self.y == outra_esfera.y and self.z == outra_esfera.z and self.raio == outra_esfera.raio
    def __eq__(self, outro):
        return outro.compara_esfera(self)


class Cubo(Forma3D):
    """Classe Cubo. Herda de Forma3D.

        Calcula a área superficial.
        Calcula o volume.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - z : coordenada inicial em z.
            - largura : tamanho das arestas do cubo."""
    def __init__(self, x=0, y=0, z=0, largura=1):
        super().__init__(x, y, z)
        self.largura = largura

    def calcule_area(self):
        self.area = 6*self.largura**2
        return round(self.area, 2)

    def calcule_volume(self):
        self.volume = self.largura**3
        return round(self.volume, 2)

# Double Dispatching
    def compara_quadrado(self, quadrado): return False
    def compara_retangulo(self, retangulo): return False
    def compara_circulo(self, circulo): return False
    def compara_esfera(self, esfera): return False
    def compara_cilindro(self, cilindro): return False
    def compara_cubo(self, outro_cubo):
        return self.x == outro_cubo.x and self.y == outro_cubo.y and self.z == outro_cubo.z and self.largura == outro_cubo.largura
    def __eq__(self, outro):
        return outro.compara_cubo(self)


class Cilindro(Forma3D):
    """Classe Cilindro. Herda de Forma3D.

        Calcula a área superficial.
        Calcula o volume.

        Atributos:
            - x : coordenada inicial em x.
            - y : coordenada inicial em y.
            - z : coordenada inicial em z.
            - raio : raio da base do cilindro.
            - altura : altura do cilindro."""
    def __init__(self, x=0, y=0, z=0, raio=1, altura=1):
        super().__init__(x, y, z)
        self.raio, self.altura = raio, altura

    def calcule_area(self):
        self.area = math.pi*self.raio**2 + 2*math.pi*self.raio*self.altura
        return round(self.area, 2)

    def calcule_volume(self):
        self.volume = math.pi*self.raio**2*self.altura
        return round(self.volume, 2)

# Double Dispatching
    def compara_quadrado(self, quadrado): return False
    def compara_retangulo(self, retangulo): return False
    def compara_circulo(self, circulo): return False
    def compara_esfera(self, esfera): return False
    def compara_cubo(self, cubo): return False
    def compara_cilindro(self, outro_cilindro):
        return self.x == outro_cilindro.x and self.y == outro_cilindro.y and self.z == outro_cilindro.z and self.raio == outro_cilindro.raio and self.altura == outro_cilindro.altura
    def __eq__(self, outro):
        return outro.compara_cilindro(self)


class Quadro:
    """Classe Quadro.

        Define uma lista figuras_geometricas.
        Adiciona ítens à lista figuras_geometricas.
        Verifica se a figura já foi inserida na lista figuras_geometricas.
        Remove ítens da lista figuras_geometricas pelo índice.
        Remove ítens da lista figuras_geometricas pela forma.

        Atributos:
            - tamanho: tamanho máximo da lista figuras_geometricas."""
    figuras_geometricas = []
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def incluir(self, fig):
        if len(self.figuras_geometricas) == self.tamanho:
            raise ErroDeInclusao("O limite de elementos da lista foi atingido")
        self.figuras_geometricas.append(fig)

    def contem(self, fig):
        if fig in self.figuras_geometricas:
            print("A figura já foi adicionada à lista.")
        else:
            print("A figura não foi adicionada ou foi excluída da lista.")

    def remover(self, n):
        if not isinstance(n, int):
            raise ErroDeIndice("O valor deve ser inteiro")
        if (n < 0) or (n >= len(self.figuras_geometricas)):
            raise ErroDeIntervalo("O valor deve ser menor que o tamanho da lista")
        self.n = n
        print(f"Removendo Figura: {self.n}")
        self.figuras_geometricas.pop(n)

    def remover_fig(self, fig):
        self.fig = fig
        if fig not in self.figuras_geometricas:
            raise ErroDeEncontrarForma(f"A forma {type(fig).__name__} não existe na lista")
        for i, f in enumerate(self.figuras_geometricas):
            if(f == fig):
                self.remover(i)
                break

    def desenhe(self):
        for i, f in enumerate(self.figuras_geometricas):
            print(">>> Figura ", i, "<<<")
            f.desenhe()

class ErroDeIndice(Exception):
    """Exceção customizada ErroDeIndice."""
    pass

class ErroDeIntervalo(Exception):
    """Exceção customizada ErroDeIntervalo."""
    pass

class ErroDeEncontrarForma(Exception):
    """Exceção customizada ErroDeForma."""
    pass

class ErroDeInclusao(Exception):
    """Exceção customizada ErroDeInclusao."""
    pass
