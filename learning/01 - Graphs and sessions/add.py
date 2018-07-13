import tensorflow as tf
# Depicting graph and session, below code will print out tensor form and not a result since
# we only defined flow, session needs to be run in order for it to output result of calculation
a = 2
b = 3
c = tf.add(a, b, name='Add')
print(c)

# Running session gives us result of calculation

sess  =  tf.Session()
print(sess.run(c))
sess.close()

# More pytonic way

with tf.Session() as sess:
    print(sess.run(c))