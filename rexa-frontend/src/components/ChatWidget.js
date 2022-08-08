import React, { useEffect } from 'react';
import { Widget, addResponseMessage } from 'react-chat-widget';
import bot from '../logo/bot.png';

import 'react-chat-widget/lib/styles.css';
import axios from'axios';

const ChatWidget = () => {

    useEffect(() => {
        addResponseMessage('Hello, I am rexa. How can I help you ?');
      }, []);
    

    const handleNewUserMessage = async (newMessage) => {

        const response = await axios.get('http://127.0.0.1:8000/msg',{
            params: {query: newMessage},
        })
        addResponseMessage(response.data.bot_response);

    };

    return (
        <div className="App">
        <Widget
            handleNewUserMessage={handleNewUserMessage}
            title="Rexa"
            subtitle=""
            profileAvatar = {bot}
        />
        </div>
    );
    }

export default ChatWidget;