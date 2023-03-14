import { Produto } from '../models/Produto.js'

export const produtoIndex = async (req, res) => {
  try {
    const produtos = await Produto.findAll();
    res.status(200).json(produtos)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const produtoCreate = async (req, res) => {
  const { descricao, marca, quant, preco } = req.body
  try {
    const novo = await Produto.create({
      descricao,
      marca,
      quant,
      preco
    })
    res.status(201).json(novo)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const produtoUpdate = async (req, res) => {
  const { id } = req.params;
  const { descricao, marca, quant, preco } = req.body

  if (!descricao || !marca || !quant || !preco) {
    res.status(400).json(
      {
        id: 0,
        msg: "Erro... informe descrição, nome, quantidade e preço do produto."
      })
    return
  }

  try {
    const atl = await Produto.update({
      descricao,
      marca,
      quant,
      preco
    }, {
      where: {
        id: id
      }
    });
    res.status(201).json({ id, msg: "Produto atualizado com sucesso!" })
  } catch (error) {
    res.status(400).json({ id: 2, msg: "Erro: " + error.message })
  }
}

export const produtoDelete = async (req, res) => {
  const { id } = req.params;
  try {
    await Produto.destroy({
      where: {
        id: id
      }
    });
    res.status(200).json({ id, msg: "Produto excluído com sucesso!" })
  } catch (error) {
    res.status(400).json({ id: 3, msg: "Erro: " + error.message })
  }
}

export const produtoQuantidade = async (req, res) => {
  try {
    const amount = await Produto.count('id');
    res.status(200).json({ msg: `Atualmente sua loja possui ${amount} produtos.` })
  } catch (error) {
    res.status(400).json({ id: 4, msg: "Erro: " + error.message })
  }
}

export const produtoId = async (req, res) => {
  const { id } = req.params;
  try {
    const produto = await Produto.findOne({ where: { id: id } });
    res.status(200).json({ msg: `O produto com o id ${id} encontrado foi o: ${produto.descricao}` })
  } catch (error) {
    res.status(400).json({ id: 5, msg: "Não foi encontrado nenhum produto com este ID." })
  }
}