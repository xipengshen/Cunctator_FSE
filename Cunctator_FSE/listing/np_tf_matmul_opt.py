A = tf.placehoder(dtype=tf.float32)
B = tf.placehoder(dtype=tf.float32)
C = A * B
T = ... # some operations on tensor C
with tf.Session() as sess:
    sess.run(T, feed_dict={A: a, B: b})