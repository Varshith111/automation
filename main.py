from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    name = data['name']
    company = data['company']
    website = data['website']

    prompt = f"""
    Write a cold email to {name} from {company}. Offer web development and marketing services from VRAZEAL. Mention you saw their site {website} and how you can help them.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cold email expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"email": response.choices[0].message.content.strip()})
