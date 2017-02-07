import pickle

class Storage:

	def __init__(self):
		self.dct = self.loader()

	def loader(self,fname='data.pkl'):
		try:
			pkl_file = open(fname,'rb')
			pkl_data = pickle.load(pkl_file)
			pkl_file.close()
			return(pkl_data)
		except:
			pkl_file = open(fname,'wb')
			dct = {'id': [123, 124, 125]}
			pickle.dump(dct,pkl_file)
			pkl_file.close()
			return(dct)

	def flush(self, fname='data.pkl', dct = None):
		if dct == None:
			dct = self.dct
		pkl_file = open(fname,'wb')
		pickle.dump(dct,pkl_file)
		pkl_file.close()
