import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axiosInstance from '../utils/AxiosInstance'
import { toast } from 'react-toastify'



const Profile = () => {


  const jwt_access = localStorage.getItem("token")

  const user = JSON.parse(localStorage.getItem("user"))

  const navigate = useNavigate();

  useEffect(() => {
    if (jwt_access === null && !user) {
      navigate("/login")
    } else {
      getSomeData()
    }
  }, [jwt_access, user])

   const refresh = JSON.parse(localStorage.getItem("refresh"))


  const getSomeData = async () => {

    console.log("Getting some data")

    const resp = await axiosInstance.get("auth/test-auth/")

    if (resp.status === 200) {
      console.log(resp.data);

    }
  }


  const handleLogout = async () => {
    const res = await axiosInstance.post("auth/logout/", {"refresh_token": refresh})
    if (res.status === 200) {
      localStorage.removeItem("access")
      localStorage.removeItem("refresh_token")
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
