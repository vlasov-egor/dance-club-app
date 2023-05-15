import React, {useState} from 'react';
import './App.css';
import {ClientHeader} from "./components/MainMenu/ClientHeader";
import ClientsList from "./components/Clients/ClientsList";
import MenuButton from "./components/MainMenu/MenuButton";

function App() {
    const [state, setState] = useState("");
    console.log(state)
    switch (state) {
        case "Клиенты":
            return <ClientsList/>;
        case "Расписание":
            return <ClientsList/>;
        case "Абонементы":
            return <ClientsList/>;
        default:
            return (
                <div className="App">
                    <header>
                        <ClientHeader full_name={"Антон Пупкин"}/>
                    </header>
                    <footer>
                        <div className="MainMenu">
                            <MenuButton
                                text={"Клиенты"}
                                img={"/imgs/ClientsLogo.svg"}
                                onClick={setState}
                            />
                            <MenuButton
                                text={"Расписание"}
                                img={"/imgs/Calendar.svg"}
                                onClick={setState}
                            />
                            <MenuButton
                                text={"Абонементы"}
                                img={"/imgs/Membership.svg"}
                                onClick={setState}
                            />
                        </div>
                    </footer>
                </div>
            );
    }
}

export default App;
