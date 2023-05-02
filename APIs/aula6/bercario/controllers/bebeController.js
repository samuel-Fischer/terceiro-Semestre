import { Bebe } from '../models/Bebe.js';
import { Mae } from '../models/Mae.js';
import { Medico } from '../models/Medico.js';

export const bebeIndex = async (req, res) => {
  try {
    const bebe = await Bebe.findAll(
      { include: [Mae, Medico] },
    );
    res.status(200).json(bebe);
  } catch (error) {
    res.status(400).send(error);
  };
};

export const bebeCreate = async (req, res) => {
  const { nome, mae_id, medico_id, data_nascimento, peso_nascimento, altura } = req.body;

  if (!nome || !mae_id || !medico_id || !data_nascimento || !peso_nascimento || !altura) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados." });
    return;
  };

  try {
    const bebe = await Bebe.create({
      nome, mae_id, medico_id, data_nascimento, peso_nascimento, altura
    });
    res.status(201).json(bebe);
  } catch (error) {
    res.status(400).send(error);
  };
};