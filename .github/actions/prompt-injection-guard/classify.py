#!/usr/bin/env python3
"""
Prompt Injection Guard classifier using Llama Prompt Guard 2.

Classifies input text as BENIGN or MALICIOUS based on prompt injection
and jailbreak attack patterns.
"""

import os
import sys

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def chunk_text(text: str, tokenizer, max_tokens: int = 500) -> list[str]:
    """
    Split text into chunks that fit within the model's token limit.
    Uses 500 tokens to leave room for special tokens.
    """
    tokens = tokenizer.encode(text, add_special_tokens=False)

    if len(tokens) <= max_tokens:
        return [text]

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)

    return chunks


def classify_text(
    text: str, model, tokenizer, threshold: float
) -> tuple[str, float, bool]:
    """
    Classify text and return (classification, confidence, is_malicious).
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

    with torch.no_grad():
        logits = model(**inputs).logits

    probabilities = torch.softmax(logits, dim=-1)
    predicted_class = logits.argmax().item()
    confidence = probabilities[0][predicted_class].item()

    classification = model.config.id2label[predicted_class]
    is_malicious = classification == "MALICIOUS" and confidence >= threshold

    return classification, confidence, is_malicious


def main():
    input_text = os.environ.get("INPUT_TEXT", "")
    model_size = os.environ.get("MODEL_SIZE", "86M")
    threshold = float(os.environ.get("THRESHOLD", "0.5"))

    if not input_text.strip():
        print("No text provided, skipping classification")
        set_output("classification", "BENIGN")
        set_output("confidence", "1.0")
        set_output("is_malicious", "false")
        return

    model_name = f"meta-llama/Llama-Prompt-Guard-2-{model_size}"
    print(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    chunks = chunk_text(input_text, tokenizer)
    print(f"Processing {len(chunks)} chunk(s)")

    max_malicious_confidence = 0.0
    any_malicious = False

    for i, chunk in enumerate(chunks):
        classification, confidence, is_malicious = classify_text(
            chunk, model, tokenizer, threshold
        )
        print(f"Chunk {i + 1}: {classification} (confidence: {confidence:.4f})")

        if is_malicious:
            any_malicious = True
            max_malicious_confidence = max(max_malicious_confidence, confidence)

    final_classification = "MALICIOUS" if any_malicious else "BENIGN"
    final_confidence = max_malicious_confidence if any_malicious else confidence
    final_is_malicious = "true" if any_malicious else "false"

    print(f"\nFinal result: {final_classification} (confidence: {final_confidence:.4f})")

    set_output("classification", final_classification)
    set_output("confidence", f"{final_confidence:.4f}")
    set_output("is_malicious", final_is_malicious)


def set_output(name: str, value: str):
    """Set GitHub Actions output."""
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"{name}={value}\n")
    else:
        print(f"::set-output name={name}::{value}")


if __name__ == "__main__":
    main()
