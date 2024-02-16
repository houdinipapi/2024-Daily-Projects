import React, { useState } from "react";
import { useParams } from 'react-router-dom';

function Room() {
    const { roomCode } = useParams();
    const [state, setState] = useState({
        votesToSkip: 2,
        guestCanPause: false,
        isHost: false,
    });

    return (
        <div>
            <h3>{roomCode}</h3>
            <p><strong>Votes: </strong>{state.votesToSkip}</p>
            <p><strong>Guest Can Pause: </strong>{state.guestCanPause.toString()}</p>
            <p><strong>Host: </strong>{state.isHost.toString()}</p>
        </div>
    );
}

export default Room;