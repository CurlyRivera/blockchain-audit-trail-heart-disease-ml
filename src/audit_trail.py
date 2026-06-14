import json
import hashlib
from datetime import datetime


def hash_file(filename):
    """Create a SHA-256 hash for a file."""
    sha256_hash = hashlib.sha256()

    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


def hash_block(block):
    """Create a SHA-256 hash for an audit block."""
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def create_audit_block(
    block_number,
    dataset_name,
    dataset_version,
    dataset_hash,
    model_name,
    model_version,
    features_used,
    hyperparameters,
    performance_metrics,
    previous_block_hash
):
    """Create one blockchain-inspired audit block."""
    audit_block = {
        "block_number": block_number,
        "dataset_name": dataset_name,
        "dataset_version": dataset_version,
        "dataset_hash": dataset_hash,
        "model_name": model_name,
        "model_version": model_version,
        "training_date": datetime.now().isoformat(),
        "features_used": features_used,
        "hyperparameters": hyperparameters,
        "performance_metrics": performance_metrics,
        "previous_block_hash": previous_block_hash
    }

    audit_block["current_block_hash"] = hash_block(audit_block)

    return audit_block


def save_audit_chain(audit_chain, output_path):
    """Save audit chain as a JSON file."""
    with open(output_path, "w") as f:
        json.dump(audit_chain, f, indent=4)
