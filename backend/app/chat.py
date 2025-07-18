# chat.py

def basic_chat_response(message):
    message = message.lower().strip()
    if any(greet in message for greet in ["hello", "hi", "hey"]):
        return "Hey there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just code, but I’m running great 😄. How about you?"
    elif "your name" in message:
        return "I'm your friendly AI assistant."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day 🌟"
    else:
        return None  # Not a basic response, fallback to NLP
