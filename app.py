import asyncio
import streamlit as st

from services.support_team import process_customer_question


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Company AI Customer Support",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666;
        margin-bottom: 25px;
    }

    .department-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f7f7f7;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">🤖 Company AI Customer Support</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Ask your question and our AI Manager Agent will route
    it to the appropriate department specialist.
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("🏢 Departments")

    st.markdown(
        """
        ### 💻 IT
        Laptop, VPN, software, network and applications.

        ### 💰 Finance
        Payroll, expenses, invoices and payments.

        ### 👥 HR
        Leave, benefits, onboarding and HR policies.

        ### 🏨 Hospitality
        Cafeteria, facilities, meeting rooms and events.

        ### 🔐 Security
        Access badges, visitors and security incidents.
        """
    )

    st.divider()

    st.caption(
        "Powered by AutoGen Agent Teams + OpenAI"
    )


# ==================================================
# CHAT HISTORY
# ==================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==================================================
# DISPLAY PREVIOUS MESSAGES
# ==================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if message.get("department"):

            st.caption(
                f"🏢 Department: {message['department']}"
            )


# ==================================================
# CHAT INPUT
# ==================================================

user_question = st.chat_input(
    "Ask your company support question..."
)


# ==================================================
# PROCESS USER QUESTION
# ==================================================

if user_question:

    # ----------------------------------------------
    # Display user message
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.markdown(
            user_question
        )


    # ----------------------------------------------
    # Assistant response
    # ----------------------------------------------

    with st.chat_message("assistant"):

        try:

            with st.spinner(
                "🤖 Manager Agent is routing your question..."
            ):

                result = asyncio.run(
                    process_customer_question(
                        user_question
                    )
                )


            department = result["department"]
            answer = result["answer"]


            # --------------------------------------
            # Show routing information
            # --------------------------------------

            st.success(
                f"🏢 Routed to **{department} Department**"
            )


            # --------------------------------------
            # Show answer
            # --------------------------------------

            st.markdown(
                answer
            )


            # --------------------------------------
            # Save conversation
            # --------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "department": department
                }
            )


        except Exception as e:

            st.error(
                "Sorry, I encountered an error "
                "while processing your request."
            )

            st.exception(e)