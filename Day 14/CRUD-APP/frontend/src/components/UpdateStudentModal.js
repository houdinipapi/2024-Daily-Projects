import React from "react";
import { Modal, Button, Col, Row, Form } from "react-bootstrap";
import { updateStudent } from "../services/StudentService";



const UpdateStudentModal = (props) => {

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const studentData = Object.fromEntries(formData.entries());

        console.log("studentData:", studentData);

        updateStudent(studentData, props.student.student_id)
            .then((result) => {
                console.log("Student updated successfully!");
                alert(result);
                props.setUpdated(true);
            })
            .catch((error) => {
                console.error('Failed to update student:', error);
                alert("Failed to update student. Please try again.");
            });
    };



    return (
        <div className="container">
            <Modal
                {...props}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered
            >
                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Update Student Information
                    </Modal.Title>
                </Modal.Header>

                <Modal.Body>
                    <Row>
                        <Col sm={6}>
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="FirstName">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control
                                        type="text"
                                        name="first_name"
                                        required
                                        defaultValue={props.student.first_name}
                                        placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="LastName">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control
                                    type="text"
                                    name="last_name"
                                    required
                                    defaultValue={props.student.last_name}
                                    placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="RegistrationNo">
                                    <Form.Label>Registration No.</Form.Label>
                                    <Form.Control
                                    type="text"
                                    name="reg_no"
                                    required
                                    defaultValue={props.student.reg_no}
                                    placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="Email">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control
                                    type="text"
                                    name="email"
                                    required
                                    defaultValue={props.student.email}
                                    placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="Course">
                                    <Form.Label>Course</Form.Label>
                                    <Form.Control
                                    type="text"
                                    name="course"
                                    required
                                    defaultValue={props.student.course}
                                    placeholder="" />
                                </Form.Group>
                                <Form.Group>
                                    <p></p>
                                    <Button variant="primary" type="submit">
                                        Submit
                                    </Button>
                                </Form.Group>
                            </Form>
                        </Col>
                    </Row>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="danger" type="submit" onClick={props.onHide}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default UpdateStudentModal;