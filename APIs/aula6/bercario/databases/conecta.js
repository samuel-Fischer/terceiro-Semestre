import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize(
  'bercario', 'root', '12345678', {
  host: 'localhost',
  dialect: 'mysql',
  port: 3306
});