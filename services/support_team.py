from autogen_ext.models.openai import OpenAIChatCompletionClient

from config import OPENAI_API_KEY, MODEL_NAME

from agents.manager_agent import create_manager_agent
from agents.it_agent import create_it_agent
from agents.finance_agent import create_finance_agent
from agents.hr_agent import create_hr_agent
from agents.hospitality_agent import create_hospitality_agent
from agents.security_agent import create_security_agent


class CustomerSupportTeam:

    def __init__(self, model_client):

        self.model_client = model_client

        # Manager
        self.manager = create_manager_agent(
            self.model_client
        )

        # Department agents
        self.it_agent = create_it_agent(
            self.model_client
        )

        self.finance_agent = create_finance_agent(
            self.model_client
        )

        self.hr_agent = create_hr_agent(
            self.model_client
        )

        self.hospitality_agent = create_hospitality_agent(
            self.model_client
        )

        self.security_agent = create_security_agent(
            self.model_client
        )

    async def route_question(self, question):

        # ==================================================
        # STEP 1: MANAGER AGENT
        # ==================================================

        manager_result = await self.manager.run(
            task=question
        )

        routing = manager_result.messages[-1].content.strip()

        # Normalize the manager response
        routing = routing.upper().strip()

        print("\n====================================")
        print("USER QUESTION")
        print("====================================")
        print(question)

        print("\n====================================")
        print("RAW MANAGER RESPONSE")
        print("====================================")
        print(routing)

        # ==================================================
        # STEP 2: EXACT ROUTING
        # ==================================================

        if routing == "IT":

            department = "IT"
            selected_agent = self.it_agent

        elif routing == "FINANCE":

            department = "Finance"
            selected_agent = self.finance_agent

        elif routing == "HR":

            department = "HR"
            selected_agent = self.hr_agent

        elif routing == "HOSPITALITY":

            department = "Hospitality"
            selected_agent = self.hospitality_agent

        elif routing == "SECURITY":

            department = "Security"
            selected_agent = self.security_agent

        else:

            department = "Unknown"
            selected_agent = None

        # ==================================================
        # DEBUG
        # ==================================================

        print("\n====================================")
        print("SELECTED DEPARTMENT")
        print("====================================")
        print(department)

        # ==================================================
        # UNKNOWN DEPARTMENT
        # ==================================================

        if selected_agent is None:

            return {
                "department": "Unknown",
                "answer": (
                    "I could not determine the appropriate "
                    "department for your question. "
                    "Please provide a little more information."
                )
            }

        # ==================================================
        # STEP 3: DEPARTMENT AGENT
        # ==================================================

        department_result = await selected_agent.run(
            task=question
        )

        answer = department_result.messages[-1].content

        # ==================================================
        # DEBUG
        # ==================================================

        print("\n====================================")
        print("AGENT RESPONSE")
        print("====================================")
        print(answer)

        return {
            "department": department,
            "answer": answer
        }


async def process_customer_question(question):

    """
    Creates the AutoGen model client and team inside
    one async lifecycle.

    This avoids reusing an async client after the
    Streamlit event loop has been closed.
    """

    model_client = OpenAIChatCompletionClient(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY
    )

    try:

        team = CustomerSupportTeam(
            model_client
        )

        result = await team.route_question(
            question
        )

        return result

    finally:

        # Important:
        # Always close the AutoGen model client
        await model_client.close()