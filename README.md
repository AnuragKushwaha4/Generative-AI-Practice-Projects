This repository contains my practice projects and experiments with Generative AI using LangChain.
It includes different implementations like:

🔍 RAG (Retrieval Augmented Generation)

💬 Chatbots with message history

🧩 Prompt engineering experiments

1st. Implemented RAG(Retrieval Argumented Generation) : RAG is AI Framework used to provide external context to model and give response over that context. RAG is implemented in 6 stages: 1. Ingestion 2. Splitting 3. Embeddings 4. storing 5. retriving 6. generation

2nd. Implemented LCEL(Langchain expression Language) : it help to create chain from a langchain feacture or components. Understand Runnables. It is something that can be chained means every components in langchain are not supports chaining so Runnable make them to support chain and make model more convinient.

3rd Implemented Chatbot with message history actually via creating session for a single chat.

4th Earlier i was Implemented a chatbot with message history now i implemented i miniproject deployed via streamlit to handling dynamic session management and handling message history.

5th Tools and Agents :These are the important part of Generative AI field:
Before Introducing about my project let me explain what actually is Tools and Agents:

Tools: Tools are basically a function or External function that can capable to perform a specific task very efficiently and you all know AI is train over user data or Large data set then i preety obvious that AI can not be truly efficient in performing all these tasks so tools are used to provide functionality to AI model for performing specific task.

Agents:Agents are like smart decision makers that knows how to use tools and where to use which tool.

Now in my project i created a AI agent that can search for user Query for over different Platform like some information it will collect from Wikipedia some from Arxiv if user want something from specific info from any website i created a tool for it also user can ask their query after sharing website link.

Mean my Agent helps user in finding info from wiki , arxivs , and From specific websites also.