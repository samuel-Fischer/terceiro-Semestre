import { Medico } from '../models/Medico.js';

export const medicoIndex = async (req, res) => {
  try {
    const medico = await Medico.findAll();
    res.status(200).json(medico);
  } catch (error) {
    res.status(400).send(error);
  };
};

export const medicoCreate = async (req, res) => {
  const { CRM , nome, telefone, especialidade } = req.body;

  if (!CRM || !nome || !telefone || !especialidade) {
    res.status(400).json({ id: 0, msg: "Erro... Informe os dados." });
    return;
  };

  try {
    const medico = await Medico.create({
      CRM, nome, telefone, especialidade
    });
    res.status(201).json(medico);
  } catch (error) {
    res.status(400).send(error);
  };
};