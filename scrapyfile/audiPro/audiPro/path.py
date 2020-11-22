import os
images_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"img")
if not os.path.exists(images_path):
    os.mkdir(images_path)
