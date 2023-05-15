import React from 'react';
import Client from "./Client";
import './style.css'
import Modal from "../Modal";
import EditClient from "./EditClient";

export default function ClientsList() {
    //  Todo: clients from back-end
    const clients: string[] = ["Генадий Пистолетов", "Анатолий Чертозвонцев", "Яша Лава"];
    return (
        <div className="ClientsList">
            {clients.map(c => <Client full_name={c}/>)}
        </div>
    );
}

