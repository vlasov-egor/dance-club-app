import React from 'react';
import './App.css';
import Header from "./components/Header/Header";
import Button from "./components/Button/Button"

const App: React.FC = () => {
    return (
        <div className="App">
            <header>
                <Header text={"Имя Фамилия"}/>
                <Header text={"Какая-нибудь другая инфа(ближайшее занятие или и т.д.)"}/>
            </header>
            <main>
                <Button text={"Клиенты"}/>
                <Button text={"Занятия"}/>
                <Button text={"Абонементы"}/>
            </main>
        </div>
    );
}

export default App;
