import React, { useState, useEffect } from 'react'
import axios from 'axios'
import "./main.css"

const App = () => {

    const [student, setStudent] = useState([])

    const [newStudent, setNewStudent] = useState({
        first_name: "",
        last_name: "",
        age: "",
        gender: "",
        grade: "",
        email: "",
        phone: "",
        address: "",
    })

    const [selectedStudent, setSelectedStudent] = useState(null)

    const [toView, setToView] = useState({
        first_name: "",
        last_name: "",
        age: "",
        gender: "",
        grade: "",
        email: "",
        phone: "",
        address: "",
    })

    const [openView, setOpenView] = useState(false);

    useEffect(() => {
        fetchStudents()
    }, [])


    const fetchStudents = () => {
        axios.get("http://localhost:8000/api/students/")
            .then(response => {
                console.log(response.data)
                setStudent(response.data)
            })
            .catch(error => {
                console.log(error)
            })
    }

    const handleInputChange = (event) => {
        setNewStudent({ ...newStudent, [event.target.name]: event.target.value })
        console.log(newStudent)
    }

    const handleAddStudent = () => {
        axios.post("http://localhost:8000/api/students/", newStudent)
            .then(response => {
                setStudent([...student, response.data])
                setNewStudent({
                    first_name: "",
                    last_name: "",
                    age: "",
                    gender: "",
                    grade: "",
                    email: "",
                    phone: "",
                    address: "",
                })
            })
            .catch(error => {
                console.error(error)
            })
    }

    const handleViewStudent = async (id) => {
        const response = await axios.get(`http://localhost:8000/api/students/${id}/`)
        setToView(response.data)
        setOpenView(true)
    }

    const handleEditStudent = (student) => {
        setSelectedStudent(student)
        setNewStudent(student);
    }

    const handleUpdateStudent = () => {
        axios.put(`http://localhost:8000/api/students/${selectedStudent.id}/`, newStudent)
        .then(response => {
            fetchStudents();
            setNewStudent({
                first_name: "",
                last_name: "",
                age: "",
                gender: "",
                grade: "",
                email: "",
                phone: "",
                address: "",
            })
        })
        .catch(error => {
            console.error(error)
        })
    }

    const handleCancelUpdateStudent = () => {
        setSelectedStudent(null)
        setNewStudent({
            first_name: "",
            last_name: "",
            age: "",
            gender: "",
            grade: "",
            email: "",
            phone: "",
            address: "",
        })
    }

    const handleDeleteStudent = (id) => {
        axios.delete(`http://localhost:8000/api/students/${id}/`)
        .then(response => {
            fetchStudents();
        })
        .catch(error => {
            console.error(error)
        })
    }


    return (
        <div className="app-container">

            <h1>Student Management System</h1>

            {/* Form Container */}
            <div className="form-container">

                <div className="form-inputs">

                    <input type="text" name="first_name" placeholder="First Name" value={newStudent.first_name} onChange={handleInputChange} />

                    <input type="text" name="last_name" placeholder="Last Name" value={newStudent.last_name} onChange={handleInputChange} />

                    <input type="number" name="age" placeholder="Age" value={newStudent.age} onChange={handleInputChange} />

                    <input type="text" name="gender" placeholder="Gender" value={newStudent.gender} onChange={handleInputChange} />

                    <input type="text" name="grade" placeholder="Grade" value={newStudent.grade} onChange={handleInputChange} />

                    <input type="email" name="email" placeholder="Email" value={newStudent.email} onChange={handleInputChange} />

                    <input type="text" name="phone" placeholder="Phone" value={newStudent.phone} onChange={handleInputChange} />

                    <textarea name="address" placeholder="Address" value={newStudent.address} onChange={handleInputChange} />

                    <div className="form-buttons">
                        {
                            selectedStudent ? (
                                <>
                                    <button
                                        onClick={handleUpdateStudent}
                                    >
                                        Update
                                    </button>

                                    <button
                                        onClick={handleCancelUpdateStudent}
                                    >
                                        Cancel
                                    </button>
                                </>
                            ) : (
                                <button
                                    onClick={handleAddStudent}>
                                    Add New Student
                                </button>
                            )
                        }
                    </div>

                </div>

            </div>

            {/* Students List */}
            <ul className="student-list">
                {
                    student.map(student => (
                        <li key={student.id}>
                            <div>
                                <strong>
                                    {student.first_name} {student.last_name}
                                </strong>
                            </div>

                            <div className="actions">

                                <button
                                    className="view"
                                    onClick={() => handleViewStudent(student.id)}
                                >View
                                </button>

                                <button
                                    className="edit"
                                    onClick={() => handleEditStudent(student)}
                                >Edit
                                </button>

                                <button
                                    className="delete"
                                    onClick={() => handleDeleteStudent(student.id)}
                                >Delete</button>

                            </div>
                        </li>
                    ))
                }
            </ul>

            {/* View Student */}
            {
                openView && (
                    <>
                        <div className="outer-box">

                            <strong>
                                {toView.first_name} {toView.last_name}
                            </strong>

                            <br />

                            <span>Age: {toView.age}</span>

                            <br />

                            <span>Gender: {toView.gender}</span>

                            <br />

                            <span>Grade: {toView.grade}</span>

                            <br />

                            <span>Email: {toView.email}</span>

                            <br />

                            <span>Phone: {toView.phone}</span>

                            <br />

                            <span>Address: {toView.address}</span>

                            <br />

                        </div>

                        <button
                            onClick={() => setOpenView(false)}
                        >
                            Close
                        </button>
                    </>


                )
            }

        </div>
    )
}

export default App
