import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import { getStudents } from '../services/StudentService';
import "../App.css";


const Students = () => {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        let mounted = true;
        getStudents().then(data => {
            if (mounted) {
                setStudents(data)
            }
        });

        return () => mounted = false;
    }, []);

    return (
        <div>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Registration No.</th>
                        <th>Email</th>
                        <th>Course</th>
                    </tr>
                </thead>
                <tbody>
                    {students.map((student) =>
                        <tr key={student.id}>
                            <td>{student.student_id}</td>
                            <td>{student.first_name}</td>
                            <td>{student.last_name}</td>
                            <td>{student.reg_no}</td>
                            <td>{student.email}</td>
                            <td>{student.course}</td>
                        </tr>
                    )}
                </tbody>
            </Table>
        </div>
        
    );

};

export default Students;
