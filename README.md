# Image
![ThinkAi](image.jpeg)

# ThinkAI
An AI-powered application to assist in design thinking leveraging the capabilities of large language models.

## Introduction
ThinkAI is an interactive Streamlit application that guides users through the design thinking process. The app harnesses AI to generate insights, suggestions, and guidance based on user inputs across various stages of the design thinking methodology: Empathize, Define, Ideate, Prototype, and Test.

## Features
- **Interactive Interface**: Offers a step-by-step walkthrough of the design thinking stages.
- **Autofill for Demo**: Users can quickly start with a demo setup where essential fields are autofilled.
- **AI-powered Suggestions**: Generates AI suggestions for each stage based on user input.
- **Report Generation**: Users can produce a downloadable PDF report upon obtaining results.
- **Input Review**: Users have the ability to review their input at any point.
- **Restart Capability**: The application can be restarted from any stage.

## To-Do Ideas for Real-Time Prototyping
- **Real-Time Prototyping Module**: Implement a feature for real-time prototyping functionality.
- **Live Prototype Viewer**: Incorporate a tool that allows users to view and interact with prototypes in real-time.
- **Collaborative Prototyping**: Explore possibilities for collaborative prototyping functionalities for team projects.
- **Feedback Integration**: Integrate a feedback mechanism for instant input on prototypes during the design process.

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

## Dependencies
- streamlit
- extra_streamlit_components
- streamlit_option_menu
- fpdf
- langchain
- weaviate
- clarifai

## Setup
To run the app locally:
1. Clone the repository.
2. Install the necessary dependencies.
3. Launch the app using Streamlit.

```bash
streamlit run app.py
```

## Note
This application utilizes utility functions from various modules (e.g., `utils.pdf`, `utils.clarifai`, `utils.prompts`). Ensure these modules and their respective functions are accessible in your local setup.

## Feedback
For any feedback, issues, or feature requests, please open an issue in the repository.
