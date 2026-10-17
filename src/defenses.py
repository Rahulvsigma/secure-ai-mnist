
import torch.nn.functional as F


def smooth_images(images):
    return F.avg_pool2d(
        images,
        kernel_size=3,
        stride=1,
        padding=1
    )


def train_with_adversarial_examples(
    model,
    data_loader,
    optimizer,
    device,
    epochs=3
):
    model.train()

    for epoch in range(epochs):
        total_loss = 0

        for images, labels in data_loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = F.cross_entropy(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        average_loss = total_loss / len(data_loader)
        print(
            f"Epoch {epoch + 1}: "
            f"Loss = {average_loss:.4f}"
        )

    return model
