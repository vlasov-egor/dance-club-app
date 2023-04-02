import React from 'react';
import './style.css'

interface ButtonProps {
    text: string
}

const Button = (props: ButtonProps): JSX.Element => {
    return (
        <div className="Button">
            <button>{props.text}</button>
        </div>
    )
}

export default Button;