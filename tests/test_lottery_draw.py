import mock
import pytest

from mib import db
from mib.background import _lottery_draw
from mib.models.lottery_participant import LotteryParticipant


class TestLotteryDraw:
    @pytest.mark.parametrize("draw", [15, 45])
    def test_lottery_draw(self, draw):
        p1 = LotteryParticipant(participant_id=1, choice=2)
        p2 = LotteryParticipant(participant_id=2, choice=15)
        p3 = LotteryParticipant(participant_id=3, choice=50)
        db.session.add_all([p1, p2, p3])
        db.session.commit()
        with mock.patch("random.randint") as m:
            m.return_value = draw
            _lottery_draw()
            assert len(db.session.query(LotteryParticipant).all()) == 0
