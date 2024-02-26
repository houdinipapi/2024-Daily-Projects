import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Signup = () => {

    const [formData, setFormData] = useState({
        email: "",
        first_name: "",
        last_name: "",
        password: "",
        confirm_password: ""
    })

    const [error, setError] = useState("")

    const handleOnChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value})
    }

    const { email, first_name, last_name, password, confirm_password } = formData

    const handleSubmit = (e) => {
        e.preventDefault()
        if (!email || !first_name || !last_name || !password || !confirm_password) {
            console.log("All fields are required")
            setError("All fields are required")
        } else if (password !== confirm_password) {
            console.log("Passwords do not match")
            setError("Passwords do not match")
        } else {
            console.log(formData)

        }
    }

  return (
    <div>
      <div className="form-container">
        <div style={{width:"100%"}} className="wrapper">
            <h2>Create Account</h2>
            
            <form onSubmit={handleSubmit}>

                <p style={{color:"red", padding:"1px"}}>{ error ? error : "" }</p>

                <div className="form-group">
                    <label>Email Address: </label>
                    <input
                        type="email"
                        className="email-form"
                        name="email"
                        value={email}
                        onChange={handleOnChange}
                    />
                </div>

                <div className="form-group">
                    <label>First Name: </label>
                    <input
                        type="text"
                        className="email-form"
                        name="first_name"
                        value={first_name}
                        onChange={handleOnChange}
                    />
                </div>

                <div className="form-group">
                    <label>Last Name: </label>
                    <input
                        type="text"
                        className="email-form"
                        name="last_name"
                        value={last_name}
                        onChange={handleOnChange}
                    />
                </div>

                <div className="form-group">
                    <label>Password: </label>
                    <input
                        type="password"
                        className="email-form"
                        name="password"
                        value={password}
                        onChange={handleOnChange}
                    />
                </div>

                <div className="form-group">
                    <label>Confirm Password: </label>
                    <input
                        type="password"
                        className="confirm-password-form"
                        name="confirm_password"
                        value={confirm_password}
                        onChange={handleOnChange}
                    />
                </div>

                <input type="submit" value="Submit" className="submitButton" />

            </form>

            <h3 className="text-option">Or</h3>
            <div className="githubContainer">
                <button>Sign up with GitHub</button>
            </div>

            <div className="googleContainer">
                <button>Sign up with Google</button>
            </div>


        </div>
      </div>
    </div>
  )
}


export default Signup
