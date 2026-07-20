# Project Structure: Space Invaders

This project is a Space Invaders game implemented in Python using the Turtle graphics library. The structure is organized to separate core configuration, domain models, and assets.

```text
.
├── pyproject.toml            # Project metadata and dependencies
├── src/
│   └── app/
│       ├── assets/           # Game assets (images, piskel files)
│       │   ├── alien1.png
│       │   ├── alien2.png
│       │   ├── grenade.png
│       │   ├── gun.png
│       │   ├── missile.png
│       │   ├── Mountain-1.png.png
│       │   ├── piskel/
│       │   └── saucer1.png
│       ├── core/             # Global configuration and constants
│       │   └── config.py
│       ├── main.py           # Application entry point
│       └── models/           # Game logic and entities
│           └── domain/
│               ├── alien.py
│               ├── alien_tile.py
│               ├── bullet.py
│               ├── button.py
│               └── gun.py
```
the new project must use uv
uv run src/app/main.py to run the main application
