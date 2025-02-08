from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools #tool that is being used

#this function expects a .env file
load_dotenv()


agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"), #this model has static information, but inorder for this model to generate answers on latest information, they need some tools and now we will be providing those
    #below are the parameters , you can find these from YFinance documentation
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True, #all the information is being gathered through the above internal call and with this I can also see these calls
    markdown=True, #if my generated response has some comparisons , I dont want to see those symbols to make the border so that's why we are implementing markdown plus providing a below instruction that provide data in form of tables
    instructions=["Use tables to display data."],
    debug_mode=True

)

#test your connections
#agent.print_response("Write a pickup line for the next girl i meet")

agent.print_response("Summarize and compare analysis funadamentals and recommendations of stocks of Tesla adn spaceX")