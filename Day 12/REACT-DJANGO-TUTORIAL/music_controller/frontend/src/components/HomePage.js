import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Room from "./Room";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path="/" element={<h1>Home Page</h1>} />
                    <Route path="/join" element={<RoomJoinPage/>} />
                    <Route path="/create" element={<CreateRoomPage/>} />
                    <Route path="/room/:roomCode" element={<Room/>} />
                </Routes>
            </Router>
        );
    }
}