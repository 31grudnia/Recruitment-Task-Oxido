from dotenv import load_dotenv
import os

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

MODEL = "gpt-4o"
ARTICLES_STORAGE_PATH = "data/articles/"