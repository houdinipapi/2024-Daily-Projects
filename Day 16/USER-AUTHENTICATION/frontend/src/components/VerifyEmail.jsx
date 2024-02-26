import React, { useState } from 'react'

const VerifyEmail = () => {
  return (
    <div>
      <div className="form-container">

        <form action="">
        <div className="form-group">
          <label htmlFor="">Enter your OTP Code:</label>
          <input
            type="text"
            className="email-form"
            name="otp"
          />
        </div>
        <input type="submit" value="Send" className="vbtn" />
        </form>

      </div>
    </div>
  )
}

export default VerifyEmail
