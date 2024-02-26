import React, { useState } from 'react'

const Signup = () => {
  return (
    <div>
      <div className="form-container">
        <div style={{width:"100%"}} className="wrapper">
            <h2>Create Account</h2>
            <form>

                <div className="form-group">
                    <label>Email Address: </label>
                    <input
                        type="email"
                        className="email-form"
                        name="email"
                    />
                </div>

                <div className="form-group">
                    <label>First Name: </label>
                    <input
                        type="text"
                        className="email-form"
                        name="first_name"
                    />
                </div>

                <div className="form-group">
                    <label>Last Name: </label>
                    <input
                        type="text"
                        className="email-form"
                        name="last_name"
                    />
                </div>

                <div className="form-group">
                    <label>Password: </label>
                    <input
                        type="password"
                        className="email-form"
                        name="password"
                    />
                </div>

                <div className="form-group">
                    <label>Confirm Password: </label>
                    <input
                        type="password"
                        className="confirm-password-form"
                        name="confirm_password"
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
