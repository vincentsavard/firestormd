from flask import Blueprint, jsonify

from firestormd.version import VERSION

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/version", methods=["GET"])
def get_api_version():
    return jsonify({"version": VERSION})
