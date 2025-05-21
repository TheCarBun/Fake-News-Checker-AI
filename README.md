# [AI Fact Checker](https://isitfakenews.streamlit.app/)

[AI Fact Checker](https://isitfakenews.streamlit.app/) is a simple web application that allows users to verify facts and claims using an AI-powered backend. The app is built with Streamlit for the user interface and leverages a Langflow API endpoint for fact-checking responses.

Check it out here 👉🏼 https://isitfakenews.streamlit.app/

## Features

- **User-friendly UI:** Enter any query or claim in a text box.
- **AI-powered fact checking:** Queries are sent to a Langflow-powered API for analysis.
- **Instant results:** Get clear, concise fact-checking output in seconds.

## How It Works

1. The user enters a query or statement to be fact-checked.
2. Upon clicking the "Fact Check" button, the app sends the input to a Langflow API endpoint.
3. The API processes the input and returns a fact-checked response.
4. The result is displayed in the Streamlit app.

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://docs.streamlit.io/library/get-started/installation)
- [requests](https://pypi.org/project/requests/)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/TheCarBun/Fake-News-Checker-AI.git
cd "Fake News Checker AI"
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure API credentials:**

- **Create a `.env` file:**  
  In the project root directory, create a file named `.env` and add your Langflow API token:
  ```env
  API_TOKEN=your_langflow_api_token_here
  ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your default web browser.

## File Structure

```
AI Fact Checker/
├── app.py        # Streamlit app source code
├── .env         # Environment variabless
├── requirements.txt # Python dependencies
└── README.md      # Project documentation
```

## Code Overview

- **app.py:**
  - Sets up the Streamlit UI.
  - Handles user input and button events.
  - Sends POST requests to the Langflow API.
  - Displays the AI-generated fact-checking output.

## Customization

- **Langflow API:**  
  You can swap the API endpoint or update the authentication token in `app.py` as needed.
- **UI Enhancements:**  
  Modify the Streamlit components to add more features or improve the layout.

## License

This project is for educational and personal use. Please check the terms of use for Langflow and Streamlit for further details.

## Acknowledgements

- [Langflow](https://langflow.org/) for the AI backend.
- [Streamlit](https://streamlit.io/) for the rapid UI development.
