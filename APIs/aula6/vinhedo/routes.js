import { Router } from "express"
import { vinhoCreate, vinhoIndex } from "./controllers/vinhoController.js"
import { marcaCreate, marcaIndex } from "./controllers/marcaController.js"

const router = Router()

router.get('/vinhos', vinhoIndex)
      .post('/vinhos', vinhoCreate)
      .get('/marcas', marcaIndex)
      .post('/marcas', marcaCreate)

export default router