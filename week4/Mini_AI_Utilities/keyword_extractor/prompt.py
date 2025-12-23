def keyword_prompt(text):
    return [
        {"role": "system", "content": "You are a helpful assistant that extracts important keywords from text."},
        {"role": "user", "content": f"Extract keywords from this text, separated by commas:\n{text}"}
    ]