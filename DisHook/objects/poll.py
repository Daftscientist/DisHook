from typing import List, Optional
from .emoji import Emoji

class PollMedia(object):
    """
        Represents the media of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object-poll-media
    """
    text: str
    emoji: Optional[Emoji]

    def __init__(self, text: str, emoji: Optional[Emoji] = None):
        """
            Initializes the poll media.

            Args:
                text (Optional[str]): The text of the poll media.
                emoji (Optional[Emoji], optional): The emoji of the poll media. Defaults to None. Can not be set for a question.
        """

        self.text = text
        self.emoji = emoji
    
    def __dict__(self):
        """
            Returns the dictionary representation of the poll media.

            Returns:
                dict: The dictionary representation of the poll media.
        """
        return {
            "text": self.text,
            "emoji": self.emoji.__dict__() if self.emoji else None
        }

class PollAnswer(object):
    """
        Represents an possible answer to a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object-poll-answer
    """
    answer_id: Optional[int] = None
    poll_media: Optional[PollMedia]

    def __init__(self, answer_id: Optional[int] = None, poll_media: Optional[PollMedia] = None):
        """
            Initializes the poll answer.

            Args:
                answer_id (Optional[int], optional): The answer ID. Defaults to None. Only sent as a response by Discord.
                poll_media (Optional[PollMedia], optional): The media of the poll answer. Defaults to None.
        """
        self.answer_id = answer_id
        self.poll_media = poll_media
    
    def __dict__(self):
        """
            Returns the dictionary representation of the poll answer.

            Returns:
                dict: The dictionary representation of the poll answer.
        """
        return {
            "answer_id": self.answer_id,
            "poll_media": self.poll_media.__dict__()
        }

class PollResultsAnswerCount(object):
    """
        Represents the answer count of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-results-object-poll-results-answer-count
    """
    answer_id: int
    count: int
    me_voted: bool

    def __init__(self, answer_id: int, count: int, me_voted: bool):
        """
            Initializes the answer count of a poll.

            Args:
                answer_id (int): The answer ID.
                count (int): The count of the answer.
                me_voted (bool): Whether the user has voted.
        """
        self.answer_id = answer_id
        self.count = count
        self.me_voted = me_voted
    
    def __dict__(self):
        """
            Returns the dictionary representation of the answer count.

            Returns:
                dict: The dictionary representation of the answer count.
        """
        return {
            "id": self.answer_id,
            "count": self.count,
            "me_voted": self.me_voted
        }

class PollResults(object):
    """
        Represents the results of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-results-object
    """
    is_finalized: bool
    answer_counts: List[PollResultsAnswerCount]

    def __init__(self, is_finalized: bool, answer_counts: List[PollResultsAnswerCount]):
        """
            Initializes the poll results.

            Args:
                is_finalized (bool): Whether the poll is finalized.
                answer_counts (List[PollResultsAnswerCount]): The answer counts of the poll.
        """
        self.is_finalized = is_finalized
        self.answer_counts = answer_counts
    
    def __dict__(self):
        """
            Returns the dictionary representation of the poll results.

            Returns:
                dict: The dictionary representation of the poll results.
        """
        return {
            "is_finalized": self.is_finalized,
            "answer_counts": [answer_count.__dict__() for answer_count in self.answer_counts]
        }

class Poll(object):
    """
        Represents a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object
    """
    question: PollMedia
    answers: List[PollAnswer]
    duration: int
    allow_multiselect: bool
    layout_type: Optional[int] = 1

    def __init__(self,
                 question: PollMedia,
                 duration: int,
                 allow_multiselect: bool,
                 layout_type: Optional[int] = 1):
        """
            Initializes the poll.

            Args:
                question (PollMedia): The media of the poll question.
                duration (int): The duration of the poll in hours.
                allow_multiselect (bool): Whether multiple answers can be selected.
                layout_type (Optional[int], optional): The layout type of the poll. Defaults to 1.

            Raises:
                ValueError: If the poll is invalid.
        """
        self.question = question
        self.answers = []
        self.duration = duration
        self.allow_multiselect = allow_multiselect
        self.layout_type = layout_type

        self.validate()

    def validate(self) -> None:
        """
            Validates the poll.

            Raises:
                ValueError: If the poll is invalid.
        """
        if not self.question.text:
            raise ValueError("Poll question must have text.")
        if len(self.question.text) > 300:
            raise ValueError("Poll question text cannot exceed 300 characters.")
        if len(self.answers) > 10:
            raise ValueError("A poll cannot have more than 10 answers.")
        if self.duration > 168:  # 7 days * 24 hours
            raise ValueError("Poll duration cannot exceed 7 days (168 hours).")
        if self.layout_type not in [1]:
            # could well be expanded to include more layout types down-the-line by Discord.
            # https://discord.com/developers/docs/resources/poll#layout-type
            raise ValueError("Poll layout type must be valid.")

    def add_answer(self, poll_media: PollMedia) -> None:
        """
            Adds an answer to the poll.

            Args:
                poll_media (PollMedia): The media of the poll answer.

            Raises:
                ValueError: If the poll is invalid.
        """
        self.answers.append(
            PollAnswer(
                poll_media=poll_media
            )
        )
        self.validate()

    def __dict__(self):
        """
            Returns the dictionary representation of the poll.

            Returns:
                dict: The dictionary representation of the poll.
        """
        return {
            "question": self.question.__dict__(),
            "answers": [answer.__dict__() for answer in self.answers],
            "duration": self.duration,
            "allow_multiselect": self.allow_multiselect,
            "layout_type": self.layout_type
        }