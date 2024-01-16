GPT Text Detection Web Application
This is a proof of concept (POC) site that can identify whether a given text was generated by a GPT model. The application is currently hosted at detectgptforme.com.

Requisites
The application is built with Flask. It is suitable for local or internal use but is not recommended for internet-facing production environments in its current state.
An OpenAI API key is required. You can obtain a key for free from openai.com.
Setting Up
OpenAI API Key: To import your OpenAI API key, run the following command in your console, replacing GET YOUR OWN KEY AND PASTE IT HERE with your actual key:
export OPENAI_API_KEY=GET YOUR OWN KEY FROM OPENAI AND PASTE IT HERE
Application Functionality: The applet allows users to paste text into an input field. It then uses the gpt-3.5-turbo-instruct model from OpenAI's GPT-3.5 series to analyze the text and determine if it was syntactically generated by a GPT model.

The text should be limited to a few paragraphs for optimal results.
The output is straightforward: 'Yes' if the text is identified as being generated by ChatGPT, and 'No' if it is not, or if it has been reworded in a way that the analysis cannot confidently identify it as GPT-generated.
Modules Required
Python 3 or greater must be installed.
Python packages:
openai (install via pip)
flask (install via pip)
Usage
To run the application locally:

Clone the repository or download the source code.
Install the required Python modules.
Set up your OpenAI API key as described above.
Run the Flask application by executing the main Python script.
Feel free to modify or add any additional information that might be relevant to your users or the specificities of your application.

There is a POC availible at https://detectgptforme.com

![Chat GPT Output](https://github.com/chrisjchandler/gptdetectionserver/blob/main/gptout.jpg "ChatGPT output inquiring about Abe Lincoln")

![Open AI detection positive](https://github.com/chrisjchandler/gptdetectionserver/blob/main/GPTyes.jpg "OpenAI detection indicating that the content came from ChatGPT")

![Open AI detection negative](https://github.com/chrisjchandler/gptdetectionserver/blob/main/gptno.jpg "Open AI detection of summary text about Abe not generated by CHAT GPT")
