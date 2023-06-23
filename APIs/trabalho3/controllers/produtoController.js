import { Log } from '../models/Log.js'
import { Produto } from '../models/Produto.js'
import { Usuario } from '../models/Usuario.js'

export const produtoIndex = async (req, res) => {
  try {
    const produtos = await Produto.findAll({ include: Usuario })
    res.status(200).json(produtos)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const produtoCreate = async (req, res) => {
  const { nome, quantidade, preco, usuario_id } = req.body

  // se não informou estes atributos
  // if (!nome || !quantidade || !preco) {
  //   res.status(400).json({ id: 0, msg: "Erro... Informe os dados" })
  //   return
  // }

  try {
    const produto = await Produto.create({
      nome, quantidade, preco,
      usuario_id
    });
    res.status(201).json(produto)
  } catch (error) {
    res.status(400).send(error)
  }
}

export const produtoDestroy = async (req, res) => {
  const { id } = req.params
  // obtém dados acrescentados no middleware verificaLogin (ao req)
  const user_logado_id = req.user_logado_id

  try {
    await Produto.destroy({ where: { id } });

    // registra um log desta exclusão
    await Log.create({
      descricao: "Exclusão do Produto " + id,
      usuario_id: user_logado_id
    })

    res.status(200).json({ msg: "Ok! Removido com Sucesso" })
  } catch (error) {
    res.status(400).send(error)
  }
}
