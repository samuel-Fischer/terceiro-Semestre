-- * 1) Utilizando o operador IN, crie uma consulta para que liste o nome de todos os gêneros menos os gêneros de
-- * suspense, terror e comédia;

SELECT g.nome "Genero"
FROM genero g
WHERE
    g.nome NOT IN ('Suspense','Comédia','Terror');



-- * 2) Utilizando subconsultas, crie uma consulta que retorne os títulos, gênero e duração de filmes em que o gênero seja
-- * SUSPENSE e a duração esteja entre 70 e 130 minutos;

SELECT f.tituloOriginal AS "Filme", g.nome "Genero", f.duracao
FROM filme f
INNER JOIN genero g ON f.idGenero = g.id
WHERE
    g.nome IN('Suspense') AND
    (f.duracao >= 70 AND f.duracao <= 130);



-- * 3) Crie uma function incrementar +44min em todos os filmes de um determinado gênero (o gênero é passado como
-- * parâmetro).

DELIMITER $$
CREATE PROCEDURE incrementar_Time(IN nomeGenero VARCHAR(45))
BEGIN
UPDATE filme
SET filme.duracao = filme.duracao + 44
WHERE filme.idGenero IN (SELECT genero.id
                        FROM genero
                        WHERE genero.nome = nomeGenero);
END $$
DELIMITER ;

CALL incrementar_Time("Suspense");



-- * 4) Crie uma procedure que recebe o nome de um ator e informa os filmes que ele participou;

DROP PROCEDURE IF EXISTS ator_filme;

DELIMITER $$
CREATE PROCEDURE ator_filme(IN nomeAtor VARCHAR(45))
BEGIN
    SELECT f.tituloOriginal AS "Filme"
    FROM filme f
    INNER JOIN elenco e ON f.id = e.idFilme
    INNER JOIN ator a   ON a.id = e.idAtor
    WHERE a.nome = nomeAtor;
END $$
DELIMITER ;

CALL ator_filme("Emmanuelle Riva");



-- * 5) Crie uma procedure que informe o nome dos atores que não participaram de nenhum filme;

DROP PROCEDURE IF EXISTS ator_desempregado;

DELIMITER $$
CREATE PROCEDURE ator_desempregado()
BEGIN
    SELECT a.nome AS "Ator"
    FROM ator a
    LEFT JOIN elenco e ON a.id = e.idAtor
    WHERE e.idAtor IS NULL;
END $$
DELIMITER ;

CALL ator_desempregado();



-- * 6) Crie uma procedure que exiba o título e o gênero de todos os filmes que não passaram ainda em cinema algum;

DROP PROCEDURE IF EXISTS filme_nao_exibido;

DELIMITER $$
CREATE PROCEDURE filme_nao_exibido()
BEGIN
    SELECT f.tituloOriginal AS "Filme", g.nome AS "Genero"
    FROM filme f
    INNER JOIN genero g ON f.idGenero = g.id
    WHERE f.id NOT IN (SELECT sessao.idFilme FROM sessao);
END $$
DELIMITER ;

CALL filme_nao_exibido();



-- * 7) Crie uma procedure que receba como parâmetro o nome de uma cidade e exiba os cinemas existentes nesta cidade.;

DROP PROCEDURE IF EXISTS cinemas_cidade;

DELIMITER $$
CREATE PROCEDURE cinemas_cidade(IN nomeCidade VARCHAR(45))
BEGIN
    SELECT c.nomeFantasia AS "Cinema"
    FROM cinema c
    INNER JOIN cidade ci ON c.idCidade = ci.id
    WHERE ci.nome = nomeCidade;
END $$
DELIMITER ;

CALL cinemas_cidade("Pelotas");



-- * 8) Crie uma procedure que receba dois parâmetros (gênero atual, gênero novo) e altere o gênero dos filmes de acordo
-- * com os parâmetros recebidos.

DROP PROCEDURE IF EXISTS alterar_genero;

DELIMITER $$
CREATE PROCEDURE alterar_genero(IN generoAtual VARCHAR(45), IN generoNovo VARCHAR(45))
BEGIN
    UPDATE filme
    SET filme.idGenero = (SELECT genero.id
                        FROM genero
                        WHERE genero.nome = generoNovo)
    WHERE filme.idGenero = (SELECT genero.id
                        FROM genero
                        WHERE genero.nome = generoAtual);
END $$
DELIMITER ;

CALL alterar_genero("Suspense", "Pânico");




SHOW PROCEDURE STATUS WHERE db = 'AULA08';

SHOW FUNCTION STATUS WHERE db = 'AULA08';