# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import tensorflow.compat.v1 as tf
from keras import backend as K
from keras.utils import CustomObjectScope

def relu6(x):
    return K.relu(x, max_value=6)

with CustomObjectScope({'relu6': relu6}):
    tflite_model = tf.lite.TFLiteConverter.from_keras_model_file(
        'speech_commands.hdf5').convert()
    with open('model.tflite', 'wb') as f:
        f.write(tflite_model)