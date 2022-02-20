import imagehash
import os
from PIL import Image
import json

class Image_processing():
    def __init__(self, data, type="dictionary"):
        self.data = data
        self.type = type

    def data_type(self):
        if self.type.lower() == "image":
            image_list = self.image_processing()
            return self.image_hasing(image_list)
        elif self.type.lower() == "dictionary":
            return self.data
        else:
            raise Exception("Cant process this type of data")

    def image_processing(self):
        saved_image = []
        base_path = self.data
        for image in os.listdir(base_path):
            image_file = os.path.join(base_path, image)
            try:
                saved_image.append(Image.open(image_file))
            except Exception as error:
                print(f"Error found: {error}")
        return saved_image

    def image_hasing(self, image_list):
        image_hash = {}
        for image in image_list:
            hash = imagehash.average_hash(image)
            filename = image.filename.split("\\")[-1]
            image_hash[filename]=str(hash)
        return image_hash

class Data_procsseing():
    def __init__(self, data):
        self.data = data

    def save_dict_txt(self, filename, path_to_save):
        with open(f"{path_to_save}\{filename}", "w") as file:
            file.write(json.dumps(self.data))