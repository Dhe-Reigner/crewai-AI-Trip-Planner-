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



---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crewai-travel-planner.git
cd crewai-travel-planner
```
### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
crewai run


🧪 Example Inputs
        from_city:         Michigan
        destination_city:  Nairobi
        date_from:         17th October 2025
        date_to:           29th October 2025
        interests:         wildlife,safaris,culture
        budget:            $5900

🟰 Expected output:

Suggested round-trip flights (NYC ↔ Mombasa)

10-day itinerary: beach days, Swahili cuisine, Fort Jesus tour

Recommended Airbnbs and hotels

Total budget estimate (flights, food, accommodation, activities)

Local tips on weather and customs


📄 License

This project is licensed under the MIT License.

🤝 Contributing

Pull requests are welcome! If you’d like to contribute a new agent, improve prompts, or integrate new APIs, feel free to fork the repo and submit a PR.

🧠 Inspiration

This project was inspired by the need for intelligent, modular, and personalized travel planning — reducing the hassle and time spent manually researching different parts of a trip. CrewAI’s agent-based system provides a perfect architecture for such collaboration.

🌐 Connect

Twitter: @yourhandle

LinkedIn: Your Name

Project Demo (Coming soon...)


---

Would you like me to help you scaffold this structure in code as well (i.e., agents, tasks, `main.py`, etc.)? I can give you a project boilerplate tailored to this use case.
