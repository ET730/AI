from envs.obsgrid_env import ObsGrid


class RoadEnv(ObsGrid):

    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
            ["S", "R", "W", "W", "W", "W", "R", "W", "W"],
            ["W", "Ts", "R", "R", "R", "R", "Tl", "R", "R"],
            ["W", "R", "W", "W", "W", "W", "R", "W", "W"],
            ["R", "Ts", "R", "Ts", "R", "R", "Ts", "W", "W"],
            ["W", "W", "W", "R", "W", "W", "R", "Ts", "R"],
            ["W", "R", "R", "Tl", "W", "W", "W", "R", "W"],
            ["W", "R", "W", "R", "Ts", "R", "R", "Tl", "R"],
            ["W", "R", "W", "W", "R", "W", "W", "R", "W"],
            ["R", "Ts", "R", "R", "Tl", "R", "G", "Ts", "R"],
        ]
        rewards = {"R": -0.04, "S": -0.04, "Tl": -0.04, "Ts": -0.04, "G": 5}
        actdyn = {0: {0: 1}, 1: {1: 1}, 2: {2: 1}, 3: {3: 1}}
        super().__init__(actions, grid, actdyn, rewards)

