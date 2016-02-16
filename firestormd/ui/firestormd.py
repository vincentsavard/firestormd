from flask import Flask, abort, jsonify

from firestorm.media.exceptions import NoMediaFoundError, NoMediaLoadedError, NoMediaPlayingError, MediaAlreadyPlayingError

from firestorm.ui.resources.mediaresource import media_blueprint
from firestorm.ui.resources.playerresource import player_blueprint

app = Flask(__name__)
app.register_blueprint(media_blueprint)
app.register_blueprint(player_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
