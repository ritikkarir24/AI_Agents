from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

#this function expects a .env file
load_dotenv()


agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile")
)

#test your connections
#agent.print_response("Write a pickup line for the next girl i meet")

