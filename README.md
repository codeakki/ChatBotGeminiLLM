# CHATBOT-GEMINI-LLM

CHATBOT-GEMINI-LLM is a conversational AI model designed to engage in natural language dialogues with users. The model has the capability to remember past interactions, allowing it to provide contextually relevant responses based on the user's history. This feature enhances the continuity and coherence of conversations, making the user experience more personalized and effective.

# How to run?

### STEPS:

Clone the repository

```bash
Project repo https://github.com/codeakki/ChatBotGeminiLLM.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.9 -y
```

```bash
conda activate venv
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
streamlit run app.py
```

Now,

```bash
open up localhost:

```

## Sample

![OpenAI Logo](https://github.com/codeakki/ChatBotGeminiLLM/blob/master/image.png)

### Techstack Used:

- Python
- Streamlit
- google-generativeai
