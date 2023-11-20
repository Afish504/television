import pytest
from television import Television

class Test:
    def setup_method(self):
        self.tvl = Television()

    def teardown_method(self):
        del self.tvl

    def test_init(self):
        assert self.tvl.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tvl.power()
        assert self.tvl.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tvl.power()
        assert self.tvl.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tvl.power()
        self.tvl.mute()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 0"

        self.tvl.mute()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 0"

    def test_chanel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.channel_down()
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.power()
        self.tvl.channel_down()
        assert str(self.tvl) == "Power = True, Channel = 3, Volume = 0"

        for _ in range(4):  # Simulating channel down beyond the minimum channels
            self.tvl.channel_down()
        assert str(self.tvl) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.volume_up()
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.power()
        self.tvl.volume_up()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 1"

        for _ in range(3):  # Simulating volume up beyond the maximum volume
            self.tvl.volume_up()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.volume_down()
        assert str(self.tvl) == "Power = False, Channel = 0, Volume = 0"

        self.tvl.power()
        self.tvl.volume_down()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 0"

        self.tvl.volume_up()
        self.tvl.volume_down()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 0"

        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 1"

        self.tvl.mute()
        self.tvl.volume_down()
        assert str(self.tvl) == "Power = True, Channel = 0, Volume = 0"