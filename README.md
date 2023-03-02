# Creating custom Chatbot with ChatGPT API

## Motivation

The launch of ChatGPT had a profound impact on the world, as it enabled countless individuals to benefit from its ability - to simplify complex concepts and solve sophisticated problems, ranging from assisting students to improving the operations of large businesses. Now, OpenAI has introduced the ChatGPT API, which allows organizations to seamlessly integrate this technology into their products, that will allow to unlock exponential improvements in functionality and performance of these products.

## Task

In this project, we will use ChatGPT API and Gradio to provide Chatbot User Interface. Gradio is library that allows easy-to-use quick demo for using Machine Learning models.  

## Running API on Docker Container

- Sign up in OpenAI website and get your API key.
- `.env` must contain the OPENAPI KEY and paths. Sample included. For production purpose, .env file should be included in .gitignore file.
- Run the docker container:

```bash
docker compose up
```

- If any changes made to the code, then run following command for the code changes to be reflected in the docker container.Then, we can run the above command.

```bash
docker compose build
```

- On your web browser, go to `http://localhost:9001` and the Chatbot Gradio Interface will appear.

- Sample as follows.

![alt text](https://github.com/di37/chatbot-chatgpt-api/blob/main/screenshots/sample.png?raw=true)

## Resources

- ChatGPT API Documentation: https://platform.openai.com/docs/guides/chat
- Gradio Chatbot Documentation: https://gradio.app/creating-a-chatbot/ 
- ChatGPT Clone Tutorial: https://www.youtube.com/watch?v=n5nn3mQxrE8&ab_channel=1littlecoder

## Important Note

This project is created exclusively for educational purpose. Not to be used for commercial purposes.
