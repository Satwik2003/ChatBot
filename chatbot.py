from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
completion = openai.Completion



start_sequence = "\nSteve: "
restart_sequence = "\n\nHuman: "
session_prompt = "The following is a conversation with an Steve. The Steve is helpful, creative, clever, and very friendly chatbot built by Mojang. Steve lives alone in self-built wood mansion on a secluded mountain. He likes to build stuff on his own. Currently, he is working on a map art."

def ask(question, chatlog=None):
    prompt_text= f'{chatlog}{restart_sequence}: {question}{start_sequence}'
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt_text,
    temperature=0.04,
    max_tokens=190,
    top_p=0.42,
    best_of=6,
    frequency_penalty=0.42,
    presence_penalty=0.02,
    stop=[" Human:", "Steve:"]
    )
    story = response['choices'][0]['text']
    return str(story)

def appendChat(question, answer, chatlog=None):
    if chatlog is None:
        chatlog = session_prompt
    return f'{chatlog}{restart_sequence} {question}{start_sequence}{answer}'

if __name__ == '__main__':
    print(session_prompt) 

    chatlog = None

    while (True):

        question = input(f'{restart_sequence}')

        if question.lower() == "exit":
            print("Successfully Exited")
            break

        answer = ask(question, chatlog)

        print(f'\nSteve: {answer}')
    