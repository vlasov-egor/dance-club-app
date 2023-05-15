import React, {useState} from 'react';
import EditClient from "./EditClient";
import Modal from "../Modal";

interface ClientProps {
    full_name: string
}

export default function Client(props: ClientProps) {
    const [modal, setModal] = useState(false);
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
                <button onClick={() => setModal(true)}>
                    <img src={"/imgs/InfoLogo.svg"} alt={"Info"}></img>
                </button>
            </div>
            {modal &&
                <Modal title="Изменить пользователя" onClose={() => setModal(false)}>
                    <EditClient onUpdate={() => {
                        setModal(false)
                    }}/>
                </Modal>}
            {/*    Todo: add client button */}
        </div>
    );
}
