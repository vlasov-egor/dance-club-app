import React from 'react';

interface ButtonProps {
    text: string,
    img: string
}

function MenuButton(props: ButtonProps) {
    return (
        <div className="MenuButton">
            <button>
                <div className="MenuButtonText">{props.text}</div>
                <img className="MenuButtonImage" src={props.img} alt="menu_img"/>
            </button>
        </div>
    );
}

export default MenuButton;