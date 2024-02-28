import { useState } from 'react'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Signup, Login, VerifyEmail, Profile, ForgetPassword } from './components';
import './App.css'
import ResetPassword from './components/ResetPassword';




function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Router>
        <ToastContainer />
        <Routes>
          <Route path="/" element={<Signup/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/otp/verify" element={<VerifyEmail/>} />
          <Route path="/dashboard" element={<Profile/>} />
          <Route path="/forget-password" element={<ForgetPassword/>} />
          <Route path="/password-reset-confirm/:uid/:token" element={<ResetPassword/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App
