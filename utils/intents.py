def detect_intent(text):

    text = text.lower()

    greetings = [
        "hello",
        "hi",
        "hey"
    ]

    goodbye = [
        "bye",
        "goodbye"
    ]

    if any(word in text for word in greetings):
        return "greeting"

    if any(word in text for word in goodbye):
        return "goodbye"

    return "general"