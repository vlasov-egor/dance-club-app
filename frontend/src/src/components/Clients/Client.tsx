import React from 'react';

interface ClientProps {
    full_name: string
}

function Client(props: ClientProps) {
    return (
        <div className="Client">
            <div className="ClientItem ClientName">
                {props.full_name}
            </div>
            <div className="ClientItem ClientState">
                {"Активен"}
            </div>
            <div className="ClientItem ClientSessions">
                {"1/10"}
            </div>
            <div className="ClientItem ClientEndDate">
                {"04.06.23"}
            </div>
            <div className="ClientItem ClientInfoButton">
                <button>
                    <img src={"/imgs/InfoLogo.svg"} alt={"Info"}></img>
                </button>
            </div>
        </div>
    );
}

export default Client;