import React from 'react';

interface ModalProps {
    children: React.ReactNode
    title: string
    onClose: () => void
}

export default function Modal({children, title, onClose}: ModalProps) {
    return (
        <div className="Modal">
            <div className="ModalData">
                <button className="ModalExitButton" onClick={onClose}>
                    <img src="/imgs/CloseLogo.svg" alt="CloseLogo"></img>
                </button>
                <div className="ModalTitle">{title}</div>
                {children}
            </div>
        </div>
    );
}
