
from flask.json import jsonify
from mib.dao.lottery_manager import LotteryManager
from flask import request
from mib.utils import next_lottery_date

def get_next_lottery():
    participants = LotteryManager.get_participants()
    date = next_lottery_date()
    return jsonify({
        "date":date.strftime("%d/%m/%Y"),
        "participants":[p.serialize() for p in participants]
    }), 200

def participate():
    data = request.json
    l =  LotteryManager.add_participant(data["email"],data["choice"])
    if l:
        return jsonify({
                "status": "success",
                "message":"Participant successfully added"
            }), 201
    else:
        return jsonify({
                "status": "failure",
                "message":"A participant with the given email already exists"
            }), 200
