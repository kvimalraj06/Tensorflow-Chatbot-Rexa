import React from 'react';
import ChatWidget from './components/ChatWidget';
import './css/styling.css';

class App extends React.Component {
    render(){
        return (
            <div>
                <div className="background">
                    <h1 className="header">Welcome to Rexa</h1>
                </div>
                <ChatWidget />
            </div>
        );
    }
}

export default App;