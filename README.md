# <div align="center">Quantum Minigolf</div>

<div align="center"><i>A Unique Simulation Blending Minigolf with Quantum Physics Principles.</i></div>

***

## Table of Contents

- [Quantum Game](#quantum-game)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Customization](#customization)
  - [Compiling](#compiling)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

Quantum Minigolf reinvents the traditional game of minigolf by incorporating quantum mechanics principles, featuring a golf ball with quantum behavior distinct from classical physics. Developed through sophisticated Python programming, this project serves as a simulation to demonstrate an in-depth understanding of quantum phenomena. It exemplifies the application of complex quantum concepts in a familiar setting, providing an engaging and educational tool for exploring the fundamentals of quantum mechanics.

## Customization

> NOTE: This is a **work in progress** meaning it is not yet complete and may not provide the most accurate information.

If you want to customize styling, speed, etc, feel free to change the parameters in the `style.json` file. For information on each of these parameters, see the table below:

| Parameter | Description |
| --- | --- |
| `scale` | The size of the screen (scale value) - Note that it multiplies the values under `defaults` |
| `resolution` | The resolution of the game itself, the higher the value, the slower the game |
| `duration` | The amount of frames until it checks if the ball is in the goal |
| `colors` | The colors of the game (Obstacle is typical RGB values, whereas the ballHeatmap RGB values can only be either 1 or 0 as they are the multiplier values) |
| `obstaclePresets` | Presets/obstacles you can initially choose from |
| `defaults` | The default values for the game (Recommended not to change) |

## Compiling

To compile the program into an executable, we used [PyInstaller](https://pyinstaller.org/en/stable/). We have actually created a `.spec` file for those of you who wish to compile it yourselves.

The following is a step-by-step guide if you wish to compile it youself:
1. Install PyInstaller with `pip install PyInstaller`
2. Run PyInstaller with `PyInstaller QuantumMinigolf.spec` *Note that capitalization is very important*
3. After running, the executable should be locatable in the `build` folder.

## Contributing

If you want to cont.ribute to this project, please follow the guidelines below:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push the new branch to your fork
5. Submit a pull request

## License

This project is licensed under the *MIT* license. See our [LICENSE](LICENSE) for more information.

We are grateful for the support of our community and for the contributions of everyone who has helped make this project what it is.

## Acknowledgments

We would like to thank the following people and organizations for their support and contributions to this project:

- [Valentina Banner](https://realhuman101.github.io/) for contributing code for the game logic and the game UI, and helping co-create the presentation.
- [Madelyn Lee](https://github.com/madness118/) for contributing code for the game logic and the game UI, and helping co-create the presentation.
- [Annie Qin](https://github.com/annieqqa/) for contributing code for the mathematics the game relies on, and helping co-create the presentation.
- [HKUST](https://hkust.edu.hk/) for providing not only the opportunity to create this project, but the opportunity to present it.

We are grateful for the support of our community and for the contributions of everyone who has helped make this project what it is.

