# Fresco Maker

Fresco Maker is a little software who is made and used by the team 6 of ALGOSUP students to split their fresco and give instruction manual to each others teams

We created this program with [Python 3.11.6](docs.python.org/3.11/)

## Installation

Do a gitclone and start the Initialization

#### Libraries Required :

- [tkinter](https://tkdocs.com/tutorial/index.html)
- [reportlab](https://docs.reportlab.com/reportlab/userguide/ch5_platypus/)
- [Pillow](https://pypi.org/project/Pillow/)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [matplotlib](https://matplotlib.org/stable/index.html)
- [mpl_toolkits](https://matplotlib.org/1.3.0/mpl_toolkits/index.html)

## Initilization

If you want to use it you need to build the app to do that open your terminal and execute:

```bash
python setup.py build
```

[cx_freeze](https://cx-freeze.readthedocs.io/en/stable/) will build your executable app to run

## Usage

- To use it you just need to run the executable file, when the GUI appears you need to put the path of your fresco image with valid proportion.

- Choose the number of teams to split the fresco in equal parts for each team

- Accept the documentation generation

- And let's run !


## How does it work ?

This will be done in the following 5 steps:

1. Fresco Picture splitting in equal part among the teams
2. Split the team cut image in images of 3x3 pixels
3. Get each 3x3 image and get colors for each pixel
4. Generate the list of all movements to solve the cube
5. Generate a pdf for each team with a detailed manual to create all rubiks face

Now Follow the documentation and realize your fresco !


## License

[MIT](./LICENSE)