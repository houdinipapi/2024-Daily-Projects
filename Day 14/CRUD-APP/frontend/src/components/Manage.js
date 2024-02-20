import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

import { Button, ButtonToolbar } from 'react-bootstrap';
import { FaEdit } from 'react-icons/fa';
import { RiDeleteBin5Line } from 'react-icons/ri';
import { getStudents, deleteStudent } from '../services/StudentService';
import AddStudentModal from './AddStudentModal';
import UpdateStudentModal from './UpdateStudentModal';


const Manage = () => {
    const [students, setStudents] = useState([]);
    const [addModalShow, setAddModalShow] = useState(false);
    const [editModalShow, setEditModalShow] = useState(false);
    const [editStudent, setEditStudent] = useState([]);
    const [isUpdated, setIsUpdated] = useState(false);


    useEffect(() => {
        let mounted = true;

        if (students.length > 0 && !isUpdated) {
            return;
        }
        getStudents().then(data => {
            if (mounted) {
                setStudents(data);
            }
        });

        return () => {
            mounted = false;
            setIsUpdated(false);
        }
    }, [isUpdated,students]);

    const handleAdd = (e) => {
        e.preventDefault();
        setAddModalShow(true);

        console.log('Add button clicked');
    };

    const handleUpdate = (e, student) => {
        e.preventDefault();
        setEditModalShow(true);
        setEditStudent(student);
        };

    const handleDelete = (e, student_id) => {
        if(window.confirm('Are you sure?')){
            e.preventDefault();
            deleteStudent(student_id)
            .then((result) => {
                alert(result);
                setIsUpdated(true);
            },
            (error) => {
                console.error('Failed to delete student:', error);
                alert("Failed to delete student. Please try again.");
            });
        }
    };

    let AddModelClose = () => setAddModalShow(false);
    let EditModelClose = () => setEditModalShow(false);



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
                                    variant="primary"
                                    onClick={event => handleUpdate(event, student)}
                                >
                                    <FaEdit />
                                </Button>
                                
                                <span>&nbsp;&nbsp;</span>

                                <Button
                                    className="mr-2"
                                    variant="danger"
                                    onClick={event => handleDelete(event, student.student_id)}
                                >
                                    <RiDeleteBin5Line />
                                </Button>

                                <UpdateStudentModal
                                    show={editModalShow}
                                    onHide={EditModelClose}
                                    student={editStudent}
                                    setUpdated={setIsUpdated}
                                />

                                
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
                setUpdated={setIsUpdated}
            />

        </div>

    );

};

export default Manage;