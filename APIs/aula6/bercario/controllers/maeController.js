import { Mae } from '../models/Mae.js';

export const maeIndex = async (req, res) => {
  try {
    const mae = await Mae.findAll();
    res.status(200).json(mae);
  } catch (error) {
    res.status(400).send(error);
  };
};

export const maeCreate = async (req, res) => {
  const { nome, endereco, telefone, data_nascimento } = req.body;

  if (!nome || !endereco || !telefone || !data_nascimento) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados." });
    return;
  };

  try {
    const mae = await Mae.create({
      nome, endereco, telefone, data_nascimento
    });
    res.status(201).json(mae);
  } catch (error) {
    res.status(400).send(error);
  };
};