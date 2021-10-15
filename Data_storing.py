import os
from PIL import Image
import imagehash

# basepath = r"D:\Pictures\test"
# images = []
# for image in os.listdir(basepath):
#     open_image = os.path.join(basepath, image)
#     open = Image.open(open_image)
#     images.append(open)

def user_prompt():
    user_input = input("Please, provide the path to the image map\n")

    def get_image(path):
        images = []
        for image in os.listdir(user_input):
            open_image = os.path.join(user_input, image)
            open = Image.open(open_image)
            images.append(open)
        return images

    def open_image(image_list, show_content="individual"):
        if show_content.lower() == "all":
            for image in image_list:
                image.show()
                break
        print(f"total images in the map: {len(image_list)}")
        user_selection = input("which image do you want to see? (provide file name)\n")
        for i, image in enumerate(image_list):
            if f"{user_input}\{user_selection}" == image.filename:
                image_list[i].show()
            else:
                raise Exception("image not in the list")

    image_list = get_image(user_input)

    while user_input != "quit":
        print("Image saved")
        print("Fucntion list\n"
              "---------------\n"
              "show image")
        user_input = input("what function do you need?\n")
        if user_input.lower() == "show image":
            image_choice = input("do you want to see all images? y/n\n")
            if image_choice.lower() == "y":
                open_image(image_list, show_content="all")
            else:
                open_image(image_list)


if __name__ == '__main__':
    #D:\Pictures\test
    #20180707_065314.jpg
    user_prompt()