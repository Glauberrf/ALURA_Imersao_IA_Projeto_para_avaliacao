import google.generativeai as genai

#Função para obter as respostads do Gemini
def GeminiBot(prompt):
  
    GOOGLE_API_KEY="API_KEY_GEMINI"
    genai.configure(api_key=GOOGLE_API_KEY)

    #Listando os modelos disponíveis
    '''for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)'''

    generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
    }

    safety_settings={
        'HATE': 'BLOCK_NONE',
        'HARASSMENT': 'BLOCK_NONE',
        'SEXUAL' : 'BLOCK_NONE',
        'DANGEROUS' : 'BLOCK_NONE'
        }

    model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                    generation_config=generation_config,
                                    safety_settings=safety_settings,)

    chat = model.start_chat(history=[])

    response = chat.send_message(prompt)
    return response.text
