from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from io import BytesIO
import torch

# Use BLIP Base (much smaller)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cpu")

def caption_image(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert('RGB')
    inputs = processor(images=image, return_tensors="pt").to("cpu")
    generated_ids = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(generated_ids[0], skip_special_tokens=True)
    return caption

def analyze_image(image_bytes):
    caption = caption_image(image_bytes)
    explanation = f"The image was captioned as: {caption}. Comparing with text for consistency."
    return 0.7, explanation  # Placeholder score
