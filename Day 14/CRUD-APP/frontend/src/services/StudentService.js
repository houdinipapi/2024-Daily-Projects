import axios from 'axios';

export function getStudents() {
    return axios.get('http://127.0.0.1:8000/students/')
        .then(response => response.data);
}

export function addStudent(student) {
    return axios.post('http://127.0.0.1:8000/students/', {
        student_id: null,
        first_name: student.first_name,
        last_name: student.last_name,
        email: student.email,
        reg_no: student.reg_no,
        course: student.course
    })
        .then((response) => response.data);
}