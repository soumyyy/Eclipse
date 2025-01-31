# dataset_utils.py

import json
import random
import logging

# Set up logging
logger = logging.getLogger(__name__)

def loadDataset(filePath):
    """
    Load the dataset from a JSON file.
    """
    with open(filePath, 'r') as file:
        dataset = json.load(file)
    logger.info(f"Loaded dataset from {filePath}")
    return dataset

def splitDataset(dataset, trainRatio=0.8):
    """
    Split the dataset into training and testing sets.
    """
    keys = list(dataset.keys())
    random.shuffle(keys)

    splitIndex = int(len(keys) * trainRatio)
    trainData = {key: dataset[key] for key in keys[:splitIndex]}
    testData = {key: dataset[key] for key in keys[splitIndex:]}

    logger.info(f"Dataset split into {len(trainData)} training samples and {len(testData)} testing samples")
    return trainData, testData

def preprocessText(text):
    """
    Preprocess text by normalizing and cleaning.
    """
    text = text.lower().strip()
    # Add more preprocessing steps as needed
    logger.debug(f"Preprocessed text: {text}")
    return text

def augmentData(dataset, augmentFactor=1):
    """
    Augment the dataset to increase its size.
    """
    augmentedData = {}
    for key, samples in dataset.items():
        augmentedData[key] = samples.copy()
        for _ in range(augmentFactor):
            augmentedData[key].extend(samples)
    
    logger.info(f"Augmented dataset with a factor of {augmentFactor}")
    return augmentedData