# Prey-Predator Simulation

## Overview

This is a simple prey-predator simulation implemented in Python using the Pygame library. The simulation involves entities representing prey and predators interacting within a defined environment.

## Features

- **Entities:** The simulation includes two types of entities - prey and predators.
  
- **Movement:** Entities move within the simulation space based on predefined rules and randomly, and interact with eachothers in a specific range.

- **Interactions:** Predators can interact with prey entities, and Preys can interact with trees. Specific behaviors, such as catching prey, are simulated.

- **Delay Mechanism:** The code includes a delay mechanism to control the frequency of specific actions, preventing entities from moving or interacting too frequently.
  
| Action   |  Delay |
|---       |---     |
|  Move    |   	1s  |   
|   Reproduce (If mate in range)	   |   20s  |
|   	Energy Loss    | 1 bar every 1s   | 
|  Energy Gain 	 |  3 bars on eating 	  |
| Regenerate Trees| 10s |

![earfh](https://github.com/FadlGh/Earfh/assets/97055147/db8852c6-3aa6-4e90-858a-2d9c7d7ff321)

