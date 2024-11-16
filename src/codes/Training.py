#!/usr/bin/env python3
"""
Script to train a Keras model using TensorFlow for DonkeyCar.
This script facilitates the training process for autonomous driving models, 
allowing users to specify their data directory (tubs), model output path, 
and additional parameters for model configuration.

Basic usage: 
    train.py --tubs data/ --model models/mypilot.h5

Usage:
    train.py [--tubs=tubs] (--model=<model>)
    [--type=(linear|inferred|tensorrt_linear|tflite_linear)]
    [--comment=<comment>]

Options:
    -h --help              Show this screen.
"""

from docopt import docopt  # For parsing command-line arguments
import donkeycar as dk  # DonkeyCar framework for autonomous car project
from donkeycar.pipeline.training import train  # Import the training function from the pipeline

def main():
    """
    Main entry point for the script.
    - Parses command-line arguments using docopt.
    - Loads the DonkeyCar configuration.
    - Calls the training function with the specified arguments.
    """
    args = docopt(__doc__)  # Parse the command-line arguments based on the docstring
    cfg = dk.load_config()  # Load the DonkeyCar configuration (e.g., model, hyperparameters)
    
    # Retrieve input arguments for the training process:
    tubs = args['--tubs']  # Path to the training data (tub) directories
    model = args['--model']  # Path to the model file (e.g., where the trained model will be saved)
    model_type = args['--type']  # Type of model to train (e.g., 'linear', 'inferred')
    comment = args['--comment']  # Optional comment for the training run

    # Call the training function from DonkeyCar's pipeline with the parsed arguments
    train(cfg, tubs, model, model_type, comment)

if __name__ == "__main__":
    """
    Script entry point.
    If this file is executed directly (not imported), the `main()` function will run.
    """
    main()
