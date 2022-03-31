import hashlib

class SwarmChainBlock:
    def __init__(self, prev_block_hash, appendable_data):
        self.prev_block_hash = prev_block_hash
        self.appendable_data = appendable_data
        self.block_data = "".join(appendable_data) + "-" + prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
