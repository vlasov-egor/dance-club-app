import React from 'react';
import './style.css'

interface HeaderProps {
    text: string;
}

const FullNameHeader = (props: HeaderProps): JSX.Element => {
    return (
        <div className="FullNameHeader">
            {props.text}
        </div>
    )
}

export default FullNameHeader;