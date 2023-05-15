import React, {useState} from 'react';

interface EditClientProps {
    onUpdate: () => void
}

export default function EditClient({onUpdate}: EditClientProps) {
    const [state, setState] = useState('');
    const submitHandler = (event: React.FormEvent) => {
        event.preventDefault();
        //  client.name = state if any
        //  PUT to back
        onUpdate();
    }

    return (
        <form className="EditClientForm" onSubmit={submitHandler}>
            <input type="text" className="EditClientFormInput" placeholder="Имя"
                   onChange={(event) => {
                       setState(event.target.value);
                   }}></input>
            <input type="text" className="EditClientFormInput" placeholder="Дата рождения"></input>
            <input type="text" className="EditClientFormInput" placeholder="Количество занятий"></input>
            <button className="EditClientFormButton UpdateButton">Изменить</button>
            <button className="EditClientFormButton DeleteButton">Удалить</button>
        </form>
    );
}