import numpy
from shogun.Kernel import DirectorKernel

class DirectorLinearKernel(DirectorKernel):
	def __init__(self):
		DirectorKernel.__init__(self)
	def has_features(self):
		return True
	def kernel_function(self, idx_a, idx_b):
		return numpy.dot(traindat[:,idx_a], traindat[:,idx_b])

traindat = numpy.random.random_sample((10,10))
testdat = numpy.random.random_sample((5,5))
parameter_list=[[traindat,testdat,1.2],[traindat,testdat,1.4]]

def kernel_director_linear_modular (fm_train_real=traindat,fm_test_real=testdat,scale=1.2):

	from shogun.Features import RealFeatures
	from shogun.Kernel import LinearKernel, AvgDiagKernelNormalizer
	from modshogun import Time

	feats_train=RealFeatures(fm_train_real)
	feats_train.io.set_loglevel(0)
	feats_train.parallel.set_num_threads(1)
	feats_test=RealFeatures(fm_test_real)
	 
	kernel=LinearKernel()
	kernel.set_normalizer(AvgDiagKernelNormalizer(scale))
	kernel.init(feats_train, feats_train)

	dkernel=DirectorLinearKernel()
	dkernel.set_normalizer(AvgDiagKernelNormalizer(scale))
	dkernel.set_num_vec_lhs(traindat.shape[0])
	dkernel.set_num_vec_rhs(traindat.shape[1])

	print  "km_train"
	t=Time()
	km_train=kernel.get_kernel_matrix()
	t1=t.cur_time_diff(True)

	print  "dkm_train"
	t=Time()
	dkm_train=dkernel.get_kernel_matrix()
	t2=t.cur_time_diff(True)

	#dkm_train=dkernel.get_kernel_matrix()
	#dkm_train=numpy.zeros((5,5))
	#for i in xrange(5):
	#	for j in xrange(5):
	#		dkm_train[i,j]=dkernel.kernel(i,j)
	

	print "km_train", km_train
	print "dkm_train", dkm_train

	return km_train, dkm_train

if __name__=='__main__':
	print('DirectorLinear')
	kernel_director_linear_modular(*parameter_list[0])
