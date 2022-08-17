from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class Webhook(BaseModel):
    webhook_url = str
    default_username = str
    default_profile_picture = str

    @classmethod
    def send():
        print("test")


Webhook().send()