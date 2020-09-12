import tensorflow as tf

# if gpu is low, then code will be blocked
# print(tf.reduce_sum(tf.random.normal([1000, 1000])))
print(tf.test.is_gpu_available())
print(tf.config.list_physical_devices('GPU'))

