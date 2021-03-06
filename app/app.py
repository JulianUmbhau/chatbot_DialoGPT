# %%
from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
# %%

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")

    for step in range(5):
        new_user_input_ids = tokenizer.encode(userText + tokenizer.eos_token, return_tensors="pt")

        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=1) if step > 0 else new_user_input_ids

        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        return str(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))

if __name__ == "__main__":
    # Get port and debug mode from environment variables    
    port = os.environ.get('dash_port')
    debug = os.environ.get('dash_debug')=="True"
    app.run(debug=debug, host="0.0.0.0", port=port)
