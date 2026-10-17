
import copy
import random
import torch


def create_poisoned_dataset(dataset, poison_count=6000):
    poisoned_dataset = copy.deepcopy(dataset)
    poisoned_dataset.targets = dataset.targets.clone()

    random.seed(42)
    selected_indices = random.sample(
        range(len(poisoned_dataset.targets)),
        poison_count
    )

    for index in selected_indices:
        old_label = poisoned_dataset.targets[index].item()
        change = random.randint(1, 9)
        poisoned_dataset.targets[index] = (old_label + change) % 10

    return poisoned_dataset


if __name__ == "__main__":
    print("This module creates a label-poisoned MNIST dataset.")
