
![MethodAI](image.jpeg)

# MethodAI
A Cutting-Edge Solution Merging Methodologies with Artificial Intelligence for Rapid Prototyping and Efficient Product Development



## Introduction

`MethodAI` is an interactive Streamlit application that assists users in navigating the innovation process by seamlessly integrating various methodologies like Design Thinking and Lean Six Sigma. By capitalizing on artificial intelligence, the application enhances problem-solving efficiency while emphasizing user-centered principles, enabling rapid prototyping.

## Features

# MethodAI Features

# MethodAI Features

- **User-Centric Focus:** MethodAI prioritizes the user experience, ensuring personalized and efficient solutions.
- **Methodology Diversity:** Integrates methodologies like Design Thinking and Lean Six Sigma for a holistic problem-solving approach.
- **AI-Driven Insights:** Provides AI-generated suggestions and guidance based on user inputs across all stages of the innovation process.
- **Rapid Prototyping:** Swiftly generates prototypes aligning with rapid prototyping principles.
- **Data Enrichment:** Incorporates a feedback response system for enhanced evaluation of problem-solving methodologies.
- **Flexibility and Adaptability:** Allows users to explore diverse approaches in a flexible and adaptive manner.
- **Report Generation:** Facilitates the creation of downloadable PDF reports summarizing inputs and AI-derived suggestions.
- **AI Model Compatibility:** Compatible with multiple LLM models, Clarifai (GPT-4), and Groq [models](https://console.groq.com/docs/models)

## How to Use

1. **Autofill and Demo**: To quickly see the app in action, click "Autofill" to pre-populate the fields and then click "Generate Now" to get AI-powered insights.
2. **Manual Input**: Users can manually input answers to the presented questions, which will guide the AI's suggestions.
3. **Navigate Between Stages**: Once generated, the results for each design thinking stage can be viewed through tabs or by using the 'Next' button.
4. **Download Report**: Go to the "Download Report" tab to generate and download a comprehensive PDF report of your inputs and the AI's suggestions.
5. **Review Inputs**: Users can review their provided inputs in the "Your Input" tab.
6. **Restart**: If needed, users can restart the process by navigating to the "Restart" tab.

### To-Do List:
1. **WORKING** Implement Real-Time Prototyping Module: Develop real-time prototyping functionality.
2. **In Progress - Methodology Selection Enhancement**: Prepare for the integration of the methodology selection option, such as Design Thinking or Lean Six Sigma.
3. Set up **langchain_ollama** llama 3.2 locally.
4. Incorporate Live Prototype Viewer: Create a tool for users to interact with prototypes in real-time.
5. Explore Collaborative Prototyping: Investigate collaborative prototyping options for team projects.
6. Integrate Feedback Mechanism: Add a feedback system for instant input on prototypes during the design process.



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
