import tensorflow as tf

class Network(object):
  def __init__(self, sess):
    self.sess = sess
    self.copy_op = None

  def calc_actions(self, observation):
    return self.actions.eval({self.inputs: observation}, session=self.sess)

  def calc_outputs(self, observation):
    return self.outputs.eval({self.inputs: observation}, session=self.sess)

  def calc_max_outputs(self, observation):
    return self.max_outputs.eval({self.inputs: observation}, session=self.sess)

  def run_copy(self):
    if self.copy_op is None:
      raise Exception("run `create_copy_op` first before copy")
    else:
      self.sess.run(self.copy_op)

  def create_copy_op(self, network):
    with tf.variable_scope('copy_from_target'):
      copy_ops = []

      for name in self.var.keys():
        copy_op = self.var[name].assign(network.var[name])
        copy_ops.append(copy_op)

      self.copy_op = tf.group(*copy_ops, name='copy_op')
