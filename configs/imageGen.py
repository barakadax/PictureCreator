import os
from pydantic import BaseModel, Field

class ImageGeneratorConfig(BaseModel):
    model: str = Field(default_factory=lambda: os.getenv('PIPELINE_MODEL', 'prompthero/openjourney'), allow_mutation=False)
    sample: bool = Field(default_factory=lambda: bool(os.getenv('PIPELINE_SAMPLE', True)), allow_mutation=False)
    temperature: float = Field(default_factory=lambda: float(os.getenv('PIPELINE_TEMPERATURE', 0.1)), allow_mutation=False)
    steps: int = Field(default_factory=lambda: int(os.getenv('PIPELINE_STEPS', 10)), allow_mutation=False)
    guidance: int = Field(default_factory=lambda: int(os.getenv('PIPELINE_GUIDANCE', 12)), allow_mutation=False)
    width: int = Field(default_factory=lambda: int(os.getenv('PIPELINE_WIDTH', 512)), allow_mutation=False)
    height: int = Field(default_factory=lambda: int(os.getenv('PIPELINE_HEIGHT', 512)), allow_mutation=False)
    randomness: int = Field(default_factory=lambda: int(os.getenv('PIPELINE_RANDOMNESS', 2**32 - 1)), allow_mutation=False)
