import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load env immediately
load_dotenv(override=True)


def get_llm(model="gpt-4.1-mini", temperature=0.7):

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing")

    if not base_url:
        raise RuntimeError("OPENAI_BASE_URL is missing")

    print(f"Using LLM gateway: {base_url}")

    return ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=api_key,
        base_url=base_url,
        default_headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
