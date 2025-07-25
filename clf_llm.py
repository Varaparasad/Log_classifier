from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq=Groq()


def classify_with_llm(log_message):
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    only return the category name.No preamble. 
    Log message: {log_message}'''

    chat=groq.chat.completions.create(
        model='meta-llama/llama-4-scout-17b-16e-instruct',
        messages=[
            {   'role':'user',
                'content':prompt
            }
        ]
    )
    return chat.choices[0].message.content


if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))