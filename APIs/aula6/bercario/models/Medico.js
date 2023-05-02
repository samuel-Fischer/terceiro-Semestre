import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Medico = sequelize.define('medico', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  CRM: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  nome: {
    type: DataTypes.STRING(50),
    allowNull: false
  },
  telefone: {
    type: DataTypes.STRING(20),
    allowNull: false
  },
  especialidade: {
    type: DataTypes.STRING(30),
    allowNull: false, 
    unique: true
  }
}, {
  
});