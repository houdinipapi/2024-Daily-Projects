import React, { useState } from 'react'
import axiosInstance from "../utils/AxiosInstance"
import { toast } from 'react-toastify'




const ForgetPassword = () => {

  const [email, setEmail] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (email) {
      const res = await axiosInstance.post("auth/password-reset/", {"email": email})

      if (res.status === 200) {
        console.log(res.data)
        toast.success("A link has been sent to your email address.")
      }
      console.log(res)
      setEmail("")
    }


  }

  return (
    <div>

      <h2>Enter your registered email address:</h2>
      <div className="wrapper">
        <form action="" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="">Email Address:</label>
            <input
              type="email"
              className="email-form"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <button className="vbtn">Send</button>
        </form>
      </div>
      
    </div>
  )
}


export default ForgetPassword
