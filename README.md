

![MethodAI](image.jpeg)

# MethodAI
A Cutting-Edge Solution Merging Methodologies with Artificial Intelligence for Rapid Prototyping and Efficient Product Development


## Introduction


`MethodAI` is an interactive Streamlit application that aids users in navigating the innovation process by seamlessly integrating various methodologies like **Design Thinking** and **Lean Six Sigma**. Leveraging artificial intelligence, the application enhances problem-solving efficiency while emphasizing user-centered principles, enabling rapid prototyping.


## Why?
Highlighting the lack of user-centered methodologies and the absence of prototypes before final production, ensures product viability by involving the user from the outset and allowing for testing before the definitive implementation.

## For what?
The application aims to optimize innovation by facilitating the generation of disruptive ideas, their validation with real users, and reducing the time invested in unsuccessful projects.

## How?
Through the combination of successful methodologies such as Design Thinking and Lean Six Sigma, augmented by artificial intelligence, development is streamlined for rapid prototyping and iterative testing before the final implementation, significantly enhancing the effectiveness of the product creation process.

## How much?
The assessment of resources and costs for implementing these enhancements will depend on the project's scope regarding development and the quality of prototype generation, as well as the cost associated with using the paid LLM. A detailed analysis is recommended for an accurate estimate.


## Features

- **User-Centric Focus:** MethodAI prioritizes the user experience, ensuring personalized and efficient solutions.
- **Methodology Diversity:** Incorporates methodologies like Design Thinking and Lean Six Sigma for an enhanced problem-solving strategy.
- **AI-Driven Insights:** Provides AI-generated suggestions and guidance based on user inputs across all stages of the innovation process.
- **Rapid Prototyping:** Swiftly generates prototypes aligning with rapid prototyping principles.
- **Data Enrichment:** Incorporates a feedback response system for enhanced evaluation of problem-solving methodologies.
- **Flexibility and Adaptability:** Allows users to explore diverse approaches in a flexible and adaptive manner.
- **Report Generation:** Facilitates the creation of downloadable PDF reports summarizing inputs and AI-derived suggestions.
- **AI Model Compatibility:** Compatible with multiple LLM models, Clarifai (GPT-4), and Groq [models](https://console.groq.com/docs/models)

## How to Use

- **Autofill and Demo:** Quickly explore the app by clicking "Autofill" to pre-fill fields and then "Generate Now" for AI-powered insights.
- **Manual Input:** Users can input answers manually for tailored AI recommendations.
- **Navigate Between Stages:** Move between stages of different methodologies effortlessly, not limited to just Design Thinking, to enhance results.
- **Rapid Prototyping:** Allows for the generation of disruptive ideas and testing their application with real users.
- **Download Report:** Access the "Download Report" tab to retrieve a detailed PDF report encompassing inputs and AI suggestions.
- **Review Inputs:** Evaluate your inputs within the "Your Input" section.
- **Restart:** Restart the process if needed by navigating to the "Restart" tab.

### To-Do List:
1. **WORKING** Implement Real-Time Prototyping Module: Develop real-time prototyping functionality.
2. **In Progress - Methodology Selection Enhancement**: Prepare for the integration of the methodology selection option, such as Design Thinking or Lean Six Sigma.
3. Set up **langchain_ollama** llama 3.2 locally.
4. Incorporate Live Prototype Viewer: Create a tool for users to interact with prototypes in real-time.
5. Explore Collaborative Prototyping: Investigate collaborative prototyping options for team projects.
6. Integrate Feedback Mechanism: Add a feedback system for instant input on prototypes during the design process.

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