from pydantic import BaseModel, validator

class ImageRequest(BaseModel):
    prompt: str
    negPrompt: str

    @validator("prompt", pre=True)
    def prompt_validator(cls, v: str) -> str:
        if v == None or v == "":
            raise ValueError('Must contain prompt to create an image')
        return v

    @validator("negPrompt", pre=True)
    def negative_prompt_validator(cls, v: str) -> str:
        return "" if v is None else v
