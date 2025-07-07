def combine_scores(text_score, image_score, source_score):
    weights = [0.4, 0.4, 0.2]
    scores = [text_score or 0.5, image_score or 0.5, source_score or 0.5]
    final = sum([w*s for w, s in zip(weights, scores)])
    return round(final * 100, 2)
