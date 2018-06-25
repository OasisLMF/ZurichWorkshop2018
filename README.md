<img src="https://oasislmf.org/packages/oasis_theme_package/themes/oasis_theme/assets/src/oasis-lmf-colour.png" alt="Oasis LMF logo" width="250"/>

# ZurichWorkshop2018
Workshop material for Zurich Oasis conference 2018.

## Cloning the repository

You can clone this repository from <a href="https://github.com/OasisLMF/OasisPiWind" target="_blank">GitHub</a> using HTTPS or SSH. Before doing this you must generate an SSH key pair on your local machine and add the public key of that pair to your GitHub account (use the GitHub guide at <a href="https://help.github.com/articles/connecting-to-github-with-ssh/" target="_blank">https://help.github.com/articles/connecting-to-github-with-ssh/</a>). To clone over SSH use

    git clone --recursive git+ssh://git@github.com/OasisLMF/OasisPiWind

To clone over HTTPS use

    git clone --recursive https://<GitHub user name:GitHub password>@github.com/OasisLMF/OasisPiWind

## Setting up the environment

We recommend using a Python virtual environment for running the excercises. To set up the your virtual environment, run the following commands in the project root directory:

   virtualenv -p /usr/bin/python3.6 venv3.6
   source venv3.6/bin/activate
   pip install -r requirements.txt
   # The next command will make a kernel named "ZurichWorkshop2018" available in Jupyter.
   pip install ipykernel
   ipython kernel install --user --name=ZurichWorkshop2018

## Running the excercises



## Documentation
# Oasis
* <a href="https://oasislmf.github.io">General Oasis documentation</a>
* <a href="http://localhost:8000/html/docs/oasis_cli.html">Model Development Kit (MDK)</a>
* <a href="https://oasislmf.github.io/docs/oasis_mdk.html">Modules</a>
# Other reference material
* <a href="http://jupyter.org/">Jupyter project</a>
* <a href="https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261">Interactive notebooks - sharing the code (Nature article)</>
* <a href="http://docker.com/">Docker project</a>

## License
The code in this project is licensed under BSD 3-clause license.
