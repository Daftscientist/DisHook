from typing import List, Optional
from .emoji import PollMediaPartialEmoji
from dataclasses import dataclass

@dataclass
class PollMedia:
    """
        Represents the media of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object-poll-media

        Args:
            text (str): The text of the poll media.
            emoji (Optional[PollMediaPartialEmoji], optional): The emoji of the poll media. Defaults to None.
    """
    text: str
    emoji: Optional[PollMediaPartialEmoji]
    
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

@dataclass
class PollAnswer:
    """
        Represents an possible answer to a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object-poll-answer

        Args:
            answer_id (Optional[int], optional): The ID of the answer. Defaults to None.
            poll_media (Optional[PollMedia], optional): The media of the poll answer. Defaults to None.
    """
    answer_id: Optional[int] = None
    poll_media: Optional[PollMedia] = None
    
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

@dataclass
class PollResultsAnswerCount:
    """
        Represents the answer count of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-results-object-poll-results-answer-count

        Args:
            answer_id (int): The ID of the answer.
            count (int): The count of the answer.
            me_voted (bool): Whether the user voted for the answer.
    """
    answer_id: int
    count: int
    me_voted: bool
    
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

@dataclass
class PollResults:
    """
        Represents the results of a poll.
        - https://discord.com/developers/docs/resources/poll#poll-results-object

        Args:
            is_finalized (bool): Whether the poll is finalized.
            answer_counts (List[PollResultsAnswerCount]): The answer counts of the poll.
    """
    is_finalized: bool
    answer_counts: List[PollResultsAnswerCount]
    
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

@dataclass
class Poll:
    """
        Represents a poll.
        - https://discord.com/developers/docs/resources/poll#poll-create-request-object

        Args:
            question (PollMedia): The media of the poll question.
            answers (List[PollAnswer]): The answers of the poll.
            duration (int): The duration of the poll.
            allow_multiselect (bool): Whether the poll allows multiple selections.
            layout_type (Optional[int], optional): The layout type of the poll. Defaults to 1.
    """
    question: PollMedia
    answers: List[PollAnswer]
    duration: int
    allow_multiselect: bool
    layout_type: Optional[int] = 1

    def __post_init__(self):
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
