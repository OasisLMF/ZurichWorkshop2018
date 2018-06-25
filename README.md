<img src="https://oasislmf.org/packages/oasis_theme_package/themes/oasis_theme/assets/src/oasis-lmf-colour.png" alt="Oasis LMF logo" width="250"/>

# ZurichWorkshop2018
Workshop material for Zurich Oasis conference 2018.

## Setting up the environment

We recommend using a Python virtual environment for running the excercises. To set up the your virtual environment, run the following commands in the project root directory:

   virtualenv -p /usr/bin/python3.6 venv3.6
   source venv3.6/bin/activate
   pip install -r requirements.txt
   pip install ipykernel
   ipython kernel install --user --name=ZurichWorkshop2018

## Exercises

#### Running the exercises
The exercises are provided as interactive Jupyter notebooks. Jupyter is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. To install Jupyter, run the following commands:

   python -m pip install --upgrade pip
   python -m pip install jupyter

To launch Jupyter, run the following command which will start Jupyter and open the home page in a browser window. You can then navigate to the relevant workbook.

   jupyter notebook

#### Excercise 1: Introduction to the Oasis Model Development Kit (MDK).
#### Excercise 2: Introduction to Oasis model files and formats.
#### Excercise 3: Using code to adjust a model.
#### Excercise 4: Deploying a model to the Oasis platform.

## Documentation
### Oasis
* <a href="https://oasislmf.github.io">General Oasis documentation</a>
* <a href="http://localhost:8000/html/docs/oasis_cli.html">Model Development Kit (MDK)</a>
* <a href="https://oasislmf.github.io/docs/oasis_mdk.html">Modules</a>
### Other reference material
* <a href="http://jupyter.org/">Jupyter project</a>
* <a href="https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261">Interactive notebooks - sharing the code (Nature article)</a>
* <a href="http://docker.com/">Docker project</a>

## License
The code in this project is licensed under BSD 3-clause license.
