

def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "timing" in user_input or "hours" in user_input:
        return "We are open from 9 AM to 9 PM."
    elif "menu" in user_input or "serve" in user_input or "coffee" in user_input or "food" in user_input or "drinks" in user_input:
        return """
We have a wide range of delicious items!
- Coffees: Espresso, Latte, Cappuccino, Americano, Mocha
- Teas: Green Tea, Black Tea, Herbal Infusions
- Food: Fresh Croissants, Sandwiches, Muffins, and Cake of the Day.
What are you in the mood for?
"""
    elif "price" in user_input or "cost" in user_input:
        return "Our pricing starts from $10."
    
    elif "bye" in user_input:
        return "Goodbye! Have a great day 😊"
    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"


print("Chatbot: Hi! I'm your assistant. Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Chatbot:", response)
    if "bye" in user.lower():
        break


