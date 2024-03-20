import random
import numpy as np
from PIL import ImageEnhance, Image
from configs.imageAgent import ImageAgentConfig

class ImageAgent:
    def __init__(self, config: ImageAgentConfig) -> None:
        self.__config = config


    def __rand_value_between_range(self, lower_bound: float, upper_bound: float) -> int:
        random_number = random.uniform(lower_bound, upper_bound)
        random_number = random_number * 10000
        random_number = int(random_number)
        
        return random_number / 10000


    def grey_scaler(self, images: list[Image.Image]) -> list[Image.Image]:
        res: list[Image.Image] = list()

        for index, img in enumerate(images):
            image = np.array(img)
            height, width, _ = image.shape
            r = self.__rand_value_between_range(0.2, 0.3)
            g = self.__rand_value_between_range(0.5, 0.75)
            b = self.__rand_value_between_range(0.07, 0.15)

            for x in range(height):
                for y in range(width):
                    pixel = image[x, y]
                    pixel = pixel[0] * r + pixel[1] * g + pixel[2] * b
                    image[x, y] = pixel

            grey_scaled_picture = Image.fromarray(image.astype('uint8'))
            grey_scaled_picture.save(f'grey_scaled{index}.png')  # remove later
            res.append(grey_scaled_picture)

        return res
    

    def negative(self, images: list[Image.Image]) -> list[Image.Image]:
        res: list[Image.Image] = list()

        for index, img in enumerate(images):
            image = np.array(img)
            height, width, _ = image.shape

            for x in range(height):
                for y in range(width):
                    pixel = image[x, y]
                    pixel[0] = 255 - pixel[0]
                    pixel[1] = 255 - pixel[1]
                    pixel[2] = 255 - pixel[2]
                    image[x, y] = pixel

            negative_image = Image.fromarray(image)
            negative_image.save(f'negative{index}.png') # remove later
            res.append(negative_image)
        
        return res
    

    def hide_specific_color(self, images: list[Image.Image], color_to_remove: list[int]) -> list[Image.Image]:
        res: list[Image.Image] = list()

        for index, img in enumerate(images):
            image = np.array(img.convert("RGBA"))
            height, width, _ = image.shape

            for x in range(height):
                for y in range(width):
                    if image[x,y][0] == color_to_remove[0] and image[x,y][1] == color_to_remove[1] and image[x,y][2] == color_to_remove[2]:
                        image[x,y][3] = 0

            clean_image = Image.fromarray(image)
            clean_image.save(f'clean{index}.png') # remove later
            res.append(clean_image)
        
        return res


    def default_enhance(self, images: list[Image.Image]) -> list[Image.Image]:
        res: list[Image.Image] = list()

        for index, image in enumerate(images):
            contrasted = ImageEnhance.Contrast(image).enhance(self.__config.contrast)
            sharpened = ImageEnhance.Sharpness(contrasted).enhance(self.__config.sharpness)
            res.append(sharpened)

            sharpened.save(f'enhanced{index}.png')  # remove later

        return res
