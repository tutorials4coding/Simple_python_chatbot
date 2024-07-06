# Chatbot and human interection
import time
print("Hi, i'm a chatbot. What's your name?")
name = input()
print("Nice to meet you," + name + "!")
time.sleep(1)
print("How's your day going?")
response = input()

if "good" in response.lower():
    print("Glad to hear that!")
elif "bad" in response.lower():
    print("i'm soory to hear that.")
else:
    print("Interesting!")

print("It was nice chatting with you. Goodbye," + name + "!")
