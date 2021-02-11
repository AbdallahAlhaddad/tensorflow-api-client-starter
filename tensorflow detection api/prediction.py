
import numpy as np
import tensorflow as tf
from io import BytesIO
from PIL import Image
from tensorflow.keras.applications.imagenet_utils import decode_predictions


model = None
dimensions = (224, 224)


def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("model loaded")
    return model


def read_imagefile(image_encoded) -> Image.Image:
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


def preproccess(image: Image.Image):
    image = np.asarray(image.resize(dimensions))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    return image


def predict(image: Image.Image):
    # make sure model is loaded:
    global model
    if model is None:
        model = load_model()

    image = preproccess(image)

    # make predictions:
    results = decode_predictions(model.predict(image), 2)[0]

    # create response:
    response = []
    for i, res in enumerate(results):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"

        response.append(resp)

    return response
