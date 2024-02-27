import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import AxiosInstance from '../utils/AxiosInstance'
import { toast } from 'react-toastify'



const Profile = () => {

  const navigate = useNavigate()

  const user = JSON.parse(localStorage.getItem("user"))

  const jwt_access = localStorage.getItem("token")

  useEffect(() => {
    if (jwt_access === null && !user) {
      navigate("/login")
    } else {
      getSomeData()
    }
  }, [jwt_access, user])


  const getSomeData = async () => {
    
      const resp = await AxiosInstance.get("auth/test-auth/")
      if (resp.status === 200) {
        console.log(resp.data);
      }
    }

  const refresh = localStorage.getItem("refresh")

  const handleLogout = async () => {
    const res = await AxiosInstance.post("auth/logout/", {"refresh_token": refresh})
    if (res.status === 200) {
      localStorage.removeItem("access")
      localStorage.removeItem("refresh")
      localStorage.removeItem("user")
      navigate("/login")

      toast.warn("You have been logged out!")
    }
  }

  return (
    <div className="container">
      
      <h2>Hi, { user && user.names }</h2>

      <p style={{textAlign:"center"}}>Welcome to your profile!</p>

      <button
        className="logout-btn"
        onClick={handleLogout}
      >
        Logout
      </button>

    </div>
  )
}

export default Profile
