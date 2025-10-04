import streamlit as st
#from mycrew.crew import Mycrew
from crew import Mycrew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import litellm

load_dotenv()


keys  =[
    os.getenv("GEMINI_API_KEY_POJECT_MARTOZ"),
    os.getenv("GEMINI_API_KEY_PROJECT_LANGCHAIN101"),
    os.getenv("GEMINI_API_KEY_PROJECT_MARTO"),
    os.getenv("GEMINI_API_KEY_PROJECT_KAGEMA")
]
api_key_to_use = keys[0]
litellm.api_key = api_key_to_use
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro",temperature=0.7,google_api_key=litellm.api_key)

def main():
    st.set_page_config(page_title="AI-Powered Trip Planner", page_icon="✈️")
    st.title("✈️ AI-Powered Trip Planner")

    st.markdown("""
    **Plan your next trip with AI!**

    Enter your travel details below, and our AI-powered travel assistant will create a personalized travel plan, including:
    - Best places to visit
    - Accommodation & budget planning
    - Local food recommendations
    - Transportation & visa details
    """)

    with st.sidebar:
        st.header("Travel Details")
        from_city = st.text_input("Origin City", "Michigan")
        destination_city = st.text_input("Destination City", "Nairobi")
        date_from = st.text_input("Departure Date", "17th October 2025")
        date_to = st.text_input("Return Date", "29th October 2025")
        interests =  st.selectbox(
                            label="Choose your top 3-5",
                        options=["🌿 Nature & Wildlife", "🏝️ Beaches, Islands & Coast", "🎭 Culture, History & Local Life","🏔️ Mountains & Scenery","🏛️ History & Museums","🍽️ Food & Drink (e.g., cooking classes, food tours, Michelin stars, street food)","🎨 Art & Culture (e.g., galleries, theatre, live music)","🧗 Adventure & Outdoors (e.g., hiking, kayaking, sports)","🌃 Nightlife & Partying","🛍️ Shopping (e.g., luxury brands, local markets, unique boutiques)","🧘 Relaxation & Wellness (e.g., spas, beaches, scenic parks)","🗺️ Off-the-beaten-path (e.g., hidden gems, local experiences)"]
                            )
        group_size  = st.text_input("Group Size", "(e.g., Solo traveler, a couple, a family with two young children (ages 5 and 8), a group of 4 friends in their late 20s)")
        mode_of_transport = st.selectbox(
                    label="What is your desired mode of transport?",
                    options=["Relying on public transport", "Walking as much as possible","Renting a car","Using taxis / ride-sharing apps"]
                )
        pace = st.selectbox(
                    label="What is your desired pace of travel?",
                    options=["Action-packed(See as much as possible, early mornings, late nights.)", "Relaxed(A few key sights with plenty of downtime, lazy mornings, spontaneous wandering).","A good mix(Busy days balanced with some relaxation.)"]
                )
        accomodation_style = st.selectbox(
                    label="What is your desired accomodation style?",
                    options=["Hotel (Luxury, Boutique, Chain)", "Hostel","Airbnb / Vacation Rental","Bed & Breakfast"]
                )
        budget = st.text_input("Budget", "$5900")
        must_do = st.text_input("Must do", "Are there any specific attractions, restaurants, or experiences you already know you want to include? (e.g.I absolutely have to see the Eiffel Tower at night, or I have a dinner reservation at Noma.)")
        anything_to_avoid = st.text_input("Anything to avoid", "Are there things you actively dislike or want to avoid? (e.g., No crowded museums,I'm a vegetarian, Not interested in nightlife.)")

    if st.button("Generate Travel Plan"):
        if not all([from_city, destination_city, date_from, date_to, interests, group_size,mode_of_transport,pace,accomodation_style,budget,must_do,anything_to_avoid]):
            st.error("Please fill in all the fields to generate a travel plan.")
        else:
            inputs = {
        "from_city": from_city,
        "destination_city": destination_city,
        "date_from": date_from,
        "date_to": date_to,
        "interests": interests,
        "accomodation_style": accomodation_style,
        "pace of travel": pace,
        "transport":mode_of_transport,
        "group_size": group_size,
        "must_do": must_do,
        "anything_to_avoid": anything_to_avoid,
        "budget": budget,
        # 'topic': 'AI LLMs',
        # 'current_year': str(datetime.now().year)
    }

    with st.spinner("Generating your personalized travel plan..."):
        try:
            # my_crew_instance = Mycrew()
            # crew_result = my_crew_instance.kickoff(inputs=inputs)
            my_crew_instance = Mycrew()

            # get the Crew instance from your Mycrew
            crew_instance = my_crew_instance.crew()

            # then kickoff the crew, passing inputs
            #crew_result = crew_instance.kickoff(inputs=inputs)
            try:
                crew_result = crew_instance.kickoff(inputs=inputs)
            except litellm.RateLimitError as e:
                st.error("API quota exceeded. Please try again later or upgrade your plan.")


            
            st.subheader("Your AI-Powered Travel Plan")
            st.markdown(crew_result)

            # Display results from markdown files
            st.write("---_---")
            st.header("Detailed Reports")

            files = ["flight.md", "accomodation.md", "itinery.md", "local_info.md", "budget.md", "planner.md"]
            for file in files:
                try:
                    with open(file, 'r') as f:
                        st.subheader(f"{file.replace('.md', '').replace('_', ' ').title()}")
                        st.markdown(f.read())
                except FileNotFoundError:
                    st.warning(f"Could not find {file}.")
                except Exception as e:
                    st.error(f"An error occurred while reading {file}: {e}")

            st.download_button(
                     label="Download CSV",
                     data=files,
                     file_name="data.csv",
                     mime="text/plain",
                     icon=":material/download:",
                )

        except Exception as e:
            st.error(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    main()
