import { Sequelize } from 'sequelize';

export const sequelize = new Sequelize(
  "trabalho3", "root", "12345678", {
  dialect: "mysql",
  host: "localhost",
  port: 3306
});