"""
==============================================================
VisionGuard AI - Main Application Entry Point
==============================================================
File    : app.py
Purpose : Boots the Flask server, registers all route blueprints,
          initialises the database, and configures logging.
Phase   : 1 - Project Initialisation (no AI logic yet)
==============================================================
"""

import os
from flask import Flask
from flask_cors import CORS

# ── Internal imports ───────────────────────────────────────────
from backend.routes.dashboard  import dashboard_bp
from backend.routes.detection  import detection_bp
from backend.routes.api        import api_bp
from backend.database.db       import init_db
from backend.utils.logger      import setup_logger
from config.settings           import Config


def create_app(config: object = Config) -> Flask:
    """
    Application factory pattern.
    Creates and fully configures the Flask application instance.

    Args:
        config: Configuration class (default: Config from config/settings.py)

    Returns:
        Configured Flask app ready to run.
    """

    # ── 1. Create Flask app instance ───────────────────────────
    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static",
    )

    # ── 2. Load configuration ──────────────────────────────────
    app.config.from_object(config)

    # ── 3. Enable CORS (allows JS fetch from browser) ──────────
    CORS(app)

    # ── 4. Set up logging ──────────────────────────────────────
    logger = setup_logger("visionguard")
    logger.info("VisionGuard AI starting up...")

    # ── 5. Initialise SQLite database ──────────────────────────
    init_db(app)
    logger.info("Database initialised.")

    # ── 6. Register blueprints (route groups) ──────────────────
    app.register_blueprint(dashboard_bp)   # /  and /dashboard
    app.register_blueprint(detection_bp)   # /detections/*
    app.register_blueprint(api_bp)         # /api/*

    logger.info("All blueprints registered.")

    return app


# ── Run directly (development mode) ───────────────────────────
if __name__ == "__main__":
    app = create_app()

    print("\n" + "=" * 60)
    print("  🚦 VisionGuard AI  –  Traffic Enforcement Platform")
    print("  Phase 1: Project Structure Initialised")
    print("  Running at: http://127.0.0.1:5000")
    print("=" * 60 + "\n")

    app.run(
        host=app.config.get("HOST", "127.0.0.1"),
        port=app.config.get("PORT", 5000),
        debug=app.config.get("DEBUG", True),
        threaded=True,          # Handle concurrent requests
        use_reloader=True,      # Auto-reload on code changes
    )
