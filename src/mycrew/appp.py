# from langchain_huggingface import HuggingFaceEndpoint
# from datetime import datetime
# from agents import Destination_Researcher,Travel_planner,Budget_Analyst,Local_Expert
# from tasks import Research_Destination,Weather_Forecasting,Cost_Estimation,Convert_Budget,Generate_Itinerary,Adding_Local_Tips,Plan_Finalization_Saving
# from crewai import Crew,Process
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# import os
# load_dotenv()

# def main():

#     #HF_APIKEY = os.getenv("HF_TOKEN")
#     TAVILY_APIKEY = os.getenv("TAVILY_API")
#     SERPER_APIKEY = os.getenv("SERPER_API_KEY")
#     #model = os.getenv("MODEL")

#     # llm = HuggingFaceEndpoint(
#     #     repo_id=os.getenv("MODEL").replace("huggingface/", ""),
#     #     token=os.getenv("HF_TOKEN"),
#     #     task="text-generation",
#     #     temperature=0.7,
#     #     max_new_tokens=1024,
#     #     top_k=50,
#     #     top_p=0.95,
#     #     do_sample=True
#     # )

#     apikey = os.getenv("OPENAI_API_KEY")


#     llm = ChatOpenAI(
#         model="gpt-3.5-turbo",
#         temperature=0.7,
#         api_key=apikey
#     )

#     st.set_page_config(page_title="AI-Powered-Trip_planner", page_icon="✨")
#     st.title("AI-Powered-Trip-Planner")
#     st.markdown("""
#           ****Plan your next trip with AI****
#                 Enter your travel details below, and our AI-Powered travel assistant will create a personalized travel plan 
#                 Best places to visit  Accomodation & budget plannning
#                 local food recommendations Transportation & visa details
#     """)

#     # User Inputs
#     travel_from = st.text_input("Origin","India")
#     travel_to = st.text_input("Destination","Kisumu")
#     date_from = st.date_input("Departure Date")
#     date_to = st.date_input("Return Date")
#     budget = st.number_input("$")
#     group_size =  st.selectbox(
#         label="What is your travel group type?",
#         options=["solo", "couple", "family"]
# )
#     pace = st.selectbox(
#         label="What is your desired pace?",
#         options=["moderate", "relaxed"]
#     )
#     # mode_of_transport = st.selectbox(
#     #     label="What is your desired mode of transport?",
#     #     options=["uber", "train"]
#     # )
#     interests = st.text_area("Your Interests (eg., go-karting)")

#     if st.button("Generate Plan"):
#         if not travel_from or not travel_to or not date_from or not date_to or not interests or not budget or not group_size or not pace:
#             st.error("Please fill in all required fields before generating your travel plan")
#         else:
#             with st.spinner("Generating plan..."):
            
#                 crew = Crew(
#                     tasks=[Research_Destination,Weather_Forecasting,Cost_Estimation,Convert_Budget,Generate_Itinerary,Adding_Local_Tips,Plan_Finalization_Saving],
#                     agents=[Destination_Researcher,Travel_planner,Budget_Analyst,Local_Expert],
#                     memory=True,
#                     cache=True,
#                     process=Process.sequential,
#                     verbose=True,
#                     max_rpm=150,
#                     chat_llm=llm,
#                     share_crew=False,

#                 )
#                 result = crew.kickoff(inputs={ })

#                 st.subheader("Your AI Powered Travel Plan")
#                 st.markdown(result)

#                 travel_plan_text = str(result) # converts CrewOutput to string

#                 st.download_button(
#                      label="Download CSV",
#                      data=travel_plan_text,
#                      file_name="data.csv",
#                      mime="text/plain",
#                      icon=":material/download:",
#                 )
#     #print(result)
# if __name__ == "__main__":
#     main()


# #result = file_writer_tool._run('example.txt', 'This is a test content.', 'test_directory')
# #print(result)