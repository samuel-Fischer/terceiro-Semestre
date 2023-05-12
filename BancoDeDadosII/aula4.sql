DROP SCHEMA IF EXISTS aula04;
CREATE SCHEMA IF NOT EXISTS aula04;
USE aula04;

DROP TABLE IF EXISTS produtos;
CREATE TABLE IF NOT EXISTS produtos (
  referencia  VARCHAR(3) NOT NULL,
  descricao   VARCHAR(50) NULL DEFAULT NULL,
  estoque     INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (referencia)
);

INSERT INTO produtos VALUES ('001', 'Feijão', 10);
INSERT INTO produtos VALUES ('002', 'Arroz', 5);
INSERT INTO produtos VALUES ('003', 'Farinha', 15);


DROP TABLE IF EXISTS itensVenda;
CREATE TABLE IF NOT EXISTS itensVenda (
  venda       INT(11) NULL DEFAULT NULL,
  produto     VARCHAR(3) NULL DEFAULT NULL,
  quantidade  INT(11) NULL DEFAULT NULL,
  CONSTRAINT fk_itensVenda_produto
  FOREIGN KEY (produto) REFERENCES produtos (referencia) ON DELETE NO ACTION ON UPDATE NO ACTION
);


SELECT * FROM produtos;
DESC produtos;

INSERT INTO itensVenda VALUES(1, "003", 2);
UPDATE produtos SET estoque = estoque - 2 WHERE referencia = "003";


-- Cria uma trigger para diminuir uma estoque toda a vez que ouver uma venda nova em itens venda
DELIMITER $$
CREATE TRIGGER trg_itensVenda_AI AFTER INSERT
ON itensVenda
FOR EACH ROW
BEGIN
    UPDATE produtos SET estoque = estoque - NEW.quantidade WHERE referencia = NEW.produto;
END$$
DELIMITER ;

INSERT INTO itensVenda VALUES(2, "001", 4);


-- Cria uma trigger para retornar a quantidade em estoque da tabela produtos, toda vez que um venda for deletada
DELIMITER $$
CREATE TRIGGER trg_itensVenda_AD AFTER DELETE
ON itensVenda
FOR EACH ROW
BEGIN
    UPDATE produtos SET estoque = estoque + OLD.quantidade WHERE referencia = OLD.produto;
END$$
DELIMITER ;

DELETE FROM itensVenda WHERE venda = 1;



-- SELECT USER();
-- SELECT CURRENT_USER();
-- SELECT NOW();



-- Criação de uma tabela que tera o registro de todas as informações de quando uma coluna do itensVendas for deletado
DROP TABLE IF EXISTS registro;
CREATE TABLE IF NOT EXISTS registro (
  ID            INT AUTO_INCREMENT NOT NULL,
  produto_ref   INT(3) NOT NULL,
  produto_nome  VARCHAR(50) NULL DEFAULT NULL,
  produto_qnt   INT(11) NULL DEFAULT NULL,
  usuario       VARCHAR(30) NOT NULL,
  data_exclusao DATETIME,
  PRIMARY KEY (ID)
);


-- Cria uma trigger que registra todas as informações do que, quando e quem deletou uma venda da tabela itensVenda
DELIMITER $$
CREATE TRIGGER trg_registro_AD AFTER DELETE
ON itensVenda
FOR EACH ROW
BEGIN
    INSERT INTO registro (produto_ref, produto_nome, produto_qnt, usuario, data_exclusao)
    VALUES (OLD.produto, (SELECT descricao FROM produtos 
    WHERE referencia = OLD.produto), OLD.quantidade, (SELECT USER()), NOW());
END$$
DELIMITER ;

INSERT INTO itensVenda VALUES(3, "003", 6);