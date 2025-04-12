import gradio as gr
import google.generativeai as genai

# Replace with your actual Gemini API key
GENAI_API_KEY = "AIzaSyB9QBtGs9XB6AL6wYD6nJeqI5pQXqsUgDQ"  # <--- Replace this!
genai.configure(api_key=GENAI_API_KEY)

# Select the model
MODEL_NAME = 'models/gemini-1.5-pro-latest'
model = genai.GenerativeModel(MODEL_NAME)


def generate_meal_plan(dietary_preferences, allergies, ingredients):
    """
    Generates a meal plan using the Gemini API.

    Args:
        dietary_preferences (str): User's dietary preferences (e.g., vegetarian, vegan).
        allergies (str): User's allergies (e.g., nuts, dairy).
        ingredients (str): Available ingredients.

    Returns:
        str: The generated meal plan.
    """
    prompt = f"Generate a 7-day meal plan with the following preferences: {dietary_preferences}. Allergies: {allergies}. Available ingredients: {ingredients}."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating meal plan: {e}"


def generate_excuse(situation):
    """
    Generates an excuse using the Gemini API.

    Args:
        situation (str): The situation for which an excuse is needed.

    Returns:
        str: The generated excuse.
    """
    prompt = f"Generate a creative and believable excuse for: {situation}."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating excuse: {e}"



def generate_reminder(task, date_time):
    """
    Generates a reminder using the Gemini API.
    This is a placeholder; actual reminder setting requires system-level integration.
    This function generates the reminder text.

    Args:
        task (str): The task to be reminded about.
        date_time (str): The date and time of the reminder.

    Returns:
        str: The reminder text.
    """
    prompt = f"Generate a reminder message for the following task: {task} on {date_time}."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating reminder: {e}"


def generate_entertainment_suggestion(interests):
    """
    Generates entertainment suggestions using the Gemini API.

    Args:
        interests (str): User's interests.

    Returns:
        str: The generated entertainment suggestions.
    """
    prompt = f"Suggest movies, books, or activities based on these interests: {interests}."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating entertainment suggestion: {e}"

def generate_summary(text):
    """
    Generates summary of a given text using the Gemini API.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summary of the text.
    """
    prompt = f"Summarize the following text: {text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating summary: {e}"


def ai_roommate_interface():
    """
    Defines the Gradio interface for the AI Roommate application.
    """
    with gr.Blocks(title="AI Roommate") as iface:
        gr.Markdown("# AI Roommate: Your Personalized Life Assistant")

        with gr.Tab("Meal Planner"):
            diet_input = gr.Textbox(label="Dietary Preferences (e.g., vegetarian, vegan)")
            allergy_input = gr.Textbox(label="Allergies (e.g., nuts, dairy)")
            ingredient_input = gr.Textbox(label="Available Ingredients")
            meal_plan_output = gr.Textbox(label="Meal Plan")
            meal_plan_button = gr.Button("Generate Meal Plan")
            meal_plan_button.click(generate_meal_plan, inputs=[diet_input, allergy_input, ingredient_input], outputs=meal_plan_output)

        with gr.Tab("Excuse Generator"):
            situation_input = gr.Textbox(label="Situation (e.g., missing a meeting, being late)")
            excuse_output = gr.Textbox(label="Excuse")
            excuse_button = gr.Button("Generate Excuse")
            excuse_button.click(generate_excuse, inputs=situation_input, outputs=excuse_output)

        with gr.Tab("Reminder"):
            task_input = gr.Textbox(label="Task")
            date_time_input = gr.Textbox(label="Date and Time (e.g., 2024-07-20 14:00)")
            reminder_output = gr.Textbox(label="Reminder")
            reminder_button = gr.Button("Set Reminder")
            reminder_button.click(generate_reminder, inputs=[task_input, date_time_input], outputs=reminder_output)

        with gr.Tab("Entertainment Suggestions"):
            interests_input = gr.Textbox(label="Your Interests")
            entertainment_output = gr.Textbox(label="Suggestions")
            entertainment_button = gr.Button("Get Suggestions")
            entertainment_button.click(generate_entertainment_suggestion, inputs=interests_input, outputs=entertainment_output)

        with gr.Tab("Text Summarizer"):
            text_input = gr.Textbox(label="Text to Summarize", lines=7)
            summary_output = gr.Textbox(label="Summary", lines=3)
            summary_button = gr.Button("Summarize")
            summary_button.click(generate_summary, inputs=text_input, outputs=summary_output)

    return iface



if __name__ == "__main__":
    iface = ai_roommate_interface()
    iface.launch()
