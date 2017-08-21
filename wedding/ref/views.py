# coding=utf-8

"""Resources module."""

from flask import Blueprint, request, jsonify
from resting.database import db
from resting.models import User
from resting.api.schemata import UserSchema


api_bp = Blueprint('api', __name__)


@api_bp.route('/users/', methods=['GET', 'POST'])
def users_view():
    if request.method == 'POST':
        # get the posted data
        raw_posted_data = request.get_json()

        # validate data
        posted_data, errors = UserSchema().load(raw_posted_data)
        if errors:
            return jsonify(errors), 422

        # define the new user
        new_user = User(**posted_data)

        # add the new database action to the session
        db.session.add(new_user)
        try:
            # commit the session to realise the actions
            db.session.commit()
        except:
            # if we encounter an integrity error, rollback
            db.session.rollback()
            # report the error with 409 - Conflict
            return jsonify({'message': 'user already exists'}), 409

        # echo the result along with 201 (sucessful creation)
        return jsonify(UserSchema().dump(new_user).data), 201

    else:
        # db query for all users
        all_users = db.session.query(User).all()

        return jsonify(UserSchema(many=True).dump(all_users).data), 200


@api_bp.route('/users/<username>', methods=['GET', 'DELETE'])
def user_view(username):
    # query all users with the matching username and get the first one
    matched_user = db.session.query(User) \
        .filter(User.username == username) \
        .first()

    # if we didn't find any user, return 404
    if not matched_user:
        return jsonify({'message': 'username not found'}), 404

    if request.method == 'GET':
        # return the matched user
        return jsonify(UserSchema().dump(matched_user).data), 200

    elif request.method == 'DELETE':
        # delete the matched user from our database
        db.session.delete(matched_user)
        # remember to commit the session
        db.session.commit()
        # normally return an empty response (i.e. 204)
        return jsonify(None), 204
