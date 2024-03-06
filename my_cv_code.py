import numpy as np

def k_fold_cross_validation(model, X, y, k):
    n = len(X)
    fold_size = n // k
    validation_errors = []

    for i in range(k):
        # Split the data into training and validation sets
        validation_indices = np.arange(i * fold_size, min((i + 1) * fold_size, n))
        training_indices = np.concatenate([np.arange(0, i * fold_size),
                                           np.arange((i + 1) * fold_size, n)])

        X_train, y_train = X.iloc[training_indices], y.iloc[training_indices]
        X_val, y_val = X.iloc[validation_indices], y.iloc[validation_indices]

        # Train the model
        model.fit(X_train, y_train)

        # Evaluate the model on the validation set
        validation_error = 1 - model.score(X_val, y_val)
        validation_errors.append(validation_error)

    # Compute and print the average validation error
    avg_validation_error = np.mean(validation_errors)
    return avg_validation_error