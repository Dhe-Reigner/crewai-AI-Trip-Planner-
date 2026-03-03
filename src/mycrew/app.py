import streamlit as st
#from mycrew.crew import Mycrew
from crew import Mycrew
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os



load_dotenv()
import os

api_key= os.getenv("HUGGINGFACE_API_KEY")
#llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=api_key)

def main():
    st.set_page_config(page_title="AI-Powered Trip Planner", page_icon="✈️")
    st.title("✈️ AI-Powered Trip Planner")

    st.markdown("""

Enter your travel details and let our AI-powered travel assistant craft a personalized, end-to-end travel plan just for you. We'll take care of everything:

🛫 
Flight Options

🏨 Accommodation Recommendations


🗺️ Daily Itinerary Planner


🌤️ Local Info & Travel Tips


💰 Budget Estimator & Expense Tracker


🧭 All-in-One Travel Plan

    """)

    with st.sidebar:
        st.header("Travel Details")
        col1, col2 = st.columns(2)
        with col1:

            from_city = st.text_input(" 🌆 Origin City",           placeholder= "Michigan")
            destination_city = st.text_input("🌇 Destination City", placeholder="Nairobi")
            date_from = st.text_input("📅 Departure Date",placeholder= "17th October 2025")
            date_to = st.text_input("📅 Return Date",placeholder= "29th October 2025")

            options = [
                # Tourism & Leisure
                "🌿 Nature & Wildlife",
                "🏝️ Beaches, Islands & Coast",
                "🎭 Culture, History & Local Life",
                "🏔️ Mountains & Scenery",
                "🏛️ History & Museums",
                "🍽️ Food & Drink (e.g., cooking classes, food tours, Michelin stars, street food)",
                "🎨 Art & Culture (e.g., galleries, theatre, live music)",
                "🧗 Adventure & Outdoors (e.g., hiking, kayaking, sports)",
                "🌃 Nightlife & Partying",
                "🛍️ Shopping (e.g., luxury brands, local markets, unique boutiques)",
                "🧘 Relaxation & Wellness (e.g., spas, beaches, scenic parks)",
                "🗺️ Off-the-beaten-path (e.g., hidden gems, local experiences)",

                # Business & Professional
                "💼 Business (e.g., conferences, meetings, networking events)",
                "🏢 Coworking Spaces & Business Centers",
                "📈 Industry Events & Trade Shows",

                # Education & Learning
                "🎓 Education (e.g., university visits, language courses, workshops)",
                "📚 Seminars & Professional Development",
                "🧪 Research & Academic Collaboration",

                # Other Logical Categories
                "🏥 Healthcare & Medical (e.g., clinics, wellness checks)",
                "🤝 Volunteering & Social Impact",
                "👨‍👩‍👧‍👦 Family & Friends Visits",
                "🕌 Religious & Spiritual Sites",
                "🚀 Tech & Innovation Hubs",
                "🎤 Public Speaking & Events",
            ]

            interests =  st.multiselect(label="📋 Choose your top 3-5",options=options)

            group_size  = st.text_input("🧑‍🤝‍🧑 Group Size",placeholder= "Solo traveler,couple")
        with col2:
            mode_of_transport = st.selectbox(
                        label="🚌 What is your desired mode of transport?",
                        options=["Relying on public transport", "Walking as much as possible","Renting a car","Using taxis / ride-sharing apps"]
                    )
            pace = st.selectbox(
                        label="🚶🏻‍♂️‍➡️ What is your desired pace of travel?",
                        options=["Action-packed(See as much as possible, early mornings, late nights.)", "Relaxed(A few key sights with plenty of downtime, lazy mornings, spontaneous wandering).","A good mix(Busy days balanced with some relaxation.)"]
                    )
            
            accomodation_style = st.selectbox(
                        label="🏢 What is your desired accomodation style?",
                        options=["Hotel (Luxury, Boutique, Chain)", "Hostel","Airbnb / Vacation Rental","Bed & Breakfast"]
            )
            budget = st.text_input("💲 Budget",placeholder= "$5900")
            must_do = st.text_input("📝 Must do",placeholder= "Dinner reservation at Nokras on...")
            anything_to_avoid = st.text_input("🚫 Anything to avoid",placeholder="Not interested in nightlife.")

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
                
                crew_result = crew_instance.kickoff(inputs=inputs)
                

                
                st.subheader("Your AI-Powered Travel Plan")
                st.markdown(crew_result)

                # Display results from markdown files
                st.write("---_---")
                st.header("Detailed Reports")

                files = ["flight.md", 
                "accomodation.md", 
                "itinery.md", 
                "local_info.md", 
                "budget.md",
                 "planner.md"]
                combined_content = ""
                
                for file in files:
                    try:
                        with open(file, 'r') as f:
                            
                            st.subheader(f"{file.replace('.md', '').replace('_', ' ').title()}")
                            st.markdown(f.read())

                            # combined_content += f"\n\n"
                            # combined_content += f.read()
                    except FileNotFoundError:
                            combined_content += f"\n\n"

                            st.header("Detailed Reports")

                            st.download_button(
                                label="Download Full Travel Plan",
                                data=combined_content,
                                file_name="planner.md",
                                mime="text/markdown",
                                icon=":material/download:",

                            )
                            
                    except FileNotFoundError:
                        st.warning(f"Could not find {file}.")
                    except Exception as e:
                        st.error(f"An error occurred while reading {file}: {e}")


            # except litellm.RateLimitError as e:
            #         st.error("API quota exceeded. Please try again later or upgrade your plan.")


            except Exception as e:
                            st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
