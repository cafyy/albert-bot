from albert_bot.albert_bot import AlbertBot


def test_bot_instantiate() -> None:
    albert = AlbertBot()
    assert albert.on_ready() == 'Logged as albert-bot!'
