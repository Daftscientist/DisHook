from typing import List, Optional

class Webhook:
    
    def __init__(self,
                 webhook_url: str,
                 wait: Optional[str] = True,
                 thread_id: Optional[int] = None,
                 username: Optional[str] = None,
                 avatar_url: Optional[str] = None,
                 ) -> None:
        self.webhook_url = webhook_url
        self.wait = wait
        self.thread_id = thread_id
        self.username = username
        self.avatar_url = avatar_url
        self.webhook_content = None

    def set_webhook_content(self, content: WebhookContent) -> None:
        self.webhook_content = content

    def send(self) -> None:
        if self.webhook_content is None:
            raise EmptyWebhook("No content to send.")
        requests.post(self.webhook_url, json=self.webhook_content.to_dict())
