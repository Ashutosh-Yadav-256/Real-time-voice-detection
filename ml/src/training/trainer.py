import json
from pathlib import Path

import torch
from torch import nn, optim


class Trainer:
    def __init__(self, model, train_loader, val_loader, learning_rate=0.001, device="cpu"):
        self.model = model.to(device)
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.criterion = nn.BCELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.device = device
        self.metrics = {"train_loss": [], "val_loss": []}

    def train_epoch(self):
        self.model.train()
        total_loss = 0.0
        for inputs, targets in self.train_loader:
            inputs = inputs.to(self.device)
            targets = targets.to(self.device)
            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = self.criterion(outputs, targets)
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(self.train_loader)

    def validate(self):
        self.model.eval()
        total_loss = 0.0
        with torch.no_grad():
            for inputs, targets in self.val_loader:
                inputs = inputs.to(self.device)
                targets = targets.to(self.device)
                outputs = self.model(inputs)
                loss = self.criterion(outputs, targets)
                total_loss += loss.item()
        return total_loss / len(self.val_loader)

    def save_checkpoint(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        torch.save(self.model.state_dict(), path)

    def fit(self, epochs, checkpoint_path):
        for epoch in range(epochs):
            train_loss = self.train_epoch()
            val_loss = self.validate()
            self.metrics["train_loss"].append(train_loss)
            self.metrics["val_loss"].append(val_loss)
            self.save_checkpoint(f"{checkpoint_path}_epoch_{epoch}.pt")
            with open(f"{checkpoint_path}_metrics.json", "w") as f:
                json.dump(self.metrics, f)
