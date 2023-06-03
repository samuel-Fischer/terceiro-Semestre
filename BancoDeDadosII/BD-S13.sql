-- 1. Crie um banco de dados chamado aula13.
CREATE DATABASE IF NOT EXISTS aula13;
USE aula13;


-- 2. No banco aula13 crie as tabelas conforme o diagrama.
CREATE TABLE IF NOT EXISTS usuario (
  id INT AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  email VARCHAR(255) NOT NULL,
  fone VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS forum (
  id INT AUTO_INCREMENT,
  titulo VARCHAR(45) NOT NULL,
  data_criacao DATE NOT NULL,
  PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS postagem (
  usuario_id INT NOT NULL,
  forum_id INT NOT NULL,
  mensagem TEXT NOT NULL,
  data_postagem DATE NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario (id),
  FOREIGN KEY (forum_id) REFERENCES forum (id)
) ENGINE=INNODB;


-- 3. Crie um usuário chamado moderador, com a senha 123teste. Este usuário poderá acessar as 3 tabelas com permissão de INSERT, UPDADE e DELETE.
CREATE USER 'caramalvado'@'localhost' IDENTIFIED BY '123teste';
GRANT INSERT, UPDATE, DELETE ON aula13.* TO 'caramalvado'@'localhost';


-- 4. Crie um usuário chamado pikachu, com a senha teste123. Este usuário poderá somente fazer SELECT no campo mensagem da tabela postagem
CREATE USER 'cabrabom'@'localhost' IDENTIFIED BY 'teste123';
GRANT SELECT (mensagem) ON aula13.Postagem TO 'cabrabom'@'localhost';


-- 5. Crie um usuário chamado maverick, com a senha topgun. Este usuário poderá fazer INSERT, UPDATE e DELETE nas tabelas fórum e postagem. Ele
-- também poderá fazer SELECT na tabela usuário.
CREATE USER 'maverick'@'localhost' IDENTIFIED BY 'topgun';
GRANT INSERT, UPDATE, DELETE ON aula13.forum TO 'maverick'@'localhost';
GRANT INSERT, UPDATE, DELETE ON aula13.postagem TO 'maverick'@'localhost';
GRANT SELECT ON aula13.usuario TO 'maverick'@'localhost';

-- Atualiza as permissões
FLUSH PRIVILEGES;

-- Renomeia o nome de usuário
RENAME USER 'caramalvado'@'localhost' TO 'moderador'@'localhost';
RENAME USER 'cabrabom'@'localhost' TO 'pikachu'@'localhost';

-- Alterar a senha de um usuário
-- ALTER USER 'maverick'@'localhost' IDENTIFIED BY 'topgun7';

-- Para ver quais são os usuários cadastrados no banco de dados
SELECT user FROM mysql.user;

-- Para ver quais são as permissões de um usuário
SHOW GRANTS FOR 'moderador'@'localhost';
SHOW GRANTS FOR 'maverick'@'localhost';

-- Para sair do banco de dados
quit;

-- Para logar com um usuário no banco de dados
mysql -u moderador -p;

-- Para checar qual usuário está logado
SELECT current_user();

-- Para exclui um usuário
-- DROP USER 'maverick'@'localhost';


-- 6. Com o usuário moderador, faça inserção de regi  stros nas tabelas forum e usuario (pelo menos 8 registros na tabela usuario e 5 registros na tabela forum).
USE aula13
-- faça inserção de 8 usuários na tabela usuario
INSERT INTO usuario (nome, email, fone) VALUES ('Pedro', 'pedro@gmail.com', '9999-9999');
INSERT INTO usuario (nome, email, fone) VALUES ('Maria', 'maria@gmail.com', '8888-8888');
INSERT INTO usuario (nome, email, fone) VALUES ('João', 'joao@gmail.com', '7777-7777');
INSERT INTO usuario (nome, email, fone) VALUES ('Ana', 'ana@gmail.com', '6666-6666');
INSERT INTO usuario (nome, email, fone) VALUES ('Fulano', 'fulano@gmail.com', '5555-5555');
INSERT INTO usuario (nome, email, fone) VALUES ('Beltrano', 'beltrano@gmail.com', '4444-4444');
INSERT INTO usuario (nome, email, fone) VALUES ('Ciclano', 'ciclano@gmail.com', '3333-3333');
INSERT INTO usuario (nome, email, fone) VALUES ('José', 'jose@gmail.com', '2222-2222');

-- faça inserção de 5 fóruns
INSERT INTO forum (titulo, data_criacao) VALUES ('Fórum 1', NOW());
INSERT INTO forum (titulo, data_criacao) VALUES ('Fórum 2', NOW());
INSERT INTO forum (titulo, data_criacao) VALUES ('Fórum 3', NOW());
INSERT INTO forum (titulo, data_criacao) VALUES ('Fórum 4', NOW());
INSERT INTO forum (titulo, data_criacao) VALUES ('Fórum 5', NOW());


-- 7. Com o usuário root consulte o conteúdo das tabelas fórum e usuário; (tente fazer as mesmas consultas com os usuários moderador, pikachu e maverick)
SELECT * FROM usuario;
SELECT * FROM forum;
mysql -u maverick -p;


-- 8. Com o usuário maverick, insira 10 registros na tabela postagem (as postagens deverão ser de 6 usuários diferentes).
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (1, 3, 'Vendo canguru a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (2, 1, 'Compro laranja a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (3, 2, 'Troco canguru por laranja', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (4, 5, 'Vendo laranja a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (5, 4, 'Troco laranja por canguru', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (6, 3, 'Compro canguru a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (7, 2, 'Troco laranja por canguru', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (8, 1, 'Vendo canguru a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (3, 4, 'Compro laranja a pilha', NOW());
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (8, 5, 'Troco canguru por laranja', NOW());


-- 9. Com o usuário root consulte o conteúdo da tabela postagem; (tente fazer a mesma consulta com os usuários moderador, pikachu e maverick)
SELECT * FROM postagem;


-- 10. Com o usuário moderador, faça uma consulta que retorne: título do fórum, nome do usuário e data da postagem
SELECT f.titulo, u.nome, p.data_postagem FROM postagem p
INNER JOIN usuario u ON u.id = p.usuario_id
INNER JOIN forum f ON f.id = p.forum_id;


-- 11. Com o usuário pikachu, tente fazer a mesma consulta da questão anterior (exiba o print da consulta e o resultado obtido).
SELECT f.titulo, u.nome, p.data_postagem FROM postagem p
INNER JOIN usuario u ON u.id = p.usuario_id
INNER JOIN forum f ON f.id = p.forum_id;


-- 12. Acesse o banco com o usuário root (ou algum usuário com permissões de superadmin)
mysql -u root -p


-- 13. Verifique se o autocommit do banco está ativo ou não (exiba o comando)
SELECT @@autocommit;


-- 14. Desabilite o autocommit
SET autocommit = 0;


-- 15. Faça uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 16. Inicie uma transação
START TRANSACTION;


-- 17. Insira 1 novo registro a tabela postagem
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (2, 3, 'Vendo manteiga a pilha', NOW());


-- 18. Faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 19. Execute um rollback da transação.
ROLLBACK;


-- 20. Faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 21. Inicie uma transação
START TRANSACTION;


-- 22. Faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 23. Insira 1 novo registro a tabela postagem
INSERT INTO postagem (usuario_id, forum_id, mensagem, data_postagem) VALUES (3, 3, 'Vendo beterraba a pilha', NOW());


-- 24. Faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 25. Execute o commit da transação.
COMMIT;


-- 26. Faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
SELECT * FROM postagem;


-- 27. Tente realizar um rollback e faça, novamente, uma consulta (SELECT) de todos os registros da tabela postagem
ROLLBACK;
SELECT * FROM postagem;


-- 28. Habilite o autocommit
SET autocommit = 1;


-- 29. Exclua o usuário maverick
DROP USER 'maverick'@'localhost';


-- 30. Exclua o usuário pikachu
DROP USER 'pikachu'@'localhost';


-- 31. Exclua o usuário moderador
DROP USER 'moderador'@'localhost';


-- 32. Faça uma consulta que exiba o título das postagens dos usuários que o nome (nome do usuário) tenha a letra “a”.
SELECT f.titulo, u.nome, p.data_postagem FROM postagem p
INNER JOIN usuario u ON u.id = p.usuario_id
INNER JOIN forum f ON f.id = p.forum_id
WHERE u.nome LIKE '%a%';

