import express from 'express';
import { pool } from '../db.js';

const router = express.Router();

// GET all students
router.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM students ORDER BY id');
    res.json(result.rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// GET student by ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query('SELECT * FROM students WHERE id = $1', [id]);
    
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Student not found' });
    }
    
    res.json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// POST new student
router.post('/', async (req, res) => {
  try {
    const { name, email, course } = req.body;
    
    if (!name || !email || !course) {
      return res.status(400).json({ error: 'Name, email and course are required' });
    }

    const result = await pool.query(
      'INSERT INTO students (name, email, course) VALUES ($1, $2, $3) RETURNING *',
      [name, email, course]
    );
    res.status(201).json(result.rows[0]);
  } catch (error) {
    if (error.code === '23505') { // Unique violation
      res.status(400).json({ error: 'Email already exists' });
    } else {
      res.status(500).json({ error: error.message });
    }
  }
});

// PUT update student
router.put('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, course } = req.body;
    
    if (!name || !email || !course) {
      return res.status(400).json({ error: 'Name, email and course are required' });
    }

    const result = await pool.query(
      'UPDATE students SET name = $1, email = $2, course = $3 WHERE id = $4 RETURNING *',
      [name, email, course, id]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Student not found' });
    }
    
    res.json(result.rows[0]);
  } catch (error) {
    if (error.code === '23505') {
      res.status(400).json({ error: 'Email already exists' });
    } else {
      res.status(500).json({ error: error.message });
    }
  }
});

// DELETE student
router.delete('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query('DELETE FROM students WHERE id = $1 RETURNING *', [id]);
    
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Student not found' });
    }
    
    res.json({ message: 'Student deleted successfully', student: result.rows[0] });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

export default router;