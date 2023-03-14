import express from 'express'
import { sequelize } from './databases/conecta.js'

const app = express()
const port = 3000

import routes from './routes.js'
app.use(express.json())
app.use(routes)

async function conecta_db() {
  try {
    await sequelize.authenticate();
    console.log('Conexão com banco de dados realizada com sucesso.');
    // cria as tabelas do sistema (a partir dos modelos) e se não existir.
    await sequelize.sync();
  } catch (error) {
    console.error('Erro na conenão com o banco: ', error);
  }
}

conecta_db()

app.get('/', (req, res) => {
  res.send('Aula 1: Desenvolvimento de Serviços e APIs')
})

app.listen(port, () => {
  console.log(`Servidor Rodando na Porta: ${port}`)
})