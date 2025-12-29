import os
import cv2
import numpy as np
import torch
from segment_anything import sam_model_registry, SamPredictor

# -------------------------
# PATH SETUP
# -------------------------
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

SAM_CHECKPOINT = os.path.join(
    BASE_DIR, "models", "sam_vit_h_4b8939.pth"
)

MODEL_TYPE = "vit_h"
device = "cuda" if torch.cuda.is_available() else "cpu"

sam = sam_model_registry[MODEL_TYPE](checkpoint=SAM_CHECKPOINT)
sam.to(device=device)

predictor = SamPredictor(sam)

# -------------------------
# BACKGROUND REMOVAL
# -------------------------
def remove_background(input_path, output_path):
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Image not found")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    predictor.set_image(image_rgb)

    h, w, _ = image.shape

    # 🔥 Bounding box covering most of the image
    input_box = np.array([0, 0, w, h])

    masks, _, _ = predictor.predict(
        box=input_box,
        multimask_output=False
    )

    mask = (masks[0] * 255).astype(np.uint8)

    rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    rgba[:, :, 3] = mask

    cv2.imwrite(output_path, rgba)
