import logging 
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

