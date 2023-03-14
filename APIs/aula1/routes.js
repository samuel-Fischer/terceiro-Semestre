import { Router } from 'express'
import { produtoCreate, produtoDelete, produtoId, produtoIndex, produtoQuantidade, produtoUpdate } from './controllers/ProdutoController.js'
const router = Router()

router.get('/produtos', produtoIndex)
router.post('/produtos', produtoCreate)
router.put('/produtos/:id', produtoUpdate)
router.delete('/produtos/:id', produtoDelete)
router.get('/produtos/quant', produtoQuantidade)
router.get('/produtos/id/:id', produtoId)

export default router