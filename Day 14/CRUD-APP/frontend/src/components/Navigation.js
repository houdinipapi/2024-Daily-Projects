import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import logo from "../static/img/logo.png";
import "../App.css";



const Navigation = () => {
    return (
        <div>
            <Navbar bg="dark" variant="dark" expand="lg" id="my-nav">
                <Navbar.Brand href="/">
                    <img
                        alt=""
                        src={logo}
                        width="40"
                        height="50"
                        className="d-inline-block align-center"
                    />{' '}
                    Student Management Application
                </Navbar.Brand>
            </Navbar>
        </div>
    );
};

export default Navigation;