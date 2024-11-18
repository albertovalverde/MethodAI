
![ThinkAi](image.jpeg)

# ThinkAI
An AI-powered application to assist in design thinking using the power of large language models.

## Introduction

`ThinkAi` is an interactive Streamlit application that guides users through the Design Thinking process. The app uses AI to generate insights, suggestions, and guidance based on user inputs across various stages of the design thinking methodology: Empathize, Define, Ideate, Prototype, and Test.

## Features

1. **Interactive Interface**: Offers a step-by-step walkthrough of the design thinking stages.
2. **Autofill for Demo**: Users can quickly start with a demo setup, where the necessary fields are autofilled.
3. **Feedback Response System**: Data Enrichment Set for Enhanced Design Thinking Evaluation.
4. **AI-powered Suggestions**: Based on user input, the application generates AI suggestions for each stage.
5. **Report Generation**: After obtaining results, users can generate a downloadable PDF report.
6. **Input Review**: Users can review their input at any point.
7. **Restart Capability**: The application can be restarted from any stage.
8. **AI Model Compatibility**: Compatible with various LLM models, Clarifai (GPT-4) and Groq [models](https://console.groq.com/docs/models)
## How to Use

1. **Autofill and Demo**: To quickly see the app in action, click "Autofill" to pre-populate the fields and then click "Generate Now" to get AI-powered insights.
2. **Manual Input**: Users can manually input answers to the presented questions, which will guide the AI's suggestions.
3. **Navigate Between Stages**: Once generated, the results for each design thinking stage can be viewed through tabs or by using the 'Next' button.
4. **Download Report**: Go to the "Download Report" tab to generate and download a comprehensive PDF report of your inputs and the AI's suggestions.
5. **Review Inputs**: Users can review their provided inputs in the "Your Input" tab.
6. **Restart**: If needed, users can restart the process by navigating to the "Restart" tab.

### To-Do:
1. **WORKING** Implement Real-Time Prototyping Module: Develop real-time prototyping functionality.
2. Set up **langchain_ollama** llama 3.2 locally.
3. Incorporate Live Prototype Viewer: Create a tool for users to interact with prototypes in real-time.
4. Explore Collaborative Prototyping: Investigate collaborative prototyping options for team projects.
5. Integrate Feedback Mechanism: Add a feedback system for instant input on prototypes during the design process.

### Does this align better with what you were looking for in the To-Do list structure? Let me know if you need any changes or further assistance!

## Dependencies

- streamlit
- extra_streamlit_components
- streamlit_option_menu
- fpdf
- weaviate
- langchain
- clarifai (openai GPT-4)
- langchain_groq [models](https://console.groq.com/docs/models)
- langchain_ollama (llama 3.2 locally)

## Setup

To get the app running locally:

1. Clone the repository.
2. Install the dependencies.
3. Run the app using Streamlit.

`streamlit run app.py`

## Integration with Visual Studio Code for Debugging
To debug the Streamlit app using Visual Studio Code with the provided configuration, follow these steps:
1. Ensure your `launch.json` contains the following configuration:
   
   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python:Streamlit",
               "type": "debugpy",
               "request": "launch",
               "module": "streamlit",
               "args": [
                   "run",
                   "app.py",
                   "${file}",
                   "--server.port",
                   "2000"
               ]
           }
       ]
   }
   ```

2. **Launch the Debugger**: Select the "Python:Streamlit" configuration in VS Code and press the play button to start debugging your Streamlit app with the specified arguments.


## Note

This app makes use of utility functions from various modules (e.g., `utils.pdf`, `utils.clarifai`, `utils.prompts`). Ensure these modules and their respective functions are available in your local setup.

## Feedback

For any feedback, issues, or feature requests, please open an issue in the repository.
