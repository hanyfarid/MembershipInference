
# see https://huggingface.co/datasets/faridlab/stroll

from datasets import load_dataset
dataset = load_dataset("faridlab/stroll", trust_remote_code=True)

