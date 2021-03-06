import json
from typing import Dict

from flask import current_app

from mib.events.channels import PUBLISH_CHANNEL_LOTTERY_NOTIFICATION
from mib.events.channels import PUBLISH_CHANNEL_LOTTERY_WINNERS
from mib.events.redis_setup import get_redis


class EventPublishers:
    @classmethod
    def publish_lottery_winners(cls, msg: Dict):
        if "users" not in msg:
            return None
        else:
            return get_redis(current_app).publish(
                PUBLISH_CHANNEL_LOTTERY_WINNERS, json.dumps(msg)
            )

    @classmethod
    def publish_notify_winners(cls, msg: Dict):
        if "notifications" not in msg:
            return None
        else:
            return get_redis(current_app).publish(
                PUBLISH_CHANNEL_LOTTERY_NOTIFICATION, json.dumps(msg)
            )
