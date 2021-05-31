Exercício baseado em http://swcarpentry.github.io/

Crie um banco de dados com as tabelas a seguir:

  ![Banco de Dados survey](assets/diagrama_bd.png)

Para cada tabela crie os seguinte atributos

**Person: pessoa que realiza leituras** 

* id : identificação única	
* personal	: primeiro nome
* family : sobrenome

Exemplo de instâncias:

|id	|personal	|family|
|----------|:-------------:|------:|
dyer	| William	| Dyer|
pb	| Frank	| Pabodie |

**Site: localizações onde leituras foram realizadas** 

* name : nome do lugar	
* lat	 : latitude
* long : longitude

Exemplo de instâncias:
 
|name|	lat|	long|
|----------|:-------------:|------:|
|DR-1	|-49.85	|-128.57
|DR-3|	-47.15|	-126.72

**Visited: quando as leituras foram realizadas** 

* id : identificação única	
* site	: site visitado
* date : data da visita

Exemplo de instâncias:

|id	|site|	dated|
|----------|:-------------:|------:|
|619	|DR-1	|1927-02-08 |
|622	|DR-1	|1927-02-10 |

**Survey: leituras realizadas** 

* taken	: idenficação do site
* person	: id da pessoa que esta realizando a coleta 
* quant	 : quantitativo e indicativo do que está sendo medido. Valores possíveis rad, sal, and temp que referem-se a ‘Radiação’, ‘salinidade’ e ‘temperatura’
* reading : leitura 

Exemplo de instâncias:

|taken|	person	|quant|	reading|
|----------|:-------------:|------:|------:|
|619|	dyer|	rad|	9.82 |
|619	|dyer	|sal	|0.13 |
|622	|dyer|	rad	|7.8 |

## Exercício:
* Crie as seguintes consultas 
  * Listar quantidade de visitas que cada site recebeu
  * Listar sites que nao receberam visitas
  * Listar métricas que foram observadas na tabela survey
  * Listar pessoas que fizeram mais de dois levantamentos 
  * Listar pessoas que o sobrenome possua DYR no meio da palvra
  * Listar visitacoes a uma lista de sites passados como parâmetro
  * verifique quantas linhas possuem valor nulo na coluna quant na tabela survey
  * retorne a media de lat lon utilizando como parametro de busca um intervalo de datas
  * Retorne a quantidade de medições realizadas por cada pessoa na tabela person
  * retorne a pessoa que tem a maior quantidade de medições de temperatura entre 10 e 30
