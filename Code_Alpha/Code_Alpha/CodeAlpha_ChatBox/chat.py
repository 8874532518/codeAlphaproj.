def venom(message):
    message = message.lower().strip()

    # Greeting
    if "hello" in message or "hi" in message or "hey" in message:
        return "Hello! Welcome to the chatbot."

    # How are you
    elif "how are you" in message:
        return "I am fine. Thank you for asking!"

    # Name
    elif "your name" in message or "who are you" in message:
        return "My name is Venom. I am a basic Python chatbot."

    elif "who made you" in message or "who created you" in message or "who built you" in message:
        return "I was created by Alok Kumar sir."

    # Help
    elif "help" in message:
        return "I can answer questions about Python, study, college and some general topics."

    # Python
    elif "python" in message:
        return "Python is a popular programming language used for many types of applications."

    # Programming
    elif "programming" in message:
        return "Programming means writing instructions for a computer to perform a task."

    # Study
    elif "study" in message or "studying" in message:
        return "Regular practice and revision can make studying easier."

    # Exam
    elif "exam" in message:
        return "Prepare a simple study plan and revise important topics before the exam."

    # College
    elif "college" in message:
        return "College is a good place to learn new skills and gain practical experience."

    # BCA
    elif "bca" in message:
        return "BCA is a computer applications course that covers programming and computer-related subjects."

    # Cyber Security
    elif "cyber security" in message or "cybersecurity" in message:
        return "Cyber Security is the practice of protecting computers, networks and data."

    # Networking
    elif "networking" in message or "network" in message:
        return "Computer networking allows computers and devices to communicate with each other."

    # Good Morning
    elif "good morning" in message:
        return "Good morning! Have a great day."

    # Good Afternoon
    elif "good afternoon" in message:
        return "Good afternoon! Hope you are having a good day."

    # Good Evening
    elif "good evening" in message:
        return "Good evening! How can I help you?"

    # Good Night
    elif "good night" in message:
        return "Good night! Take care and sleep well."

    # Thanks
    elif "thank" in message or "thanks" in message or "thank_you" in message:
        return "You're welcome! I am happy to help."

    # Happy
    elif "happy" in message:
        return "That's great! Keep smiling."

    # Sad
    elif "sad" in message:
        return "I hope things get better. Take a little break and stay positive."

    # Weather
    elif "weather" in message:
        return "I cannot check live weather, but you can use a weather application."

    # Food
    elif "food" in message:
        return "Food gives us energy. Don't forget to eat properly!"

    # Joke
    elif "joke" in message:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # Project
    elif "project" in message:
        return "Projects are a good way to improve programming and practical skills."

    # Internship
    elif "internship" in message:
        return "An internship helps students gain practical experience and learn workplace skills."

    # Future
    elif "future" in message:
        return "Keep learning new skills and practice regularly for a better future."

    # Bye
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day. See you again!"

    # Unknown question
    else:
        return "Sorry, I don't understand your question."

print("------------------------------------------")
print("             BASIC CHATBOT")
print("------------------------------------------")
print("Hello! I am Venom (Chatbot).")
print("I can answer some basic questions.")
print("Type 'help' to know what I can do.")
print("Type 'bye' to exit the chatbot.")
print("------------------------------------------")

while True:

    message = input("\nYou: ")

    # Check for empty input
    if message.strip() == "":
        print("Bot: Please type something.")
        continue

    # Get chatbot response
    answer = venom(message)

    print("Bot:", answer)

    # Exit chatbot
    if "bye" in message.lower() or "goodbye" in message.lower():
        break

print("\n------------------------------------------")
print("       Chatbot session ended.")
print("       Thank you for using SimpleBot!")
print("        Have a nice day           ")
print("        Radhey Radhey              ")
print("------------------------------------------")