from dotenv import load_dotenv
load_dotenv(override=True)

from config.llm_config import get_llm


def test_llm():

    print("Starting LLM test...")

    llm = get_llm()

    try:
        resp = llm.invoke("Reply only with: LLM is working.")

        print("RAW RESPONSE:", resp)
        print("CONTENT:", resp.content)

        if resp.content and "working" in resp.content.lower():
            print("LLM test successful.")
        else:
            print("Unexpected response format.")

    except Exception as e:
        print("LLM call failed.")
        print("ERROR:", e)


if __name__ == "__main__":
    test_llm()
