
import cv2 
import os 
from paddleocr import *

image_paths = [
    "images/image1.png",
    "images/image2.png",
    "images/image3.png"
]

output_path = "text.txt"

ocr = PaddleOCR(
    lang="fa",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

os.makedirs("results", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:

    for image_path in image_paths:

        print("Reading:", image_path)

        image = cv2.imread(image_path)

        if image is None:
            print("Image not found:", image_path)
            continue

        result = ocr.predict(image)

        file.write("\n" + "=" * 40 + "\n")
        file.write(image_path + "\n")
        file.write("=" * 40 + "\n")

        for res in result:
            data = res.json["res"]

            for text in data["rec_texts"]:
                if text.strip():
                    print(text)
                    file.write(text + "\n")

print("OCR finished!")
