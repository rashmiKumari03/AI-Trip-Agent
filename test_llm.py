from dotenv import load_dotenv
load_dotenv(override=True)

import os
from llm_config import get_llm


def test_llm():
    print("\n🚀 Starting LLM test script...")

    print("📦 Creating LLM...")
    llm = get_llm()

    print("📡 Sending test prompt...")

    try:
        resp = llm.invoke("Reply only with: EURON LLM is working.")

        print("\n📨 RAW RESPONSE:", resp)
        print("📨 CONTENT:", resp.content)

        if "working" in resp.content.lower():
            print("\n🎉 SUCCESS — EURON gateway authenticated & responding!\n")
        else:
            print("\n⚠️ Response received but unexpected format.\n")

    except Exception as e:
        print("\n❌ FAILED TO CALL EURON\n")
        print("ERROR TYPE:", type(e))
        print("ERROR:", e)


if __name__ == "__main__":
    test_llm()
