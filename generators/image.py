import torch
import random
from PIL import Image
from torch import Generator
from entities.imageRequest import ImageRequest
from configs.imageGen import ImageGeneratorConfig
from diffusers import AutoPipelineForText2Image, EulerDiscreteScheduler

class ImageGenerator:
    def __init__(self, config: ImageGeneratorConfig) -> None:
        self.__config = config
        self.__device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f'Run model on: {self.__device}')

        scheduler = EulerDiscreteScheduler.from_pretrained(config.model, subfolder='scheduler')
        self.__pipeline = AutoPipelineForText2Image.from_pretrained(config.model, scheduler=scheduler, torch_dtype=torch.float).to(self.__device)


    def __generate_image(self, request: ImageRequest, generator: Generator) -> list[Image.Image]:
        image = self.__pipeline(
            prompt=request.prompt,
            negative_prompt=request.negPrompt,
            generator=generator,
            do_sample=self.__config.sample,
            temperature=self.__config.temperature,  # Higher values make output more random, don't max over 1
            num_inference_steps=self.__config.steps,  # Bigger the number the more accurate & detailed the result is
            guidance_scale=self.__config.guidance,  # Lower the value the more creative the model is from the prompt
            height=self.__config.height,
            width=self.__config.width
        ).images

        return image


    def run(self, request: ImageRequest) -> list[Image.Image]:
        random_integer = random.randint(0, self.__config.randomness) # just like salt
        generator = torch.Generator(device=self.__device).manual_seed(random_integer)

        generated_images = self.__generate_image(request, generator)
        for index, image in enumerate(generated_images):  # Remove later
            image.save(f'generated{index}.png')

        return generated_images
