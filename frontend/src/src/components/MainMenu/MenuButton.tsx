import React from 'react';
import Client from "../Clients/Client";

interface ButtonProps {
    text: string,
    img: string,
    onClick: React.Dispatch<React.SetStateAction<string>>
}

function MenuButton(props: ButtonProps) {
    return (
        <div className="MenuButton">
            <button onClick={() => props.onClick(props.text)}>
                <div className="MenuButtonText">{props.text}</div>
                <img className="MenuButtonImage" src={props.img} alt="menu_img"/>
            </button>
        </div>
    );
}

export default MenuButton;