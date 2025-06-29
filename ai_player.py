import sys
sys.path.insert(0, 'C:/Users/bhupe/OneDrive/Desktop/Notebook/flappy-bird-reborn')
sys.path.insert(0, './FlappyBirdReborn')
from FlappyBirdReborn import game_core as flappy
import numpy as np
import random
import csv
from neural_network import LossHistory,neural_net
import os.path
import timeit

NUM_INPUT = 11

def play(model):

    game_state = flappy.Game()
    game_state.init_elements()

    # Do nothing to get initial.
    state,_ = game_state.frame_step(0)

    # Move.
    while True:
        
        # Choose action.
        action = (np.argmax(model.predict(np.array([state]))[0]))

        # Take action.
        state,reward = game_state.frame_step(action)
        
        if reward == -1000:
            break


if __name__ == "__main__":
    saved_model = 'results/saved-models/256-256-512-50000-ver19-100000.weights.h5'
    model = neural_net(NUM_INPUT, [256, 256], saved_model)
    play(model)
