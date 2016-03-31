from flask import Blueprint, abort, jsonify

from firestormd.ui.services import media_service
from firestormd.media.exceptions import NoMediaFoundError

media_blueprint = Blueprint("media", __name__, url_prefix="/api/media")


@media_blueprint.route("/", methods=["GET"])
def get_all_medias():
    return jsonify({"medias": [media.to_dict() for media in media_service.get_all_medias()]})


@media_blueprint.route("/update", methods=["POST"])
def update_medias():
    media_service.update()
    return jsonify({"status": "ok"})


@media_blueprint.route("/<int:media_id>", methods=["GET"])
def get_media(media_id):
    try:
        media = media_service.get_by_id(media_id)
        return jsonify(media.to_dict())
    except NoMediaFoundError:
        abort(404)
