# SecuraBot - AI Assistant for Web Security Testing

**Version:** 1.0.0
**Author:** [Your Name/Team Name Here]
**Project Date:** October 2025

## 1. Project Vision

SecuraBot is a specialized, reliable, and efficient AI-powered chatbot designed to assist cybersecurity professionals and developers. It provides immediate, accurate information and guidance on web application vulnerabilities, focusing on SQL Injection and API endpoint testing.

This tool aims to:
- **Centralize Knowledge:** Act as a single source of truth for common vulnerabilities, testing payloads, and mitigation techniques.
- **Accelerate Learning:** Help new team members quickly get up to speed on complex security topics.
- **Boost Efficiency:** Serve as a quick-reference "expert-in-a-box" for seasoned professionals, reducing time spent searching for specific commands or concepts.

## 2. Architecture and Technology

SecuraBot is built on a modern, robust, and secure architecture that prioritizes factual accuracy over uncontrolled creativity.

### Core Architecture: Retrieval-Augmented Generation (RAG)

We made a deliberate design choice to create a **closed-world, expert-driven system.** The chatbot's intelligence is derived from a two-step process:

1.  **Retrieval:** When a user asks a question, the system first retrieves the most relevant articles and data from a curated, local **Knowledge Base** (`knowledge_base.txt`). This knowledge base contains hundreds of vetted Q&As on expert-level security topics.
2.  **Generation:** The retrieved information is then passed to a powerful Large Language Model (Google's Gemini Pro) along with a strict set of instructions. The model's task is to synthesize the provided facts into a coherent, human-readable answer.

This RAG approach guarantees that every answer is grounded in our pre-approved data, mitigating the risks of factual inaccuracy and AI "hallucination," which is paramount for a security-critical tool.

### Technology Stack

-   **AI Backend:** Python 3.11
-   **Web Framework / API:** Flask
-   **AI Model:** Google Gemini Pro (`models/gemini-pro-latest`) via the `google-generativeai` library.
-   **UI Frontend:** Self-contained HTML, CSS, and vanilla JavaScript.
-   **Environment:** Packaged using PyInstaller for cross-platform compatibility.

## 3. How to Run the Application

Follow these steps to get your own instance of SecuraBot running in minutes.

### Step 1: Get Your Free Google AI API Key

For security and to avoid shared costs, SecuraBot requires you to use your own free API key from Google.

1.  Navigate to **[Google AI Studio](https://aistudio.google.com/)**.
2.  Sign in with your Google account.
3.  In the top left menu, click **"Get API key"** and then **"Create API key in new project"**.
4.  A new key will be generated. **Copy this key immediately** and store it securely.

### Step 2: Configure the Application

1.  In the same folder as `chatbot.exe`, create a new text file.
2.  Rename this file to exactly **`.env`** (the name starts with a period).
3.  Open the `.env` file with a text editor and add your API key in the following format:
    ```
    GEMINI_API_KEY="AIzaSy...your...key...here..."
    ```
4.  Save and close the file.

### Step 3: Launch SecuraBot

1.  Double-click on **`chatbot.exe`**. A black terminal window will appear. This is the backend server. **Leave this window running in the background.**
2.  Double-click on **`index.html`**. This will open the SecuraBot user interface in your default web browser.

That's it! You can now interact with the assistant using the floating button in the corner. When you are finished, simply close the black terminal window to shut down the server.

## 4. Key Features

-   **Expert Knowledge Base:** Contains over 200 expert-vetted questions and answers on SQLi, API Security, XSS, XXE, CSRF, and more.
-   **OWASP Top 10 Integration:** Provides detailed explanations of the OWASP Top 10 for both 2021 and 2017, including key differences.
-   **Practical Payload Library:** Offers a comprehensive list of over 50 ready-to-use payloads for various testing scenarios.
-   **Authoritative Citing:** Includes links to official OWASP Cheat Sheets and PortSwigger's Web Security Academy for further reading.
-   **Interactive UI:** Features a modern, user-friendly interface with prompt starters to guide the user.
-   **Secure by Design:** Built with a secure architecture that prevents common web vulnerabilities like XSS in the UI and is designed to provide only safe, vetted information.
-   **Private and Stateless:** No conversation data is ever stored on your computer or linked to your Google account. Every session is completely private.

## 5. Future Roadmap

While SecuraBot 1.0 is a complete and powerful tool, future development could explore the following enhancements:
-   **Conversation Memory:** Implement a short-term memory to allow the chatbot to understand the context of follow-up questions more deeply.
-   **Knowledge Base Expansion:** Regularly update the `knowledge_base.txt` file with information on new vulnerabilities and testing techniques.
-   **Optional Internet Connectivity:** For advanced users, explore a feature to allow the chatbot to optionally query the Google Search API for information on zero-day threats, with strong warnings about the potential for unverified information.