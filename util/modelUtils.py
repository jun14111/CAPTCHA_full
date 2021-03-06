import keras.backend as K
from keras.metrics import categorical_accuracy
from keras import Model


def word_acc(y_true, y_pred):
    out = categorical_accuracy(y_true=y_true, y_pred=y_pred)
    return K.min(out, axis=-1)


def fixAll(model: Model):
    for layer in model.layers:
        layer.trainable = False


def unFixAll(model: Model):
    for layer in model.layers:
        layer.trainable = True
