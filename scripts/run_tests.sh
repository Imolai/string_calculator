#!/bin/bash
export PYTHONPATH=$(pwd)
python -m coverage run -m unittest discover -s tests
python -m coverage combine
python -m coverage report
python -m coverage html