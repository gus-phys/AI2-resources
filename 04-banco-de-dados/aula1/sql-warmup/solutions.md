## Exercício:
* Crie as seguintes consultas
  * Listar quantidade de visitas que cada site recebeu
'''sql
SELECT COUNT(id), site
FROM Visited
GROUP BY site;
'''
  * Listar sites que nao receberam visitas
  * Listar métricas que foram observadas na tabela survey
'''sql
SELECT DISTINCT quant
FROM Survey;
'''
  * Listar pessoas que fizeram mais de dois levantamentos
'''sql
SELECT COUNT(person), person
FROM Survey
GROUP BY person
HAVING COUNT(person) > 2;
'''
  * Listar pessoas que o sobrenome possua DYE no meio da palvra
'''sql
SELECT *
FROM Person
WHERE family LIKE '%DYE%';
'''
  * Listar visitacoes a uma lista de sites passados como parâmetro
'''sql
SELECT site
FROM Visited
WHERE site IN ('DR-1', 'MSK-4');
'''
  * verifique quantas linhas possuem valor nulo na coluna quant na tabela survey
'''sql
SELECT taken, person
FROM Survey
WHERE quant = NULL;
'''
  * retorne a media de lat lon utilizando como parametro de busca um intervalo
   de datas
  * Retorne a quantidade de medições realizadas por cada pessoa na tabela person
  * retorne a pessoa que tem a maior quantidade de medições de temperatura entre
   10 e 30
