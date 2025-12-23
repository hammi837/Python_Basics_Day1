def summarization_prompt(text):
    return [
        {"role": "system", "content": "You are a professional summarization assistant."},
        {"role": "user", "content": f"Summarize the following text:\n{text}"}
    ]

def rewriting_prompt(text):
    return [
        {"role": "system", "content": "You rewrite text to be clearer and more professional."},
        {"role": "user", "content": f"Rewrite the following text:\n{text}"}
    ]

def classification_prompt(text):
    return [
        {"role": "system", "content": "Classify the text into one category: Positive, Negative, Neutral."},
        {"role": "user", "content": text}
    ]

def keyword_prompt(text):
    return [
        {"role": "system", "content": "You are a helpful assistant that extracts important keywords from text."},
        {"role": "user", "content": f"Extract keywords from this text, separated by commas:\n{text}"}
    ]
