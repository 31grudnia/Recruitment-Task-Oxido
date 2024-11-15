from openai import OpenAI

from config import OPENAI_API_KEY, MODEL


client = OpenAI(api_key=OPENAI_API_KEY)

def openai_prompt(prompt: str) -> str:
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=2048,
            temperature=0,
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Wystąpił błąd: {e}"
    

def prepare_prompt(article_text: str) -> str:
    prompt = (
        "Przekształć poniższy artykuł na kod HTML zgodnie z następującymi wytycznymi:\n"
        "- Użyj odpowiednich tagów HTML do strukturyzacji treści.\n"
        "- Określ miejsca, gdzie warto wstawić grafiki, i oznacz je za pomocą tagu "
        '<img src="image_placeholder.jpg" alt="Tutaj podaj dokładny prompt do wygenerowania grafiki">\n'
        "- Umieść podpisy pod grafikami, używając odpowiedniego tagu HTML.\n\n"
        "Treść artykułu:\n"
        f"{article_text}"
    )
    return prompt