import openai


def task(habit, reason, time, duration):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"I want to {habit} because {reason}. Can you make me a {time}-{duration} plan of how I "
                        + f"can work towards this goal? This plan should be specific, achievable, measurable,"
                        + f" and reasonable, and should be split up into tasks for each {duration} "
                        + f"(Example: {duration}1: [content], {duration}2: [content]...). Use the most accurate, "
                        + f"efficient, and up-to-date research in making this plan to ensure that if I remain "
                        + f"consistent with this plan, I will accomplish my goal. Once the plan is made, collate the"
                          f" information into a json file with the {duration}s being the key and the tasks being the "
                        + f"value."},

            {"role": "assistant", "content": "Here is the json file:"}
        ],
        temperature=0.5,
    )
    # Pulls just the plan
    plan = response.choices[-1].message.content.strip()
    return plan


