import itertools

#Learn the transition matrix from a training text
#New version, which works with arbitrary kmers
def LearnMatrix(trainingText,alphabet,k=2):
    #The transition matrix is represented by a dictionary whose elements are kmers from the target alphabet
    mat={}
    #We will start with each matrix element equal to 0.1
    #This is to avoid having matrix elements equal to zero, because that produces likelihoods of zero
    #and we always work with the log of the likelihood.
    for kmer in itertools.product(*[alphabet]*k):
        mat[kmer] = 0.1
    for i in range(len(trainingText)-(k-1)):
        kmer = tuple(trainingText[i:i+k])
        mat[kmer] = mat[kmer]+1.0
    #Now normalize the transition matrix so that the elements in any given row add to 1.0
    #(Because they are conditional probabilities)
    for kmer in itertools.product(*[alphabet]*(k-1)):
        s=0.0
        for c in alphabet:
            s = s + mat[kmer + (c,)]
        for c in alphabet:
            mat[kmer + (c,)] = mat[kmer + (c,)]/s
    return mat

#Learn the transition matrix from a training text
def learnMatrixOld(trainingText,alphabet):
	#The transition matrix is represented by a dictionary whose keys are pairs of elements of target alphabet
	mat={}
	#We will start with each matrix element equal to 0.1
	#This is to avoid having matrix elements equal to zero, because that produces likelihoods of zero
	#and we always work with the log of the likelihood.
	for c1 in alphabet:
		for c2 in alphabet:
			mat[(c1,c2)]=0.1
	oldc = trainingText[0]
	for c in trainingText[1:]:
		mat[(oldc,c)]=mat[(oldc,c)]+1.0
		oldc=c
	#Now normalize the transition matrix so that the elements in any given row add to 1.0
	#(Because they are conditional probabilities)
	for c1 in alphabet:
		rowsum=0.0
		for c2 in alphabet:
			rowsum = rowsum + mat[(c1,c2)]
		for c2 in alphabet:
			mat[(c1,c2)]=mat[(c1,c2)]/rowsum
	return mat
	
def learnVector(trainingText, alphabet):
    '''Compute the single-character distribution of trainingText.'''
    # Initialize dictionary of (character, probability) pairs.
    v = {}
    for c in alphabet:
        v[c] = 0.1  # Avoid zeros.
        
    # Add up occurrences.
    for c in trainingText:
        v[c] = v[c] + 1
    
    # Normalize distribution.    
    norm = sum(v.values())
    for c in alphabet:
        v[c] = v[c]/norm
        
    return v
        
