import 'dotenv/config';
import express from 'express';
import { prisma } from './db/prisma';

const app = express();
app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({ status: 'api ok' });
});

app.get('/health/db', async (_req, res) => {
  try {
    await prisma.$queryRaw`SELECT 1`;
    res.json({ status: 'db ok' });
  } catch (error) {
    res.status(500).json({ status: 'db error', error });
  }
});

const port = Number(process.env.PORT || 3001);

app.listen(port, () => {
  console.log(`API running at http://localhost:${port}`);
});