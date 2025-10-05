
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
```
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
```


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
=======
# Mycrew Crew

Welcome to the Mycrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mycrew/config/agents.yaml` to define your agents
- Modify `src/mycrew/config/tasks.yaml` to define your tasks
- Modify `src/mycrew/crew.py` to add your own logic, tools and specific args
- Modify `src/mycrew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the myCrew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The myCrew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Mycrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-57-43" src="https://github.com/user-attachments/assets/1450d30b-4059-4f03-a6e1-86915790464d" />

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-57-55" src="https://github.com/user-attachments/assets/9dd3d1f3-13bd-43de-853c-a2e824a5b930" />


<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-08" src="https://github.com/user-attachments/assets/1a7e8e37-031d-49cf-b1e0-4af66de780fe" />

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-18" src="https://github.com/user-attachments/assets/fe2f3731-f2e6-453b-8611-adb6ec89814c" />


<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-27" src="https://github.com/user-attachments/assets/1a55c66a-0b8a-4988-b484-57d6bc2b4308" />

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-37" src="https://github.com/user-attachments/assets/87292350-96ec-4e26-ab6e-7613ecd93550" />

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-46" src="https://github.com/user-attachments/assets/963b2b55-0de3-4e14-b406-bd63f934efe3" />


<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-58-56" src="https://github.com/user-attachments/assets/a486b4e3-11e5-4c03-a699-28da6ca855e7" />

<img width="1366" height="768" alt="Screenshot from 2025-10-05 12-59-42" src="https://github.com/user-attachments/assets/27fe2e6f-01c7-408f-8fdb-49e48bcc0877" />
