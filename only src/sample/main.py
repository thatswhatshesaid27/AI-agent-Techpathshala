#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from sample.crew import Sample

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': ['Microservices','Load Balancing',
                'Event-Driven Architectur',
                'Database Sharding',
                'API Gateway',
                'Containerization'
                'Serverless Computing',
                'Horizontal Scaling',
                'Message Queues',
                'Distributed Systems'],
        'preffered_audience': 'graduate'
    }
    
    try:
        Sample().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': ['Microservices','Load Balancing',
                'Event-Driven Architectur',
                'Database Sharding',
                'API Gateway',
                'Containerization'
                'Serverless Computing',
                'Horizontal Scaling',
                'Message Queues',
                'Distributed Systems'],
        'preffered_audience': 'graduate'
    }
    try:
        Sample().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Sample().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': ['Microservices','Load Balancing',
                'Event-Driven Architectur',
                'Database Sharding',
                'API Gateway',
                'Containerization'
                'Serverless Computing',
                'Horizontal Scaling',
                'Message Queues',
                'Distributed Systems'],
        'preffered_audience': 'graduate'
    }
    try:
        Sample().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
