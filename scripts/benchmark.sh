#!/bin/bash

cd ..

python benchmark.py --task l --ps zs-l --model gpt-4-turbo-2024-04-09  --mp 40

python benchmark.py --task s  --model gpt-4-turbo-2024-04-09  --mp 40