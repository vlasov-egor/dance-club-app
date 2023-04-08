import React from 'react';
import './App.css';
import Header from "./components/MainMenu/Header/Header";
import EntitiesMenu from "./components/MainMenu/EntitiesMenu/EntitiesMenu";

// let tg = window.Telegram.WebApp;

const App: React.FC = () => {
    return (
        <div className="App">
            <header>
                <Header/>
            </header>
            <main>
                <EntitiesMenu/>
            </main>
        </div>
    );
}

export default App;
