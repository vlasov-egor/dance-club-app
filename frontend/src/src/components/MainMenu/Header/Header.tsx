import React from 'react';
import './style.css'
import FullNameHeader from "./FullNameHeader";
import WidgetHeader from "./WidgetHeader";

const Header = (): JSX.Element => {
    return (
        <div className="Header">
            <FullNameHeader text="Иванов Иван Иванович"/>
            <WidgetHeader text="Ближайшее занятие 12.12.2012"/>
        </div>

    )
}

export default Header;