"""
minigridをテストするファイルです
python3 -m pip install minigrid
pip install gymnasium==0.29.0
"""

import gymnasium as gym

# 登録されている環境の一覧を取得
envs = [env_spec.id for env_spec in gym.envs.registry.values()]

# 環境名を出力
print("登録されている環境:")
for env in envs:
    print(env)

env = gym.make("MiniGrid-Empty-5x5-v0", render_mode="human")