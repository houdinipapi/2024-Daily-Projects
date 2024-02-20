import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

import { Button, ButtonToolbar } from 'react-bootstrap';
import { getStudents, deleteStudent } from '../services/StudentService';
import AddStudentModal from './AddStudentModal';


const Manage = () => {
    const [students, setStudents] = useState([]);
    const [addModalShow, setAddModalShow] = useState(false);


    useEffect(() => {
        let mounted = true;
        getStudents().then(data => {
            if (mounted) {
                setStudents(data)
            }
        });

        return () => mounted = false;
    }, []);

    const handleAdd = (e) => {
        e.preventDefault();
        setAddModalShow(true);

        console.log('Add button clicked');
    };

    let AddModelClose = () => setAddModalShow(false);



    return (
        <div className="row side-row">
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Registration No.</th>
                        <th>Email</th>
                        <th>Course</th>
                        <th>Actions</th>
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
                            <td>
                                <Button
                                    className="mr-2"
                                    variant="outline-primary"
                                >
                                    Update
                                </Button>{" "}

                                <Button
                                    className="mr-2"
                                    variant="danger"
                                >
                                    Delete
                                </Button>{" "}
                            </td>
                        </tr>
                    )}
                </tbody>
            </Table>

            <ButtonToolbar>
                <Button
                    variant="success"
                    onClick={handleAdd}
                >
                    Add Student
                </Button>{" "}
            </ButtonToolbar>

            <AddStudentModal
                show={addModalShow}
                onHide={AddModelClose}
            />

        </div>

    );

};

export default Manage;