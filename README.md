# Rubiks Fresco Maker

Rubiks Fresco Maker is a little appplication who is made and used by the team 6 of Algosup students to split their fresco and give instruction manual to each others teams

## Installation


## Initilization

If you want to use it you need to build the app to do that open your terminal and execute:

```bash
python setup.py build
```

[cx_freeze](https://cx-freeze.readthedocs.io/en/stable/) will build your executable app to run

## Usage

To use it you just need to run the executable file, when the GUI appears you need to put the path of your fresco with valid proportion.

Choose the number of teams to split the fresco in equal parts for each team

Accept the documentation generation

And let's run !


## How does it work ?

This will be done in the following 5 steps:

1. Fresco Picutre splitting in equal part among the teams
2. Split the team cutted image in images of 3x3 pixels
3. Get each 3x3 image and get colors for each pixel
4. Generate the list of all movements to solve the cube
5. Generate a pdf for each team with a detailed manual to create all rubiks face


## License

[MIT](https://choosealicense.com/licenses/mit/)