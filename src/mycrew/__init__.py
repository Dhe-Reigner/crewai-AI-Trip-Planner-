from crewai.tools import tool
import requests

@tool
def google_flights_tool(departure_id: str, arrival_id: str, outbound_date: str, return_date: str = "", travel_class: str = "ECONOMY", adults: int = 1):
    """
    Searches for flights using the Google Flights API (via RapidAPI).
    Returns a list of flight options including airline, flight number, times, duration, and price.
    """
    url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"

    querystring = {
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "travel_class": travel_class,
        "adults": str(adults),
        "show_hidden": "1",
        "currency": "USD",
        "language_code": "en-US",
        "country_code": "US",
        "search_type": "best"
    }

    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",  # Replace with your actual key
        "x-rapidapi-host": "google-flights2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return {"error": f"Failed to fetch flights. Status: {response.status_code}", "details": response.text}

    return response.json()


@tool
def airbnb_search_tool(place_id: str, adults: int = 1, currency: str = "USD"):
    """
    Searches Airbnb listings by place ID.
    """
    url = "https://airbnb19.p.rapidapi.com/api/v2/searchPropertyByPlaceId"

    querystring = {
        "placeId": place_id,
        "adults": str(adults),
        "guestFavorite": "false",
        "ib": "false",
        "currency": currency,
    }

    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "airbnb19.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return {"error": f"Airbnb API failed: {response.status_code}", "details": response.text}

    return response.json()


@tool
def hotels_com_get_regions(query: str, domain: str = "US", locale: str = "en_US"):
    """
    Search for regions/locations using Hotels.com API to get place IDs or region info.
    """
    url = "https://hotels-com-provider.p.rapidapi.com/v2/regions"

    querystring = {
        "query": query,
        "domain": domain,
        "locale": locale,
    }

    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "hotels-com-provider.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return {"error": f"Failed to get regions: {response.status_code}", "details": response.text}

    return response.json()

@tool
def generate_daily_itinerary_schedule(tasks, working_hours, energy_levels, breaks, language="en"):
    """
    Generate a daily itinerary schedule based on tasks, working hours, energy levels, and breaks.
    
    Args:
        tasks (list): List of tasks to schedule.
        working_hours (dict): Working hours for each day.
        energy_levels (list): Energy levels for scheduling breaks.
        breaks (list): Scheduled breaks during the day.
        language (str): Language of the output (default: "en").
    
    Returns:
        dict: The generated itinerary schedule as JSON.
    """
    url = "https://ai-daily-task-planner-smart-to-do-generator-schedule-api.p.rapidapi.com/schedule"
    querystring = {"noqueue": "1", "language": language}
    payload = {
        "tasks": tasks,
        "workingHours": working_hours,
        "energyLevels": energy_levels,
        "breaks": breaks
    }
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "ai-daily-task-planner-smart-to-do-generator-schedule-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    if response.status_code != 200:
        return {"error": response.status_code, "message": response.text}
    return response.json()

@tool
def convert_currency(amount: float, from_currency: str, to_currency: str):
    """
    Convert a specified amount from one currency to another using the currency conversion API.

    Args:
        amount (float): The amount of money to convert.
        from_currency (str): The currency code to convert from (e.g., "USD").
        to_currency (str): The currency code to convert to (e.g., "EUR").

    Returns:
        dict: Contains the converted amount, exchange rate used, and the date of the rate.
    """
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries"
    querystring = {
        "start_date": "2025-01-01",  # example dates
        "end_date": "2025-12-31",
        "base": from_currency.upper(),
        "symbols": to_currency.upper()
    }
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return {"error": response.status_code, "message": response.text}
    data = response.json()
    # Get latest exchange rate available in the data
    latest_date = max(data['rates'].keys())
    rate = data['rates'][latest_date][to_currency.upper()]
    converted_amount = amount * rate
    return {
        "converted_amount": converted_amount,
        "exchange_rate": rate,
        "date": latest_date
    }


@tool
def get_weather_forecast(latitude, longitude, language="EN"):
    
    """
    Fetch a 5-day weather forecast for the given location coordinates.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        language (str, optional): Language code for the weather description. Defaults to "EN".

    Returns:
        list: A simplified list of daily weather summaries including date, min/max temperature, and description.
    """
    import requests
    
    url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"
    querystring = {
        "latitude": str(latitude),
        "longitude": str(longitude),
        "lang": language
    }
    
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code != 200:
        return {"error": response.status_code, "message": response.text}
    
    data = response.json()
    
    # Simplify data - just return date, min/max temps, weather description for each day
    forecast_summary = []
    for day in data.get("list", []):
        forecast_summary.append({
            "date": day.get("dt_txt"),
            "temp_min": day.get("main", {}).get("temp_min"),
            "temp_max": day.get("main", {}).get("temp_max"),
            "weather": day.get("weather", [{}])[0].get("description")
        })
    
    return forecast_summary

