# Eclipse - Enhanced Cognitive Linguistic Interactive Personal Support Engine
> A speech-to-text and text-to-speech assistant with interactive AI capabilities.

## About Eclipse
Eclipse is an AI-powered **speech-to-text and text-to-speech chatbot** that provides an interactive and personalized user experience. It integrates **Flask**, **MySQL**, and **LLM models** to ensure smooth and efficient conversations.

#### Features
-  **Speech-to-Text & Text-to-Speech** integration  
-  **AI-powered interactions** using advanced NLP models  
-  **User memory persistence** via MySQL  
-  **Web-based UI** with a clean and interactive design  
-  **Real-time text transcription and audio output**

---

##  Project Structure
ECLIPSEV2.0/
│── audio/                    # Handles audio processing
│   ├── audioManager.py
│   ├── audioTranscriber.py
│── eclipse2/                 # Virtual environment (ignored in Git)
│── models/                   # AI and NLP models
│   ├── nlpModels.py
│── static/                   # CSS, JS, and frontend static files
│   ├── script.js
│   ├── styles.css
│── templates/                # HTML templates for the UI
│   ├── login.html
│   ├── main_interface.html
│   ├── signup.html
│── utils/                    # Helper functions and scripts
│   ├── ModelUtils.py
│   ├── datasetUtils.py
│   ├── ttsService.py
│── app.py                    # Main Flask application
│── config.py                 # Configuration file
│── test.py                   # Test scripts
│── .gitignore                # Files and folders to ignore in Git
│── README.md                 # Documentation file
│── requirements.txt           # Project dependencies
│── get-pip.py                # Python package installer


Installation & Setup
1. Install Dependencies
pip install -r requirements.txt

2. Set Up Database
	1.	Create a MySQL database.
	2.	Configure your credentials in config.py.

3. Run the Application
python app.py

📌 Usage
1.	Log in using a simple sign-up system.
2.	Speak or type your queries.
3.	Eclipse responds with text or voice.
4.	View chat history from the side panel.

⚡ Tech Stack
- Backend: Flask, Python
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- AI Models: Llama 3.1, NLP models
- APIs: Google Text-to-Speech

- 📧 Email: soumyamaheshwari1234@gmail.com 
- 💬 Twitter: @Soumymaheshwri
