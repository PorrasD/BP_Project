 import { useState } from 'react'
import API from '../api'

export default function Register() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await API.post('/register', { email, password })
      setMessage(res.data.message)
    } catch (err) {
      setMessage(err.response.data.error)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" onChange={e => setPassword(e.target.value)} placeholder="Password" required />
      <button type="submit">Register</button>
      <p>{message}</p>
    </form>
  )
}
