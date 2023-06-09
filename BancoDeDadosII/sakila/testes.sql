-- Crie um gatilho(trigger) que antes de deletar um filme armazene o titulo do filme a ser
-- excluído em uma tabela de log (logFilme);

CREATE TABLE IF NOT EXISTS logFilme(
  logFilme_id int(3) NOT NULL AUTO_INCREMENT,
  filmeTitulo varchar(255) NOT NULL,
  PRIMARY KEY (logFilme_id)
) ENGINE=InnoDB;

DELIMITER $$
CREATE TRIGGER logFilme BEFORE DELETE ON filme
FOR EACH ROW
BEGIN
  INSERT INTO logFilme(filmeTitulo) VALUES (OLD.titulo);
END$$
DELIMITER ;

DELETE FROM filme WHERE filme_id = 1000;


-- Crie um trigger que após cadastrar um novo país crie uma nova cidade vinculada a este país
-- com o nome seguinte nome: nome do país concatenado com a string "TEMP". Exemplo: ArgentinaTEMP;

DELIMITER $$
CREATE TRIGGER tempCity AFTER INSERT ON pais
FOR EACH ROW
BEGIN
  INSERT INTO cidade(cidade, pais_id) VALUES (CONCAT(NEW.pais, 'TEMP'), NEW.pais_id);
END$$
DELIMITER ;

INSERT INTO pais(pais) VALUES ('Argentina');

DROP trigger tempCity;


-- Crie um trigger que antes de cadastrar um filme verifique se a duração do filme (length) é
-- maior do que 10. Caso seja menor deverá “setar” a duração como 10;

DELIMITER $$
CREATE TRIGGER lengthFilme BEFORE INSERT ON filme
FOR EACH ROW
BEGIN
  IF NEW.duracao_do_filme < 10 THEN
    SET NEW.duracao_do_filme = 10;
  END IF;
END$$
DELIMITER ;

INSERT INTO filme(titulo, idioma_id, duracao_do_filme) VALUES ('Filme TESTE', 6 , 9);


-- Crie um trigger que antes de alterar algum dado de país, salve os dados antigos do país em
-- uma tabela de log (logCountry);

CREATE TABLE IF NOT EXISTS logCountry(
  logCountry_id int(3) NOT NULL AUTO_INCREMENT,
  paisDesatualizado varchar(255) NOT NULL,
  paisAtualizado varchar(255) NOT NULL,
  PRIMARY KEY (logCountry_id)
) ENGINE=InnoDB;

DELIMITER $$
CREATE TRIGGER logCountry BEFORE UPDATE ON pais
FOR EACH ROW
BEGIN
  INSERT INTO logCountry(paisDesatualizado, paisAtualizado) VALUES (OLD.pais, New.pais);
END$$
DELIMITER ;

UPDATE pais SET pais = 'Brasil' WHERE pais_id = 112;


-- Crie uma consulta para listar o primeiro nome de cada cliente;

SELECT primeiro_nome FROM cliente;


-- Crie uma consulta para exibir os idiomas seguidos da quantidade de filme de cada idioma em
-- ordem decrescente de quantidade de filme por idioma; exibindo o nome do idioma

SELECT idioma.nome, COUNT(filme_id) AS 'Quantidade de Filmes' FROM idioma
INNER JOIN filme ON idioma.idioma_id = filme.idioma_id
GROUP BY idioma.nome
ORDER BY COUNT(filme_id) DESC;


-- Crie uma consulta para listar os atores (primeiro_nome) seguido da quantidade de diferentes
-- filmes em que trabalhou por ordem crescente de primeiro_nome do ator.

SELECT ator.primeiro_nome, COUNT(filme_id) AS 'Quantidade de Filmes' FROM ator
INNER JOIN filme_ator ON ator.ator_id = filme_ator.ator_id
GROUP BY ator.primeiro_nome
ORDER BY ator.primeiro_nome ASC;