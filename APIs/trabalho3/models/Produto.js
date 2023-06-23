import { DataTypes } from 'sequelize';
import { sequelize } from '../databases/conecta.js';
import { Usuario } from './Usuario.js'

export const Produto = sequelize.define('produto', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nome: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  quantidade: {
    type: DataTypes.INTEGER(6),
    defaultValue: 10
  },
  preco: {
    type: DataTypes.INTEGER(6),
    defaultValue: 5.99
  },
}, {
  paranoid: true
});

Produto.belongsTo(Usuario, {
  foreignKey: {
    name: 'usuario_id',
    allowNull: false
  },
  onDelete: 'RESTRICT',
  onUpdate: 'CASCADE'
})

Usuario.hasMany(Produto, {
  foreignKey: 'usuario_id'
})
