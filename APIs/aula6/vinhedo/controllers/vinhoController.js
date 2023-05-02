import { Vinho } from '../models/Vinho.js';
import { Marca } from '../models/Marca.js';

export const vinhoIndex = async (req, res) => {
  try {
    const vinho = await Vinho.findAll(
      { include: Marca}
    );
    res.status(200).json(vinho);
  } catch (error) {
    res.status(400).send(error);
  };
};

export const vinhoCreate = async (req, res) => {
  const { tipo, marca_id, preco, teor } = req.body;

  if (!tipo || !marca_id || !preco || !teor) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados." });
    return;
  };

  try {
    const vinho = await Vinho.create({
      tipo, marca_id, preco, teor
    });
    res.status(201).json(vinho);
  } catch (error) {
    res.status(400).send(error);
  };
};

