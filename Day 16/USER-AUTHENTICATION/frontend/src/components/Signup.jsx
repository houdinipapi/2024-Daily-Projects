import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify';

const Signup = () => {

    const navigate = useNavigate()

    const [formData, setFormData] = useState({
        email: "",
        first_name: "",
        last_name: "",
        password: "",
        password2: ""
    })

    const [error, setError] = useState("")

    const handleOnChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value})
    }

    const { email, first_name, last_name, password, password2 } = formData

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!email || !first_name || !last_name || !password || !password2) {
            console.log("All fields are required")
            setError("All fields are required")
        } else if (password !== password2) {
            console.log("Passwords do not match")
            setError("Passwords do not match")
        } else {
            console.log(formData)

            // Make call to the api
            const res = await axios.post("http://localhost:8000/api/v1/auth/register/", formData)

            // Check out the response
            const response = res.data
            console.log(response)
            
            if (res.status === 201) {
                // Redirect to the VerifyEmail component
                navigate("/otp/verify")
                toast.success(response.message)


                console.log(res.data)
                setError(res.data.message)
            }

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
                        name="password2"
                        value={password2}
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
