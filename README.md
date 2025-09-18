This project is about processing ECG (Electro Cargiogram) signals. Since its not real time processing, the data for processing are obtained form physionet.org MIT-BIH. Information about each process is available in either notebook 
or in .py code file.

Following tasks are performed in this project:- 
  1. Taking the discrete time input signal from raw .dat .hea and .atr file using the library wfdb(waveform database)
  2. Preprocessing of the signal. i.e to apply filter and take finite sample form the database
  3. Calculation of the R peak index using the derivative and threshold method
  4. Calculation of the HR (Heart Rate) using the atr file R peak index and manually computed R peak index
  5. HRV analysis.

The core python code is located in the src folder the notebook folder contains the .ipynb files are mostly used for visualization purposes.
