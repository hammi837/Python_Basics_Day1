def BulletPoint_prompt(text):
    return [
        {"role":"system","content":"you are a profesional converter (text to bullet-point) assistant"},
        {"role":"user","content":f"Convert text to bullet-point notes: \n {text}"}
    
    ]