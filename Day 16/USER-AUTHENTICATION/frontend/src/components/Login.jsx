import React, { useState } from 'react'
import { toast } from 'react-toastify'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Login = () => {

  const navigate = useNavigate()

  const [loginData, setLoginData] = useState({
    email: "",
    password: ""
  })

  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handleOnChange = (e) => {
    setLoginData({...loginData, [e.target.name]: e.target.value})
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const {email, password} = loginData
    if (!email || !password) {
      setError("All fields are required")
    } else {
      setIsLoading(true)
      const res = await axios.post("http://localhost:8000/api/v1/auth/login/", loginData)

      const response = res.data
      setIsLoading(false)

      console.log(response)

      if (res.status === 200) {
        toast.success("Login Successful")
      }
    }
  }


  return (
    <div>
      <div className="form-container">
        <div style={{width:"100%"}} className="wrapper">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>

              {isLoading && (
                <p>Loading...</p>
              )}

                <div className="form-group">
                    <label>Email Address:</label>
                    <input
                        type="email"
                        className="email-form"
                        name="email"
                        value={loginData.email}
                        onChange={handleOnChange}
                    />
                </div>

                <div className="form-group">
                    <label>Password:</label>
                    <input
                        type="password"
                        className="email-form"
                        name="password"
                        value={loginData.password}
                        onChange={handleOnChange}
                    />
                </div>

                <input type="submit" value="Login" className="submitButton" />

            </form>


        </div>
      </div>
    </div>
  )
}

export default Login
