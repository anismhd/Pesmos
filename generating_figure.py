from numpy import linspace, argmax
import matplotlib.pyplot as plt
def max_peak_finder():
	pass
def gen_accl_figure(data):
	time = linspace(0,len(data['E-W']['Time Series'])-1,len(data['E-W']['Time Series']))/data['Sampling Rate']
	f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(25,3), sharey=True)
	ax1.plot(time, data['N-S']['Time Series'], 'k')
	PGA = max(abs(data['N-S']['Time Series']))
	index = argmax(abs(data['N-S']['Time Series']))
	ax1.scatter(time[index],data['N-S']['Time Series'][index], edgecolors='r', marker='o', facecolors='none', label='PGA:{0:8.3f} {1:s}'.format(PGA,data['N-S']['Unit']))
	ax1.set_xlabel('time (sec)')
	ax1.set_ylabel(data['N-S']['Unit'])
	ax1.set_title('N-S')
	ax1.legend(scatterpoints=1)
	ax2.plot(time, data['E-W']['Time Series'], 'k')
	PGA = max(abs(data['E-W']['Time Series']))
	index = argmax(abs(data['E-W']['Time Series']))
	ax2.scatter(time[index],data['E-W']['Time Series'][index], edgecolors='r', marker='o', facecolors='none', label='PGA:{0:8.3f} {1:s}'.format(PGA,data['Vertical']['Unit']))
	ax2.set_xlabel('time (sec)')
	ax2.set_ylabel(data['E-W']['Unit'])
	ax2.set_title('E-W')
	ax2.legend(scatterpoints=1)
	ax3.plot(time, data['Vertical']['Time Series'], 'k')
	PGA = max(abs(data['Vertical']['Time Series']))
	index = argmax(abs(data['Vertical']['Time Series']))
	ax3.scatter(time[index],data['Vertical']['Time Series'][index], edgecolors='r', marker='o', facecolors='none', label='PGA:{0:8.3f} {1:s}'.format(PGA,data['Vertical']['Unit']))
	ax3.set_xlabel('time (sec)')
	ax3.set_ylabel(data['Vertical']['Unit'])
	ax3.set_title('Vertical')
	ax3.legend(scatterpoints=1)
	plt.tight_layout()
	return f