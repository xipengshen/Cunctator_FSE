c = np.matmul(a, b)
C = tf.placeholder(dtype=tf.float32)
T = ... # some operations on tensor C
with tf.Session() as sess:
    sess.run(T, feed_dict={C: c})