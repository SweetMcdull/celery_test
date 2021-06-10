#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Mandelbrot(BaseModel):
    n_max: int = 500
    some_threshold: float = 4.
    nx: int = 500
    ny: int = 500
