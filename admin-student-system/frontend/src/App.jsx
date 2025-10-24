import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = 'http://localhost:4000/students'

function App() {
  const [students, setStudents] = useState([])
  const [editingStudent, setEditingStudent] = useState(null)
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    course: ''
  })
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetchStudents()
  }, [])

  const fetchStudents = async () => {
    try {
      const response = await axios.get(API_URL)
      setStudents(response.data)
    } catch (error) {
      showMessage('Error loading students', 'error')
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      if (editingStudent) {
        // Update student
        await axios.put(`${API_URL}/${editingStudent.id}`, formData)
        showMessage('Student updated successfully!', 'success')
      } else {
        // Add new student
        await axios.post(API_URL, formData)
        showMessage('Student added successfully!', 'success')
      }
      resetForm()
      fetchStudents()
    } catch (error) {
      showMessage(error.response?.data?.error || 'Error saving student', 'error')
    }
  }

  const handleEdit = (student) => {
    setEditingStudent(student)
    setFormData({
      name: student.name,
      email: student.email,
      course: student.course
    })
  }

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await axios.delete(`${API_URL}/${id}`)
        showMessage('Student deleted successfully!', 'success')
        fetchStudents()
      } catch (error) {
        showMessage('Error deleting student', 'error')
      }
    }
  }

  const resetForm = () => {
    setFormData({ name: '', email: '', course: '' })
    setEditingStudent(null)
  }

  const showMessage = (text, type) => {
    setMessage({ text, type })
    setTimeout(() => setMessage(''), 3000)
  }

  return (
    <div className="app">
      <h1>🎓 Admin Student System</h1>
      
      {message && (
        <div className={`message ${message.type}`}>
          {message.text}
        </div>
      )}

      {/* Student Form */}
      <form onSubmit={handleSubmit} className="student-form">
        <h2>{editingStudent ? 'Edit Student' : 'Add New Student'}</h2>
        
        <input
          type="text"
          placeholder="Full Name"
          value={formData.name}
          onChange={(e) => setFormData({...formData, name: e.target.value})}
          required
        />
        
        <input
          type="email"
          placeholder="Email Address"
          value={formData.email}
          onChange={(e) => setFormData({...formData, email: e.target.value})}
          required
        />
        
        <input
          type="text"
          placeholder="Course"
          value={formData.course}
          onChange={(e) => setFormData({...formData, course: e.target.value})}
          required
        />
        
        <div className="form-buttons">
          <button type="submit" className="btn-primary">
            {editingStudent ? 'Update Student' : 'Add Student'}
          </button>
          {editingStudent && (
            <button type="button" onClick={resetForm} className="btn-secondary">
              Cancel
            </button>
          )}
        </div>
      </form>

      {/* Students List */}
      <div className="students-list">
        <h2>Students ({students.length})</h2>
        
        {students.length === 0 ? (
          <p className="no-students">No students found. Add your first student!</p>
        ) : (
          <div className="students-grid">
            {students.map(student => (
              <div key={student.id} className="student-card">
                <div className="student-info">
                  <h3>{student.name}</h3>
                  <p>📧 {student.email}</p>
                  <p>📚 {student.course}</p>
                  <small>Joined: {new Date(student.created_at).toLocaleDateString()}</small>
                </div>
                
                <div className="student-actions">
                  <button 
                    onClick={() => handleEdit(student)}
                    className="btn-edit"
                  >
                    Edit
                  </button>
                  <button 
                    onClick={() => handleDelete(student.id)}
                    className="btn-delete"
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default App