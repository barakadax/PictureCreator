from agents.image import ImageAgent
from generators.image import ImageGenerator
from entities.imageRequest import ImageRequest
from configs.imageAgent import ImageAgentConfig
from configs.imageGen import ImageGeneratorConfig

if __name__ == '__main__':
    imageAgentConfig = ImageAgentConfig()
    imageGenConfig = ImageGeneratorConfig()
    imageRequest = ImageRequest(
        prompt='spaghetti meatballs with tomato sauce and mozzarella' + ' displayed in the center of the image',
        negPrompt='unrealistic, abstract, deformed, disfigured, poor details, words, unbalanced composition, worst quality, normal quality, \
low quality, low res, blurry, text, watermark, logo, banner, extra digits, cropped, jpeg artifacts, signature, username, error, sketch, \
duplicate, ugly, monochrome, horror, geometry, mutation, disgusting, nsfw, nude, focus on one area, pixelated')

    imageGenerator = ImageGenerator(imageGenConfig)
    generated_images = imageGenerator.run(imageRequest)

    imageAgent = ImageAgent(imageAgentConfig)
    # Must for each generated image
    enhanced_images = imageAgent.default_enhance(generated_images)

    # Extra abilities
    grey_scaled_images = imageAgent.grey_scaler(enhanced_images)
    negative_images = imageAgent.negative(enhanced_images)
    without_specific_color = imageAgent.hide_specific_color(enhanced_images, [255, 255, 255])  # color as configuration/input...
