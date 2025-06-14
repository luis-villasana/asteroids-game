# Asteroids Game 🚀

A classic-style **Asteroids** game built with **Python** and **Pygame**, created to practice and demonstrate **Object-Oriented Programming (OOP)** fundamentals in a fun, interactive project.

---

## 🎮 Features

- **Player-controlled spaceship** with rotation, thrust, and shooting
- **Asteroid field** with large rocks that split into smaller ones when hit
- **Scoring system** for destroying asteroids
- **Game Over screen** with restart functionality
- **Sound effects** for shooting and explosions (courtesy of [Kenney.nl](https://kenney.nl))
- Clean, modular structure using `pygame.sprite.Group` and custom classes

---

## 📁 Project Structure

```
.
├── assets/
│   └── sounds/
│       ├── explosionCrunch_000.ogg
│       └── laserSmall_000.ogg
├── asteroid.py
├── asteroidfield.py
├── circleshape.py
├── constants.py
├── game.py          # Main game loop and core logic lives here
├── main.py          # Entry point
├── player.py
├── requirements.txt
├── shot.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Run the Game

```bash
python main.py
```

Use the arrow keys to move:
- **← / →**: Rotate
- **↑**: Thrust
- **Spacebar**: Shoot

Destroy all the asteroids! If you get hit, press any key to restart.

---

## 🔊 Sound Assets

Sound effects (`laserSmall_000.ogg`, `explosionCrunch_000.ogg`) come from [Kenney.nl's Sci-fi Sounds Pack](https://kenney.nl/assets/sci-fi-sounds), which is licensed **CC0 (public domain)**

---

## 🧠 Learning Goals

This project was created to practice:

- Object-Oriented Programming (OOP)
- Sprite-based architecture with `pygame.sprite.Group`
- Collision detection
- Game loop architecture
- Timers and cooldown mechanics
- Modular code and abstraction

---

## ✅ To Do / Ideas for Improvement

- Add levels or wave progression
- Add particle effects for destruction
- Implement lives and health bar
- Add a title screen
- High score tracking (file or local storage)

---