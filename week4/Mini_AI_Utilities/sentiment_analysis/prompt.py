def sentimental_prompt(text):
    return [
     {"role": "system", "content": "You are a sentiment analysis assistant"},
    {"role": "user", "content": text}
    ]