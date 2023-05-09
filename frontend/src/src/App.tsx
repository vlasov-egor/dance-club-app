import React from 'react';
import './App.css';
import {ClientHeader} from "./components/MainMenu/ClientHeader";
import {MainMenu} from "./components/MainMenu/MainMenu";

function App() {
    return (
        <div className="App">
            <header>
                <ClientHeader full_name={"Антон Пупкин"}/>
            </header>
            <footer>
                <MainMenu/>
            </footer>
        </div>
    );
}

export default App;
