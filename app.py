import google.generativeai as genai
import gradio as gr

GOOGLE_API_KEY = 'AIzaSyD5AVztAAquov4LbC-RzH2PEhf23FD4xqM'
# Configure api_key
genai.configure(api_key=GOOGLE_API_KEY)

# Define Model Instance# Define function, which helps to execute any prompt
def get_llm_response(message):
    response = chat.send_message(message)
    print(response)
    return response.text
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Define Basic information for prompt
base_info = """
You are OrderBot, an automated service to collect orders for a Burger Singh Restaurant.
You first greet the customer, then collects the order,
and then asks if its a pickup or delivery.
Please do not use your own knowladge, stick within the given context only.
You wait to collect the entire order, then summarize it and check for a final
time if the customer wants to add anything else.
"""

# Define delivery related instruction
delivery_info = """If its a delivery, you ask for an address. \
Finally you collect the payment. \
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu. \
You respond in a short, very conversational friendly style. \
The menu includes"""

# Define available burger types
burger_type = """
classic cheeseburger for 149 Rs \
bacon cheeseburger for 139 Rs \
mushroom Swiss burger for 145 Rs
"""

# Define available fries
fries = "60 Rs 45 Rs"

# Define available toppings
toppings = """
greek salad 30 Rs \
lettuce 15 Rs  \
tomato 15 Rs  \
onion 15 Rs  \
pickles 15 Rs  \
mushrooms 15 Rs  \
extra cheese 20 Rs  \
sausage 30 Rs  \
canadian bacon 35 Rs  \
AI sauce 15 Rs  \
peppers 10 Rs
"""

# define drinks
drinks = """
coke 60 Rs, 45 Rs, 30 Rs \
sprite 60 Rs, 45 Rs, 30 Rs \
bottled water 50 Rs
"""

# create prompt
context = [f"""
{base_info} \
{delivery_info} \
{burger_type} \
fries: {fries} \
Toppings: {toppings} \
Drinks: {drinks} \
"""]  # accumulate messages

# create welcome message
context.append("")
response = get_llm_response(context)

# define communication function
def bot(message, history):
  prompt = message
  context.append(prompt)
  response = get_llm_response(context)
  context.append(response)
  return response

# create gradio instance
demo = gr.ChatInterface(fn=bot, examples=["🍔🍟🥤", "classic cheeseburger", "fries", "Toppings: extra cheese/ AI sauce", "Drinks: coke/sprite/bottled water"], title=response)
# launch gradio chatbot
demo.launch(debug=True, share=True)
