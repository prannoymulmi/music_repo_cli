from unittest import mock
from unittest.mock import MagicMock

from typer.testing import CliRunner

from main import app
from src.utils.configLoader import ConfigLoader


# @mock.patch("src.main.ConfigLoader.load_config")
# def test_list_music_data(
#         mock__ConfigLoader__load_config
# ):
#     mock__ConfigLoader__load_config.return_value = None
#     runner = CliRunner()
#     result = runner.invoke(cli, ['list-music-data'])
#     assert 'listing' in result.output

def side_effect(arg):
    test = MagicMock(ConfigLoader())
    test.load_config.return_value = "YOL"
    values = {'config_loader': test, 'b': 2, 'c': 3}
    return values[arg]

@mock.patch("src.main.ConfigFactory.create_object")
def test_when_list_music_data_then_is_listed(
        mock__creator
):
    test = MagicMock(ConfigLoader())

    test.load_config.return_value = "YOL"
    mock__creator.side_effect = side_effect
    runner = CliRunner()
    result = runner.invoke(app, ['list-music-data'])
    assert 'Listing' in result.output

# @mock.patch("src.main.ConfigFactory.create_object")
def test_when_login_with_right_credentials_then_user_is_logged_on(

):
    # test = MagicMock(ConfigLoader())
    #
    # test.load_config.return_value = "YOL"
    # mock__creator.side_effect = side_effect
    runner = CliRunner()
    result = runner.invoke(app, ['login'], input="hello\nworld")
    assert 'login' in result.output


@mock.patch("src.main.ConfigFactory.create_object")
def test_when_delete_music_data_with_right_credentials_then_music_data_is_deleted(
        mock__creator
):
    test = MagicMock(ConfigLoader())

    test.load_config.return_value = "YOL"
    mock__creator.side_effect = side_effect
    runner = CliRunner()
    result = runner.invoke(app, ['delete-music-data'])
    assert 'deleting' in result.output