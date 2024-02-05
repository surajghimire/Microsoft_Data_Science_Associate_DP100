# Running the script as an experiment
# To run the script, create a ScriptRunConfig that references the folder and script file.
# You generally also need to define a Python (Conda) environment that includes any packages required by the script.
# In this example, the script uses Scikit-Learn so you must create an environment that includes that. 

# The script also uses Azure Machine Learning to log metrics, so you need to remember to include the azureml-defaults package in the environment.


from azureml.core import Experiment, ScriptRunConfig, Environment
from azureml.core.conda_dependencies import CondaDependencies

# Create a Python environment for the experiment
sklearn_env = Environment("sklearn-env")

# Ensure the required packages are installed
packages = CondaDependencies.create(conda_packages=['scikit-learn','pip'],
                                    pip_packages=['azureml-defaults'])
sklearn_env.python.conda_dependencies = packages

# Create a script config
script_config = ScriptRunConfig(source_directory='training_folder',
                                script='training.py',
                                environment=sklearn_env) 

# Submit the experiment
experiment = Experiment(workspace=ws, name='training-experiment')
run = experiment.submit(config=script_config)
run.wait_for_completion()

