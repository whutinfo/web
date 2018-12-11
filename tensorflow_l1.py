import tensorflow as tf
b = tf.variable(tf.zeros([100]))
w=tf.variable(tf.random_uniform[784,100],-1,1)
x=tf.placeholder(name = "x")
relu=tf.nn.relu(tf.matmul(w,x)+b)
c=[...]
s=tf.session()
for step in range(0,10):
	input = "...construct 100-D input array ..."
	result=s.run(c,feed_dict={x:input})
	print(step,result)