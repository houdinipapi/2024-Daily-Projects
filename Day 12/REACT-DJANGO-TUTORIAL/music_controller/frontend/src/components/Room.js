import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';

function Room() {
    const { roomCode } = useParams();
    const [state, setState] = useState({
        votesToSkip: 2,
        guestCanPause: false,
        isHost: false,
    });

    useEffect(() => {
        getRoomDetails();
    }, []);

    function getRoomDetails() {
        fetch("/api/room/" + roomCode)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error fetching room details');
                }
                return response.json();
            })
            .then((data) => {
                setState({
                    votesToSkip: data.votes_to_skip,
                    guestCanPause: data.guest_can_pause,
                    isHost: data.is_host
                });
            })
            .catch((error) => {
                console.error('Error fetching room details:', error);
            });
    }

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