import numpy as np


#dummyimage
x = np.linspace(-5, 5, 512)
y = np.alinspace(-5, 5, 512)
xx, yy = meshgrid(x, y, sparse=True)

image = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)


def moco(stack, template, max_trans = 0, ds_factor = 0):

	'''
	params
	stack      -    image stack to correct motion
	template   -    image to use as correction template
	max_trans  -    maximum number of pixels to translate image
	ds_factor  -    amount of downsampling
	'''

	frames, height, width = stack.shape

	
	


	
	
	def downsample(image):
	
		'''
		Return an image scaled by N, averaging nearest neighbour pixels
		'''
		height, width = image.shape
		
		outImage = np.empty(height//2, width//2)
		
	return
	
	
	def downsample(srcImage, N):
		return dstImage
	
	def computeTVals(template):
		''' '''
		return tVals;
	

	def computeT(tVals):
		'''appears to return a list of translation vectors'''

		return T	
	
	

	def downsample_stack(stack):
		
		return imageStack

	
	def templateFFT(oldTVals, w):
		''''''
	
		  return tFFT
		  

	def templateTranslation(image, tFFT, w, fft2, t00Vals, t01Vals, t01Vals, t11Vals):
		''' '''
		return xy


	
	
	
	  
	  def multFFT():
		''' '''
	  
		  return product;
	  
	  
		def meanAndStdDev(image):
			''' '''
			 return mean, std
	  
	  
	  def applyAffine():
		''' '''

		 return newImage;

	 def moveByOne2 (xy):
		''' '''		
		 return newXY;
