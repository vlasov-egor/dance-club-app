import React from 'react';
import MenuButton from "./MenuButton";


export function MainMenu() {
    return (
        <div className="MainMenu">
            <MenuButton text={"Клиенты"} img={"/imgs/ClientsLogo.svg"}/>
            <MenuButton text={"Расписание"} img={"/imgs/Calendar.svg"}/>
            <MenuButton text={"Абонементы"} img={"/imgs/Membership.svg"}/>
        </div>
    );
}