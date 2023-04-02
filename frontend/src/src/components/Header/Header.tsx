import React from 'react';
import './style.css'

interface HeaderProps {
    text: string;
}

const Header = (props: HeaderProps): JSX.Element => {
    return (
        <div className="Header">
            {props.text}
        </div>
    )
}

export default Header;