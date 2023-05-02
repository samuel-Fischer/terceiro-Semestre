import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';

export const Mae = sequelize.define('mae', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nome: {
    type: DataTypes.STRING(50),
    allowNull: false
  },
  endereco: {
    type: DataTypes.STRING(30),
    allowNull: false
  },
  telefone: {
    type: DataTypes.STRING(20),
    allowNull: false
  },
  data_nascimento: {
    type: DataTypes.DATE(30),
    allowNull: false
  }
});