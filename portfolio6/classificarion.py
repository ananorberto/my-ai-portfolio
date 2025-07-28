from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# Carrega dados
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.3, random_state=42
)

# Treina modelo
mlp = MLPClassifier(hidden_layer_sizes=(64,), max_iter=300, random_state=1)
mlp.fit(X_train, y_train)

# Avalia desempenho
y_pred = mlp.predict(X_test)
print(classification_report(y_test, y_pred))