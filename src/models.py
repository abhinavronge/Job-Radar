"""
module for models
"""


from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:
    """
    Job class to represent a job posting
    """

    title: str
    company: str
    location: str
    url: str
    description: str
    source: str
    posted_at: datetime | None = None
