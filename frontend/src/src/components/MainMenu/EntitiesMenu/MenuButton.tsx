import React from 'react';
import './style.css'

interface HeaderProps {
    text: string;
}

const MenuButton = (props: HeaderProps): JSX.Element => {
    return (
        <div className="MenuButton">
            <button>{props.text}</button>
        </div>
    )
}

export default MenuButton;