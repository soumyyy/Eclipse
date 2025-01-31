# model_utils.py

import torch
from transformers import BertForSequenceClassification, BertTokenizer
import logging

# Set up logging
logger = logging.getLogger(__name__)

def loadModel(modelPath, device='cpu'):
    """
    Load a pre-trained BERT model for sequence classification.
    """
    model = BertForSequenceClassification.from_pretrained(modelPath)
    model.to(device)
    logger.info(f"Model loaded from {modelPath} to {device}")
    return model

def loadTokenizer(modelPath):
    """
    Load a tokenizer for the BERT model.
    """
    tokenizer = BertTokenizer.from_pretrained(modelPath)
    logger.info(f"Tokenizer loaded from {modelPath}")
    return tokenizer

def saveModel(model, outputPath):
    """
    Save the model to a specified path.
    """
    model.save_pretrained(outputPath)
    logger.info(f"Model saved to {outputPath}")

def evaluateModel(model, tokenizer, dataset, device='cpu'):
    """
    Evaluate the model on the given dataset.
    """
    model.eval()
    correct = 0
    total = 0

    for intent, samples in dataset.items():
        for text in samples:
            inputs = tokenizer(text, return_tensors='pt').to(device)
            outputs = model(**inputs)
            predictedLabel = torch.argmax(outputs.logits, dim=1).item()

            if predictedLabel == intent:  # Assuming intent is numeric label
                correct += 1
            total += 1

    accuracy = correct / total
    logger.info(f"Model accuracy: {accuracy:.2%}")
    return accuracy