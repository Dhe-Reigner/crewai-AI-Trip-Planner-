# crewai-AI-Trip-Planner-
🌍 AI-powered Travel Planner built with CrewAI. Plan your entire trip to Kenya with intelligent agents for flights, accommodation, itinerary, budgeting, and local tips — all tailored to your preferences.

# 🧭 AI Travel Planner - Powered by CrewAI

Welcome to the **AI Travel Planner**, a multi-agent travel planning application built using [CrewAI](https://docs.crewai.com/). This project leverages autonomous AI agents to collaboratively plan a personalized trip from the United States to destinations in **Kenya**, including Nairobi, Mombasa, and more.

Each agent in the system handles a distinct part of the travel planning process — from booking flights and accommodation to creating itineraries, estimating budgets, and offering local insights.

---

## ✈️ Use Case

Plan your dream trip to Kenya using AI. Just provide your starting city, preferred Kenyan destination(s), interests, budget, and the number of travelers — and let the AI agents do the rest:

- Suggest best flight options 🛫  
- Recommend hotels or Airbnbs 🏨  
- Generate day-by-day itineraries 🗓️  
- Estimate total trip budget 💰  
- Share local tips and cultural insights 🌍  

---

## 🔧 Technologies Used

- **[CrewAI](https://docs.crewai.com/)** - Multi-agent framework
- **Python 3.12+**
- External APIs (optional): Flights, Hotels, Weather, Currency Conversion

---

## 🧠 Agent Architecture

| Agent           | Goal / Responsibility |
|----------------|------------------------|
| **Planner Agent** | Understand user preferences (origin, destination, interests, budget, group size) and coordinate overall trip planning. |
| **Flight Agent** | Find and suggest optimal flight options including prices, airlines, and travel time. |
| **Accommodation Agent** | Recommend hotel and Airbnb listings based on user preferences, location, and budget. |
| **Itinerary Agent** | Generate personalized daily schedules with activities, sightseeing, and restaurants. |
| **Local Info Agent** | Provide useful local information such as weather, events, culture, and safety tips. |
| **Budget Agent** | Estimate total trip costs, provide cost breakdown, and help track or optimize spending. |

---

## 📂 Project Structure

├── crewai_travel_planner/
│ ├── agents/
│ │ ├── flight_agent.py
│ │ ├── accommodation_agent.py
│ │ ├── itinerary_agent.py
│ │ ├── local_info_agent.py
│ │ ├── budget_agent.py
│ │ └── planner_agent.py
│ ├── tasks/
│ │ └── travel_tasks.py
│ ├── tools/
│ │ └── api_wrappers.py
│ ├── main.py
│ └── config/
│ └── settings.py
├── requirements.txt
└── README.md
