from flask import Blueprint, abort, jsonify

from firestormd.ui.services import media_service
from firestormd.media.exceptions import NoMediaFoundError, NoMediaLoadedError, NoMediaPlayingError, MediaAlreadyPlayingError

player_blueprint = Blueprint("player", __name__, url_prefix="/api/player")

@player_blueprint.route("/load/<int:media_id>", methods=["POST"])
def load_media(media_id):
    try:
        media_service.load_media_by_id(media_id)
        return jsonify({"status": "ok"})
    except NoMediaFoundError:
        abort(404)

@player_blueprint.route("/play", methods=["POST"])
def play_media():
    try:
        media_service.play_loaded_media()
        return jsonify({"status": "ok"})
    except NoMediaFoundError:
        abort(404)
    except NoMediaLoadedError:
        abort(400)
    except MediaAlreadyPlayingError:
        abort(400)

@player_blueprint.route("/pause", methods=["POST"])
def pause_current_media():
    try:
        media_service.pause_loaded_media()
        return jsonify({"status": "ok"})
    except NoMediaLoadedError:
        abort(400)
    except NoMediaPlayingError:
        abort(400)

@player_blueprint.route("/stop", methods=["POST"])
def stop_current_media():
    try:
        media_service.stop_loaded_media()
        return jsonify({"status": "ok"})
    except NoMediaLoadedError:
        abort(400)
