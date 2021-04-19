from collections import namedtuple
from albert_bot.albert_bot import pick_human

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
