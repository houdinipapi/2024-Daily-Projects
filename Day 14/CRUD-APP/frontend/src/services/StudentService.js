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

export function updateStudent(student, student_id) {
    return axios.put("http://127.0.0.1:8000/students/" + student_id + "/", {
        first_name: student.first_name,
        last_name: student.last_name,
        email: student.email,
        reg_no: student.reg_no,
        course: student.course
    })
        .then((response) => response.data);
}

export function deleteStudent(student_id) {
    return axios.delete("http://127.0.0.1:8000/students/" + student_id + "/", {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
        .then((response) => response.data);
}