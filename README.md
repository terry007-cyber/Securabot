 # SecuraBot - AI Security Assistant

    SecuraBot is a specialized AI-powered chatbot designed to assist cybersecurity professionals and students. It provides expert-level answers on topics like SQL injection, API security, the OWASP Top 10, and common testing payloads, all within a safe, controlled environment.

    This project uses a Retrieval-Augmented Generation (RAG) architecture, ensuring that all answers are based on a curated, expert-vetted knowledge base.

    ---

    ## Setup and Installation

    Follow these steps to run the project locally.

    ### 1. Clone the Repository
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

    ### 2. Create and Activate a Virtual Environment
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on Mac/Linux
    # source venv/bin/activate
    ```

    ### 3. Install Dependencies
    Install all the required Python libraries with one command:
    ```bash
    pip install -r requirements.txt
    ```

    ### 4. Create Your API Key File
    This project requires a free Google AI API key.

    *   Get your key from [Google AI Studio](https://aistudio.google.com/).
    *   In the project's root directory, create a new file named `.env`.
    *   Add your API key to the file in the following format:
        ```
        GEMINI_API_KEY="AIzaSy...your...key...here..."
        ```
    This file is listed in `.gitignore` and will not be uploaded to GitHub.

    ---

    ## Usage

    1.  **Start the Backend Server:**
        Run the following command in your terminal:
        ```bash
        python chatbot.py
        ```
        The server will start on `http://127.0.0.1:8888`.

    2.  **Open the User Interface:**
        In your file explorer, find and open the `index.html` file in your web browser.

    You can now interact with the SecuraBot assistant!