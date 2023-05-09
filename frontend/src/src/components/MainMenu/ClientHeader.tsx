import React from 'react';
import './style.css'

interface ClientProps {
    full_name: string
}

export function ClientHeader(props: ClientProps) {
    return (
        <div className="ClientHeader">{props.full_name}</div>
    );
}