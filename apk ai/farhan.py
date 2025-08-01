import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  
)

def chatbot(message, history):
    chat_history = []
    for user_msg, bot_msg in history:
        chat_history.append({"role": "user", "content": user_msg})
        chat_history.append({"role": "assistant", "content": bot_msg})

    chat_history.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",  
            messages=chat_history
        )
        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print("❌ Terjadi kesalahan:", e)
        return "Maaf, terjadi kesalahan dalam memproses pesan Anda."

demo = gr.ChatInterface(
    fn=chatbot,
    title="Bazz AI"
)

demo.launch(share=True)
