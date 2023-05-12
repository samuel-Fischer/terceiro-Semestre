DROP DATABASE IF EXISTS aula3;
CREATE DATABASE IF NOT EXISTS aula3;
USE aula3;


DROP TABLE IF EXISTS empregado;
CREATE TABLE IF NOT EXISTS empregado(
  codigo INT,
  nome CHAR(40) NOT NULL,
  setor CHAR(2),
  cargo CHAR(20),
  salario DECIMAL(10,2),
  PRIMARY KEY(codigo)
);


INSERT INTO empregado VALUES (1, "Edecio Muito Legal", "2", "Designer", 1000);
INSERT INTO empregado VALUES (3, "Eduardo Monks", "5", "Dev", 1500);
INSERT INTO empregado VALUES (4, "Raquel Murillo", "4", "Dev", 1500);
INSERT INTO empregado VALUES (6, "Gladimau Catarino", "4", "Analista", 2200);
INSERT INTO empregado VALUES (7, "Sergio Marquina", "4", "Boss", 9900);
INSERT INTO empregado VALUES (9, "Alicia Sierra", "5", "Boss", 9900);
INSERT INTO empregado VALUES (10, "Angelo Light", "1", "Dev", 1500);
INSERT INTO empregado VALUES (15, "Silene Oliveira", "1", "DBA", 2500);
INSERT INTO empregado VALUES (25, "Darta Inhame", "3", "Designer", 1650);


SELECT * FROM empregado;

SELECT * FROM empregado WHERE (nome = "Sergio Marquina");


UPDATE empregado
SET nome = "Salvador Martin"
WHERE nome = "Sergio Marquina";

DELETE FROM empregado WHERE (setor = "3");

SELECT * FROM empregado WHERE (setor = "1") ORDER BY cargo;

SELECT * FROM empregado ORDER BY cargo DESC, nome ASC;

-- 1.
SELECT * FROM empregado;
-- 2.
SELECT nome, cargo
FROM empregado;
-- 3.
SELECT nome
FROM empregado
WHERE (setor = "1");
-- 4.
SELECT nome, salario
FROM empregado
ORDER BY nome;
-- 5.
SELECT nome, salario
FROM empregado
ORDER BY nome DESC;
-- 6.
SELECT setor, nome
FROM empregado
ORDER BY setor, nome DESC;
-- 7.
SELECT nome
FROM empregado
WHERE (setor = "4")
ORDER BY nome;
-- 8.
UPDATE empregado
SET salario = 8000
WHERE codigo = 6;
-- 9. 
UPDATE empregado
SET setor = 3
WHERE nome = "Eduardo Monks";
-- 10.
UPDATE empregado
SET salario = salario * 1.20;
-- 11.
DELETE FROM empregado 
WHERE (setor = "3");
-- 12.
DELETE FROM empregado 
WHERE (nome = "Gladimau Catarino");




ALTER TABLE empregado ADD COLUMN admissao DATE;

UPDATE empregado SET admissao = "2000-04-01" WHERE codigo = 1;
UPDATE empregado SET admissao = "2000-07-01" WHERE codigo = 4;
UPDATE empregado SET admissao = "2012-09-20" WHERE codigo = 7;
UPDATE empregado SET admissao = "2000-08-20" WHERE codigo = 9;
UPDATE empregado SET admissao = "2000-06-01" WHERE codigo = 10 OR codigo = 15;

SELECT * FROM empregado WHERE admissao = "2000-06-01";
SELECT * FROM empregado WHERE admissao > "2002-01-01";

INSERT INTO empregado VALUES (16, "Eduardo Monks", "3", "Boss", 9900, "")

SELECT * FROM empregado WHERE nome LIKE "E%"; -- Lista empreados que o nome começa com a letra E
SELECT * FROM empregado WHERE nome LIKE "_A%"; -- Lista empreados que a segunda letra do nome é A
SELECT * FROM empregado WHERE nome LIKE "__L%"; -- Lista empreados que a terceira letra do nome é L
SELECT * FROM empregado WHERE nome LIKE "%A"; -- Lista empreados que o último letra do nome é A