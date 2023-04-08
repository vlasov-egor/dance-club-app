import React from 'react';
import './style.css'

interface HeaderProps {
    text: string;
}

const WidgetHeader = (props: HeaderProps): JSX.Element => {
    return (
        <div className="WidgetHeader">
            {props.text}
        </div>
    )
}

export default WidgetHeader;