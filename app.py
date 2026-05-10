from logging_config import logger 
from chat_request import chatRequest 
from config import MODEL_NAME, URL
def _finishProcess():
   print("Chat console exited. Thanks & bye")
def _get_response(messages):
    response = chatRequest(MODEL_NAME, URL, messages)
    return response
def main():
    print(f"{MODEL_NAME} chat console started. Type 'exit' to quit.")
    messages = [
        {"role": "system", 
         "content": "You are a helpful assistant. Answer briefly and concisely."
         }
    ]
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                _finishProcess()
                break
            messages.append({"role": "user", "content": user_input})
            response = _get_response(messages)
            print(f"Assistant: {response}")
            messages.append({"role": "assistant", "content": response})
        except KeyboardInterrupt:
            _finishProcess()
            break   
if __name__ == "__main__":
    main()