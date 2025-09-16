import wfdb
import numpy as np 
import matplotlib.pyplot as plt
record = wfdb.rdrecord('100', sampfrom=0, sampto=1000, channels=[0, 1]) # Read first 1000 samples of channels 0 and 1 from record '100'
#wfdb.plot_wfdb(record=record, title='Record 100: First 1000 samples of channels 0 and 1', time_units='seconds') # Plot the record with specified title and time units
annotation = wfdb.rdann('100', 'atr', sampfrom=0, sampto=1000) # Read annotations from the same record
#wfdb.plot_wfdb(record=record, annotation=annotation, title='Record 100 with Annotations', time_units='seconds') # Plot the record with annotations

signal_list = np.array(record.p_signal.tolist())
print(np.array(signal_list).shape)
print(signal_list[0:40,:])
print(record.sig_name)

k = np.arange(0, signal_list.shape[0])
plt.plot(k,signal_list[:,0], label=record.sig_name[0])

plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('ECG Signal from Record 100')
plt.legend()
plt.show()
