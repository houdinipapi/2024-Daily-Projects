import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify';

const VerifyEmail = () => {
  const [otp, setOtp] = useState("")

  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (otp) {
      const response = await axios.post("http://localhost:8000/api/v1/auth/verify/", {"otp": otp})
      if (response.status === 200) {
        navigate("/login")
        toast.success(response.data.message)
      }

    }
  }



  return (
    <div>
      <div className="form-container">

        <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="">Enter your OTP Code:</label>
          <input
            type="text"
            className="email-form"
            name="otp"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
          />
        </div>
        <input type="submit" value="Send" className="vbtn" />
        </form>

      </div>
    </div>
  )
}

export default VerifyEmail
