from fastapi import FastAPI, Form
from fastapi.responses import Response
import openai
import os

app = FastAPI()

@app.post("/api/respond")
async def respond(Body: str = Form(...)):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    system_prompt = """You are CaB Solutions’ official assistant. You help professionals learn about Revit, BIM, Quantity Takeoff, AutoCAD Civil 3D, and AI tools for AEC. Your responses are friendly, concise, and helpful. If asked about course details, pricing, or registration, use only the information provided below:

    Courses available:
    - Master Revit Architecture in 21 Days
    - Revit MEP (HVAC)
    - Revit Structure 2025
    - Quantity Takeoff with Revit
    - Generative AI for Architects

    Promo: 25% discount until Sept 30 (use code “cab25”)

    Website: https://online.mycabsolutions.com

    Support: WhatsApp 0559728212 or 0538274301
    """

    chat_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": Body}
        ]
    )

    reply = chat_response.choices[0].message.content.strip()

    return Response(
        content=f"""<?xml version="1.0" encoding="UTF-8"?>
        <Response><Message>{reply}</Message></Response>""",
        media_type="application/xml"
    )
