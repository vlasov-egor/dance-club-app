import React from 'react';
import './style.css'
import MenuButton from "./MenuButton";

const EntitiesMenu = (): JSX.Element => {
    return (
        <div className="EntitiesMenu">
            <div className="inner">
                <MenuButton text="Клиенты"/>
                <MenuButton text="Занятия"/>
                <MenuButton text="Еще что-то"/>
            </div>
        </div>
    )
}

export default EntitiesMenu;