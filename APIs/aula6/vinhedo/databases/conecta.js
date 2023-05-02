import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize(
  'vinhedo', 'root', '12345678', {
  host: 'localhost',
  dialect: 'mysql',
  port: 3306
});