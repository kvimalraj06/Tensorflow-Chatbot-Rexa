Chatbot-Rexa

Welcome to our Chatbot-Rexat! This repository contains the code for a Chatbot built using React, TensorFlow, Python FastAPI, and integrated with a MySQL database. The Chatbot has been designed with the following features:

Features:

- Query Handling: The Chatbot is capable of answering user queries using machine learning techniques implemented with TensorFlow.
- User Interaction: It can engage in interactive conversations with users, prompting for further details when needed to provide more accurate responses.
- Offensive Language Filtering: Offensive words are automatically detected and hidden during the conversation to maintain a respectful and safe environment.
- Chat History: The Chatbot saves the chat history of users, allowing for a seamless continuation of conversations across sessions.
- Query Logging: If the Chatbot encounters a query for which it has no answer, it logs the user's question for further training, improving its capabilities over time.

Technologies Used:

- TensorFlow: TensorFlow is used for building and training the machine learning model powering the Chatbot's response generation.
- React: The frontend interface of the Chatbot is built using React, providing a user-friendly and interactive experience.
- Python FastAPI: FastAPI is utilized to create the backend server, facilitating communication between the frontend and the machine learning model.
- MySQL Database: MySQL is integrated with the project to store chat histories and user queries for training purposes.

Getting Started:

To get started with the project, follow these steps:

Clone the Repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/kvimalraj06/Tensorflow-Chatbot-Rexa.git
Install Dependencies: Navigate to the project directory and install the required dependencies for both the frontend and backend:

bash
Copy code
cd chatbot-project
npm install          # Install frontend dependencies
pip install -r requirements.txt   # Install backend dependencies
Database Setup: Set up a MySQL database and configure the connection details in the backend configuration file.

Training the Model (Optional): 

If you want to train the Chatbot model further, you can provide additional training data and run the training script.

Run the Application: 

Start the backend server and frontend application:
- graphql
- Copy code
- uvicorn main:app --reload    # Run the FastAPI backend server
- npm start                     # Run the React frontend application
- Access the Chatbot: Once the server is running, access the Chatbot interface in your web browser.

Contribution Guidelines:

If you'd like to contribute to the project, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and ensure the code passes all tests.
- Submit a pull request detailing the changes you've made.

Thanks for visting my project. Happy Learning!!!
