import google.generativeai as genai

GOOGLE_API_KEY = "your_api_key" 

# Configure the Gemini API client
genai.configure(api_key=GOOGLE_API_KEY)

def planner_agent(user_prompt: str) -> str:
    print("🧭 Planner Agent working...\n")
    try:
        # Use a valid model name 
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        # Pass prompt as positional argument (not keyword)
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    user_task = (
        "Plan a 7-day budget-friendly solo travel itinerary through South India. "
        "Include top places to visit, suggested routes, local food recommendations, and estimated cost per day."
    )

    plan = planner_agent(user_task)

    print("\n📌 Travel Plan:\n")
    print(plan)

if __name__ == "__main__":
    main()
