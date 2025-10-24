import express from 'express';
import cors from 'cors';
import studentRoutes from './routes/students.js';
import { connectDB } from './db.js';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

// Routes
app.use('/students', studentRoutes);

app.get('/', (req, res) => {
  res.json({ message: 'Admin Student System API' });
});

// Mantener el proceso activo
process.on('SIGTERM', () => {
  console.log('Received SIGTERM, keeping server alive...');
});

process.on('SIGINT', () => {
  console.log('Received SIGINT, keeping server alive...');
});

// Conectar e iniciar
connectDB().then(() => {
  const server = app.listen(PORT, '0.0.0.0', () => {
    console.log(`✅ Server running on port ${PORT}`);
  });
  
  // Mantener el proceso activo
  const keepAlive = setInterval(() => {
    if (!server.listening) {
      clearInterval(keepAlive);
    }
  }, 1000);
}).catch(error => {
  console.error('❌ Failed to start server:', error);
});