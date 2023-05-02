import { Router } from "express"
import { bebeCreate, bebeIndex } from "./controllers/bebeController.js"
import { maeCreate, maeIndex } from "./controllers/maeController.js"
import { medicoCreate, medicoIndex } from "./controllers/medicoController.js"

const router = Router()

router.get('/bebes', bebeIndex)
      .post('/bebes', bebeCreate)
      .get('/maes', maeIndex)
      .post('/maes', maeCreate)
      .get('/medicos', medicoIndex)
      .post('/medicos', medicoCreate)

export default router