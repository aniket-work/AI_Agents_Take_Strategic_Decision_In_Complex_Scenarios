import streamlit as st
import asyncio
from main import run_ai_agent
from constants import LOG_FILE

# Define the business deal scenario
business_deal_scenario = "Merger between two leading tech companies facing antitrust concerns"

# Title in the sidebar
st.sidebar.title("Business Deal Scenario")
st.sidebar.write(business_deal_scenario)

st.title("Reflection AI Agent for Strategic Business Decision Analysis")

st.write(
    "This application analyzes complex business scenarios using AI agents that generate and reflect upon analyses iteratively.")

# Show the business deal scenario in the main content area as well
st.subheader("Scenario:")
st.write(business_deal_scenario)


# Use HTML for bold and larger text
st.markdown(
    "<h4><b>Enter another business scenario :</b></h4>",
    unsafe_allow_html=True
)

# Text input field
scenario_input = st.text_input("", value=business_deal_scenario)


# Use HTML for bold and larger text
st.markdown(
    "<h5><b>No. Of Reflection rotations:</b></h5>",
    unsafe_allow_html=True
)

# Number input field
iterations_input = st.number_input("", min_value=1, max_value=10, value=5)


def update_ui():
    log_placeholder = st.empty()

    # Start the AI agent task asynchronously
    task = asyncio.run(run_ai_agent())

    # Update logs every 2 seconds
    while not task.done():
        # Wait for 2 seconds
        st.time.sleep(2)

        # Read the logs and update the UI
        with open(LOG_FILE, 'r') as file:
            logs = file.read()
        log_placeholder.text_area("Logs", logs, height=300)

    # Get the final output and display it
    final_output = task.result()
    st.success("AI Agent Execution Completed.")
    st.subheader("Final Output:")
    st.write(final_output)

if st.button("Show Log"):
    with open(LOG_FILE, 'r') as file:
        log = file.read()
    st.text_area("Log Output", log, height=400)


if st.button("Run AI Agent"):
    st.write("Running AI Agent...")
    asyncio.run(run_ai_agent())
    st.write("AI Agent Finished.")

