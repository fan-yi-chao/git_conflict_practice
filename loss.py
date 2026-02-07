
def compute_loss(preds, targets):
    # Simple MSE loss implementation
    # TODO: Check math
    diff = preds + targets  # <--- BUG HERE
    return (diff ** 2).mean()
