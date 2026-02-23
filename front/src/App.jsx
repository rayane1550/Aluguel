import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './pages/login' // Mudei para Login com L maiúsculo
import HomeUser from './pages/home_user'

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/homeuser" element={<HomeUser />} />
      </Routes>
    </Router>
  )
}