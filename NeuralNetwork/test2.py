from sknn.mlp import Regressor, Layer

nn = Regressor(
    layers=[
        Layer("Rectifier", units=100),
        Layer("Linear")],
    learning_rate=0.02,
    n_iter=10)
nn.fit([0,1,2,3,4], [5,8,2,1])
