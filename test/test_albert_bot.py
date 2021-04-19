import pytest

from collections import namedtuple
from albert_bot.albert_bot import pick_human, Countdown

Member = namedtuple("Member", ['name', 'bot'])

def test_pick_someone_between_humans() -> None:
    members = [Member("albert", False), Member("josé", False)]

    picked = pick_human(members)

    assert not picked.bot
    assert picked in members


def test_pick_any_between_bots() -> None:
    members = [Member("r2d2", True), Member("hal9000", True)]

    picked = pick_human(members)

    assert picked is None

@pytest.mark.asyncio
async def test_countdown_finished() -> None:
    countdown = Countdown(1)
    await countdown.start()
    assert countdown.finished

def test_countdown_not_started() -> None:
    countdown = Countdown(1)
    assert not countdown.finished
