from fastapi import FastAPI, UploadFile, Form
from backend.analyzer.text_analyzer import analyze_text
from backend.analyzer.image_analyzer import analyze_image
from backend.analyzer.source_checker import check_source
from backend.analyzer.aggregator import combine_scores

app = FastAPI()

@app.post("/analyze/")
async def analyze_post(text: str = Form(...), image: UploadFile = None, url: str = Form(None)):
    text_score, text_expl = analyze_text(text)
    image_score, image_expl = await analyze_image(await image.read()) if image else (None, None)
    source_score = check_source(url) if url else None

    final_score = combine_scores(text_score, image_score, source_score)

    return {
        "reliability_score": final_score,
        "text": {"score": text_score, "explanation": text_expl},
        "image": {"score": image_score, "explanation": image_expl},
        "source": {"score": source_score}
    }
