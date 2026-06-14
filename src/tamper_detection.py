import copy
from audit_trail import hash_block


def recalculate_block_hash(block):
    """Recalculate an audit block hash after removing the saved hash."""
    block_copy = copy.deepcopy(block)
    block_copy.pop("current_block_hash", None)
    return hash_block(block_copy)


def verify_audit_chain(chain):
    """Verify whether an audit chain is valid."""
    verification_results = []
    chain_is_valid = True

    for i, block in enumerate(chain):
        saved_current_hash = block["current_block_hash"]
        recalculated_hash = recalculate_block_hash(block)
        hash_matches = saved_current_hash == recalculated_hash

        if i == 0:
            previous_hash_matches = block["previous_block_hash"] == "0"
        else:
            previous_hash_matches = block["previous_block_hash"] == chain[i - 1]["current_block_hash"]

        block_is_valid = hash_matches and previous_hash_matches

        if not block_is_valid:
            chain_is_valid = False

        verification_results.append({
            "block_number": block["block_number"],
            "model_name": block["model_name"],
            "hash_matches": hash_matches,
            "previous_hash_matches": previous_hash_matches,
            "block_is_valid": block_is_valid
        })

    return {
        "chain_is_valid": chain_is_valid,
        "verification_results": verification_results
    }
