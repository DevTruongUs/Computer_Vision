import os
from PIL import Image

def load_image(image_path):
    """
        Doc anh tu duong dan cho truoc va tra ve doi tuong anh
        Args: image_path
        Returns: doi tuong hinh anh
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Loi khi doc hinh anh tu: ", image_path, " ", e)
        return None
    
def is_image_file(file_path):
    """
        return True: Neu la anh
               False: Neu khong phai la anh
    """
    extensions =(".jpg", ".jpeg", ".png", ".gif", ".bmp")
    return file_path.lower().endswith(extensions)

def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                image_list.append(img)
    return image_list