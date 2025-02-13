#!/usr/bin/env python3

from typing import List, Optional

from pydantic import BaseModel


class WhisperConfig(BaseModel):
    model_name: str
    device: str
    language: str

    allow_padding: bool = False
    temperatures: List[float]
    fp16: bool = True
    compression_ratio_threshold: Optional[float] = 2.4
    logprob_threshold: Optional[float] = -1.0
    no_captions_threshold: Optional[float] = 0.6
    best_of: int = 5
    beam_size: Optional[int] = None
    no_speech_threshold: Optional[float] = 0.6
    logprob_threshold: Optional[float] = -1.0
    compression_ratio_threshold: Optional[float] = 2.4


class ParsedChunk(BaseModel):
    start: float
    end: float
    text: str
    tokens: List[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float
