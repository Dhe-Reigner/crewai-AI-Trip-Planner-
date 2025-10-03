import streamlit as st
#from mycrew.crew import Mycrew
from crew import Mycrew




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
        interests = st.text_area("Your Interests", "wildlife, safaris, culture")
        budget = st.text_input("Budget", "$5900")

    if st.button("Generate Travel Plan"):
        if not all([from_city, destination_city, date_from, date_to, interests, budget]):
            st.error("Please fill in all the fields to generate a travel plan.")
        else:
            inputs = {
                'from_city': from_city,
                'destination_city': destination_city,
                'date_from': date_from,
                'date_to': date_to,
                'interests': interests,
                'budget': budget
            }

            with st.spinner("Generating your personalized travel plan..."):
                try:
                    my_crew_instance = Mycrew()
                    crew_result = my_crew_instance.crew().kickoff(inputs=inputs)
                    
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

                except Exception as e:
                    st.error(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    main()
