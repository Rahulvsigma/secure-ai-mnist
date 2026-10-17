
import torch
import torch.nn.functional as F


def make_adversarial_image(model, images, labels, epsilon=0.15):
    images = images.clone().detach()
    labels = labels.to(images.device)
    images.requires_grad = True

    outputs = model(images)
    loss = F.cross_entropy(outputs, labels)

    model.zero_grad()
    loss.backward()

    changed_images = images + epsilon * images.grad.sign()
    changed_images = torch.clamp(changed_images, 0, 1)

    return changed_images.detach()