@tool
def get_currency_exchange(base_currency, target_currency, date=None):
    """
    Retrieve the exchange rate between base_currency and target_currency for a specific date.
    If no date is provided, use today's date.

    Args:
        base_currency (str): The currency code to convert from (e.g., "USD").
        target_currency (str): The currency code to convert to (e.g., "KES").
        date (str, optional): The date for the exchange rate in "YYYY-MM-DD" format. Defaults to today's date.

    Returns:
        dict: Contains base_currency, target_currency, date, and the exchange_rate or error details.
    """
    import requests
    from datetime import datetime

    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/timeseries"

    # If no date given, use today's date (format YYYY-MM-DD)
    if date is None:
        date = datetime.utcnow().strftime("%Y-%m-%d")

    querystring = {
        "start_date": date,
        "end_date": date,
        "base": base_currency.upper(),
        "symbols": target_currency.upper()
    }

    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return {"error": response.status_code, "message": response.text}

    data = response.json()

    # Extract the exchange rate for the given date
    rates = data.get("rates", {})
    rate_info = rates.get(date, {})
    exchange_rate = rate_info.get(target_currency.upper())

    if exchange_rate is None:
        return {"error": "Rate not found for the given date"}

    return {
        "base_currency": base_currency.upper(),
        "target_currency": target_currency.upper(),
        "date": date,
        "exchange_rate": exchange_rate
    }


@tool
def get_local_events(location: str, date_range: list):
    """
    Fetch local events happening in the specified location and date range.
    Returns detailed information for up to 5 upcoming events.

    Args:
        location (str): The location name or city.
        date_range (list): List or tuple with two date strings [start_date, end_date] in YYYY-MM-DD format.

    Returns:
        dict: Contains 'events' key with a list of event details or error message.
    """
    import requests

    # Step 1: Search for events by location and date_range (assuming API supports this)
    search_url = "https://real-time-events-search.p.rapidapi.com/search-events"
    search_querystring = {
        "location": location,
        "start_date": date_range[0],
        "end_date": date_range[1]
    }
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "real-time-events-search.p.rapidapi.com"
    }
    search_response = requests.get(search_url, headers=headers, params=search_querystring)
    if search_response.status_code != 200:
        return {"error": search_response.status_code, "message": search_response.text}
    events = search_response.json().get("events", [])
    if not events:
        return {"message": "No events found for given location and date range"}

    # Step 2: For each event, fetch detailed info (limit to first 5 for brevity)
    event_details_list = []
    detail_url = "https://real-time-events-search.p.rapidapi.com/event-details"
    for event in events[:5]:
        event_id = event.get("event_id")
        if not event_id:
            continue
        detail_querystring = {"event_id": event_id}
        detail_response = requests.get(detail_url, headers=headers, params=detail_querystring)
        if detail_response.status_code == 200:
            event_details_list.append(detail_response.json())
        else:
            event_details_list.append({"event_id": event_id, "error": detail_response.status_code})

    return {"events": event_details_list}


@tool
def get_cultural_tips(country):
    """
    Fetch cultural tips for a specified country from a vacations guide API.

    Args:
        country (str): Name of the country to get cultural tips for.

    Returns:
        dict: Contains the country name and cultural tips or an error message.
    """
    import requests
    
    url = "https://vacations-details-your-ultimate-guide.p.rapidapi.com/api/countries"
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "vacations-details-your-ultimate-guide.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": response.status_code, "message": response.text}
    
    countries = response.json().get("countries", [])
    
    for c in countries:
        if c.get("name", "").lower() == country.lower():
            # Assuming the API provides cultural tips under 'culture' or similar key
            cultural_info = c.get("culture", "No cultural tips available for this country.")
            return {"country": country, "cultural_tips": cultural_info}
    
    return {"message": f"No data found for country: {country}"}

from typing import List

@tool
def search_restaurants(location_id: str) -> dict:
    """
    Search for restaurants at a given location using TripAdvisor API.

    Args:
        location_id (str): The location identifier for the search.

    Returns:
        dict: API response JSON or error message.
    """
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"
    querystring = {"locationId": location_id}
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

@tool
def get_driving_route(waypoints: List[str], mode: str = "drive") -> dict:
    """
    Get a driving route between waypoints using a trip planner API.

    Args:
        waypoints (List[str]): List of GPS coordinates as strings "lat,lon".
        mode (str): Mode of transportation, default is "drive".

    Returns:
        dict: API response JSON or error message.
    """
    url = "https://all-in-one-trip-planner.p.rapidapi.com/routing"
    wp_str = "|".join(waypoints)
    querystring = {"waypoints": wp_str, "mode": mode}
    headers = {
        "x-rapidapi-key": "3ceb07361amsh6c1153bf5b2960ep1ce0dfjsn1e6e0170dbb8",
        "x-rapidapi-host": "all-in-one-trip-planner.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
