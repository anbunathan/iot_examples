import gym
from time import sleep
from IPython.display import clear_output
# Creating thr env
env = gym.make("Taxi-v2").env
from os import system, name



env.s = 328

# Setting the number of iterations, penalties and reward to zero,
epochs = 0
penalties, reward = 0, 0

frames = []

done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1

    # Put each rendered frame into the dictionary for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
    }
    )

    epochs += 1

print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))


# Printing all the possible actions, states, rewards.
def framesfunc(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        sleep(0.2)
        print(frame['frame'].getvalue())
        print("Timestep: ", {i + 1})
        print("State: ",{frame['state']})
        print("Action: ",{frame['action']})
        print("Reward: ",{frame['reward']})
        sleep(.1)


framesfunc(frames)


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')