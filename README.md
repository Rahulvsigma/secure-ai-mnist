# Secure AI Systems: Red Team and Blue Team on MNIST

## Project Overview

This project aims to find the security of a Convolutional Neural Network (CNN) model trained to classify hand-written digits from MNIST dataset. It covers adversarial attacks, training data poisoning, static application security testing and defence strategies.

## Objectives

Construct and test a CNN with PyTorch.
Use STRIDE and LINDDUN to model threats to security and threats to privacy, respectively.
- Using Bandit, scan Python source code.
Discuss FGSM adversarial attacks.
- Investigate random training-label poisoning.
Propose defenses of adversarial training and input smoothing.

## Technologies Used

- Python
- PyTorch and Torchvision
- MNIST dataset
- Matplotlib
- Scikit-learn
- Pandas
- Bandit

## Model Architecture

The CNN has two convolutional layers, ReLU activation, max-pooling layers, dropout layer and fully connected layers. It foretells one of the ten digit classes.

## Experimental Results

Experiment | Clean Accuracy | Adversarial Accuracy | Test Loss |
|---|---:|---:|---:|
| Baseline CNN | 98.96% | — | 0.0300 |
| FGSM attack | — | 72.78% | — |
| Random label poisoning (10%) | 98.83% | — | 0.1531 |
| Adversarial training | 98.82% | 87.79% | 0.0367 |
| Adversarial training + smoothing | 98.12% | 91.28% | Not measured |

epsilon = 0.15 was the perturbation strength used for the FGSM attack. It caused 2,722 of 10,000 test images to be misclassified.

Label poisoning altered 6000 of 60,000 training labels, with random poisoning. This model obtained 98.83% accuracy on the original test set, which was clean.

Adversarial training brought the FGSM accuracy up from 72.78% to 87.79%. The accuracy of the measurement has been improved to 91.28% using average-pooling input smoothing and clean accuracy is 98.12%.

The following are experimental outcomes of this implementation, and do not provide guarantees of robustness in general.

## Threat Modeling

STRIDE is explored in this project, which includes threats to spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege. It talks about privacy threats in the context of handwriting recognition systems in the real world, relevant to LINDDUN.

The basic experimental attacks are input manipulation and training-data poisoning, which are correlated to the respective risks listed in the OWASP Machine Learning Security Top 10.

## SAST Results

Bandit ran the 23-line CNN model implementation and found no problems. The absence of a scan doesn't mean the entire application is secure.

## Repository Contents

- `Secure_AI_MNIST_Assignment.ipynb` — Complete experiment notebook.
- `requirements.txt` — Required Python packages.
- `src/train.py` — CNN model implementation.
- `src/attacks.py` — FGSM adversarial attack.
- `src/poisoning.py` — Random label-poisoning experiment helper.
- `src/defenses.py` — Adversarial training and input-smoothing helpers.
- `results/experiment_results.csv` — Recorded experiment results.

## Limitations

A small CNN and MNIST dataset are used for the experiments. The poisoning experiment is a random ‘label change' experiment and does not prove a targeted ‘back door'. The smoothing experiment is a preliminary defense test, which is not tested with a fully adaptive attacker.

## Conclusion

The CNN baseline was very clean but was sensitive to FGSM perturbations. Adversarial training provided a good increase in robustness without sacrificing clean accuracy. In this experiment, the clean accuracy had a slight negative impact from random label poisoning. More testing should be done to evaluate the robustness to stronger and adaptive attacks.

## Reproducibility

Experimental code and recorded outputs are in the notebook. Software versions, hardware and training settings can have an impact on results.
