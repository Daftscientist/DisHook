from DisHook import Webhook, Poll, PartialEmoji, PollMedia, PollAnswer

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("A poll is attached!")

my_poll = Poll(
    question=PollMedia("What is your favorite color?"),
    duration=3,
    allow_multiselect=False,
)

my_poll.add_answer(PollMedia("Red", PartialEmoji(name="🟥")))
my_poll.add_answer(PollMedia("Green", PartialEmoji(name="🟩")))
my_poll.add_answer(PollMedia("Blue", PartialEmoji(name="🟦")))
my_poll.add_answer(PollMedia("Yellow", PartialEmoji(name="🟨")))
my_poll.add_answer(PollMedia("Other", PartialEmoji(name="❓")))
my_poll.add_answer(PollMedia("I don't know", PartialEmoji(name="🤷")))

webhook.add_poll(my_poll)

webhook.send()