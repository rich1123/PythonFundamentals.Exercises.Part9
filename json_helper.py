import json
import os
import pickle
from typing import Dict


def read_json(path: str) -> Dict:
    file_name = path
    with open(file_name) as f:
        data: json = json.load(f)
    return data


def read_all_json_files(path: str):
    all_dicts = []
    for full_file in os.listdir(path):
        if full_file.endswith('.json'):
            # full_filename = os.path.join(path, path, full_file)
            full_filename = os.path.join(path, full_file)
            with open(full_filename, 'r') as fi:
                dictionary = json.loads(fi)
                all_dicts.append(dictionary)
        return all_dicts


def write_pickle(path, data):
    outfile = open(path, 'wb')
    pickle.dump(data, outfile, protocol=1)
    outfile.close()


def load_pickle(file: str):
    with open(file, 'rb') as f:
        x: dict = pickle.load(f)
    print(x)



read_json('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')

read_all_json_files('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
#
write_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle', {
    "name": "Link",
    "neutral_special": "Bow and Arrows",
    "side_special": " Boomerang",
    "up_special": " Spin Attack",
    "down_special": "Remote Bomb",
    "final_smash": "Ancient Bow and Arrow"
})

load_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle')


# """Exercise 2 Marvel"""
# #
# read_json('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/dragon_ball_z.json')
#
# read_all_json_files('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/')
# #
# write_pickle(
#     '/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/dragon_ball.pickle',
#     '/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/dragon_ball_z.json')
#
# load_pickle(
#     '/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/dragon_ball.pickle')


# """Exercise 2 Marvel"""
#
#
# read_json('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')
#
# read_all_json_files('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
#
# write_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle',
#
# load_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle')
