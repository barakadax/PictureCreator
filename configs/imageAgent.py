import os
from pydantic import BaseModel, Field

class ImageAgentConfig(BaseModel):
    contrast: float = Field(default_factory=lambda: float(os.getenv('PIPELINE_CONTRAST', 1.2)), allow_mutation=False)
    sharpness: float = Field(default_factory=lambda: float(os.getenv('PIPELINE_SHARPNESS', 1.2)), allow_mutation=False)