import express from 'express'
import { sequelize } from './databases/conecta.js'
import routes from './routes.js'
import cors from "cors"
const app = express()
const port = 3000
app.use(cors())

app.use(express.json())
app.use(routes)

async function conecta_db() {
  try {
    await sequelize.authenticate();
    console.log('Conexão com banco de dados realizada com sucesso.');
    //cria as tabelas do sistema apartir dos modelos e se não existirem
    await sequelize.sync();
  } catch (error) {
    console.error('Erro na conexão com o banco de dados:', error);
  }
}

conecta_db()
app.get('/', (req, res) => {
  res.send('Aula 6: Desenvolvimento de serviços e APIs')
})

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`)
})