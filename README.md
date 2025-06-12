# 🐦 Flappy-Bird-Reborn: Deep Reinforcement Learning Agent

Welcome to **Flappy-Bird-Reborn**, a modified version of the classic Flappy Bird game, enhanced with an **AI agent** trained using **Deep Q-Learning** (DQN). This project demonstrates how reinforcement learning can be used to teach an agent to play games through experience.

---

## 🎯 Project Objectives

- Build a fully functional Flappy Bird clone
- Train a neural network using **Deep Q-Learning (DQN)**
- Use **experience replay**, **reward shaping**, and **Q-value approximation**
- Play the game autonomously with a trained agent

---

## 🧠 AI Concepts Used

- **Reinforcement Learning (RL)**
- **Markov Decision Process (MDP)**
- **Q-Learning** and **Bellman Equation**
- **Neural Network Q-function approximation**
- **Experience Replay**
- Reward: `+1` for staying alive, `-1000` for crashing

---

## 📁 Folder Structure

```
flappy-bird-reborn/
│
├── FlappyBirdReborn/           # Game environment
│   ├── assets/                 # Game images & sounds
│   └── game_core.py           # Game logic (states, rewards, actions)
│
├── ai_training.py             # Train the agent with DQN
├── ai_player.py               # Play with a trained model
├── neural_network.py          # Keras model architecture
│
├── results/                   # Saved models & loss logs
│   ├── saved-models/
│   └── sonar-frames/
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🏁 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bhupeshk3014/flappy-bird-reborn.git
cd flappy-bird-reborn
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the AI Agent
```bash
python ai_training.py
```
This will:
- Train for 100,000 frames
- Save models every 5000 frames to `results/saved-models/`
- Log loss data to `results/sonar-frames/`

### 4️⃣ Run the Trained Agent
```bash
python ai_player.py
```
Make sure the weight file path in `ai_player.py` matches your saved model path.

---

## 🧪 Neural Network Architecture

- **Input:** 11 sensor values
- **Hidden Layers:** 2 layers with 256 neurons each (ReLU + Dropout)
- **Output:** 2 Q-values for the actions: [flap, no-flap]
- **Loss Function:** Mean Squared Error (MSE)
- **Optimizer:** RMSprop

---

## 📊 Training Features

- **Replay Buffer:** Stores (state, action, reward, next_state) tuples
- **Mini-batch Training:** Randomly samples past experiences
- **Model Saving:** Saves weights every 5000 frames
- **Loss Logging:** Saves training loss per batch to CSV

---

## 🔍 Key Files

| File | Description |
|------|-------------|
| `neural_network.py` | Builds and compiles the neural net model |
| `ai_training.py` | Trains the AI using Deep Q-Learning |
| `ai_player.py` | Loads a trained model to play Flappy Bird |
| `game_core.py` | Manages the Flappy Bird game state and actions |

---

## 🖼️ Demo Screenshots

![AI Playing Flappy Bird](images/flappy-ai-demo.gif)

---

## 🚀 Future Enhancements

- Add **epsilon-greedy exploration** during training
- Use **Target Networks** for more stable learning
- Add **Double DQN** or **Dueling DQN**
- Include **TensorBoard** for better visualizations
- Add evaluation metrics and a random-baseline comparison

---

## 🤝 Contributors

- **Bhupesh Kumar**  
  GitHub: [@bhupeshk3014](https://github.com/bhupeshk3014)

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more information.
