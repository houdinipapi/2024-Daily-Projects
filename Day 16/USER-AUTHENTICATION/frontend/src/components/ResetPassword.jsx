import React, {useState} from 'react'
import { useNavigate, useParams } from 'react-router-dom';
import axiosInstance from '../utils/AxiosInstance';
import { toast } from 'react-toastify';



const ResetPassword = () => {

    const navigate = useNavigate()

    const {uid, token} = useParams()

    const [newPasswords, setNewPasswords] = useState({
        password: "",
        confirm_password: ""
    })

    const handleChange = (e) => {
        setNewPasswords({...newPasswords, [e.target.name]: e.target.value})
    }

    const data = {
        "password": newPasswords.password,
        "confirm_password": newPasswords.confirm_password,
        "uidb64": uid,
        "token": token
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        // Make API call
        const response = await axiosInstance.patch("auth/set-new-password/", data)
        const result = response.data

        if (response.status === 200) {
            console.log(result)
            navigate("/login")
            toast.success(response.message)
        }

    }


  return (
    <div>
        <div className="form-container">
            <div className="wrapper" style={{width:"100%"}}>
                <h2>Reset Password</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="">Password:</label>
                        <input
                            type="password"
                            className="email-form"
                            name="password"
                            value={newPasswords.password}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="">Confirm Password:</label>
                        <input
                            type="password"
                            className="email-form"
                            name="confirm_password"
                            value={newPasswords.confirm_password}
                            onChange={handleChange}
                        />
                    </div>
                    <button type="submit" className="vbtn">Reset</button>
                </form>

            </div>
        </div>
      
    </div>
  )
}

export default ResetPassword
