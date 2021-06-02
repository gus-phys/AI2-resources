## Soluções:
  * Listar quantidade de visitas que cada site recebeu  
```sql
SELECT COUNT(id), site
FROM Visited
GROUP BY site;
```
  * Listar sites que não receberam visitas
```sql
SELECT name
FROM Site
WHERE name NOT IN (
  SELECT site
  FROM Visited);
```
  * Listar métricas que foram observadas na tabela Survey
```sql
SELECT DISTINCT quant
FROM Survey;
```
  * Listar pessoas que fizeram mais de dois levantamentos
```sql
SELECT COUNT(person), person
FROM Survey
GROUP BY person
HAVING COUNT(person) > 2;
```
  * Listar pessoas que o sobrenome possua DYE no meio da palavra
```sql
SELECT *
FROM Person
WHERE family LIKE '%DYE%';
```
  * Listar visitacoes a uma lista de sites passados como parâmetro
```sql
SELECT site
FROM Visited
WHERE site IN ('DR-1', 'MSK-4');
```
  * verifique quantas linhas possuem valor nulo na coluna quant na tabela Survey
```sql
SELECT taken, person
FROM Survey
WHERE quant = NULL;
```
  * retorne a media de lat lon utilizando como parâmetro de busca um intervalo
   de datas
```sql
SELECT *
FROM Site
WHERE name IN (
  SELECT site
  FROM Visited
  WHERE dated BETWEEN '1927-02-09' and '1930-01-10');
```
  * Retorne a quantidade de medições realizadas por cada pessoa na tabela Person
```sql
SELECT person, COUNT(person)
FROM Survey
WHERE person IN (
  SELECT id
  FROM  Person)
GROUP BY person;
```
  * Retorne a pessoa que tem a maior quantidade de medições de temperatura entre
-30 e -10
```sql
SELECT COUNT(person), person, quant, reading
FROM Survey
WHERE quant = 'temp' AND reading BETWEEN -30 and -10
GROUP BY person
ORDER BY COUNT(person) DESC
LIMIT 1;
```
