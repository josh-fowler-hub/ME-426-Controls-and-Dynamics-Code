# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:24:49 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt

datarun = run1 = np.genfromtxt('Lab8_Run1_data.csv',
                               delimiter=',',
                               skip_header=1)
datafft = run1 = np.genfromtxt('Lab8_Run1_fft.csv',
                               delimiter=',',
                               skip_header=1)

f = open('Lab_9_LaTeX_Table_Gen.txt', 'w')
f.write('\\begin{center}\n\captionof{table}{Run 1}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage 100 Hz\\\\ \\hline')
for i in range(6):
    first = datarun[i, 0]
    second = datarun[i, 1]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 0]
    second = datarun[-i, 1]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 2}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage 400 Hz\\\\ \\hline')
for i in range(6):
    first = datarun[i, 2]
    second = datarun[i, 3]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 2]
    second = datarun[-i, 3]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 3}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage 600 Hz\\\\ \\hline')
for i in range(6):
    first = datarun[i, 4]
    second = datarun[i, 5]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 4]
    second = datarun[-i, 5]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 4}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage 900 Hz\\\\ \\hline')
for i in range(6):
    first = datarun[i, 6]
    second = datarun[i, 7]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 6]
    second = datarun[-i, 7]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 1 FFT}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage (FFT - (Peak))&Amplitude - Voltage (FFT - (Peak)) '
        + '100 hz\\\\ \\hline')
for i in range(6):
    first = datafft[i, 0]
    second = datafft[i, 1]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datafft[-i, 0]
    second = datafft[-i, 1]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 2 FFT}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage (FFT - (Peak))&Amplitude - Voltage (FFT - (Peak)) '
        + '400 hz\\\\ \\hline')
for i in range(6):
    first = datafft[i, 2]
    second = datafft[i, 3]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datafft[-i, 2]
    second = datafft[-i, 3]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 3 FFT}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage (FFT - (Peak))&Amplitude - Voltage (FFT - (Peak)) '
        + '600 hz\\\\ \\hline')
for i in range(6):
    first = datafft[i, 4]
    second = datafft[i, 5]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datafft[-i, 4]
    second = datafft[-i, 5]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\captionof{table}{Run 4 FFT}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage (FFT - (Peak))&Amplitude - Voltage (FFT - (Peak)) '
        + '900 hz\\\\ \\hline')
for i in range(6):
    first = datafft[i, 6]
    second = datafft[i, 7]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datafft[-i, 6]
    second = datafft[-i, 7]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}')
f.close()

plt.figure()
plt.plot(datarun[:, 0], datarun[:, 1])
plt.xlabel('Time', fontsize=16)
plt.ylabel('Amplitude - Voltage 100 Hz', fontsize=16)
plt.title('Time vs. Amplitude', fontsize=20)
plt.xlim([min(datarun[:, 0]), max(datarun[:, 0])])
plt.ylim([min(datarun[:, 1]), max(datarun[:, 1])])
plt.grid()
plt.savefig('Lab_8_Run1.png')
plt.show()

plt.figure()
plt.plot(datarun[:, 2], datarun[:, 3])
plt.xlabel('Time', fontsize=16)
plt.ylabel('Amplitude - Voltage 400 Hz', fontsize=16)
plt.title('Time vs. Amplitude', fontsize=20)
plt.xlim([min(datarun[:, 2]), max(datarun[:, 2])])
plt.ylim([min(datarun[:, 3]), max(datarun[:, 3])])
plt.grid()
plt.savefig('Lab_8_Run2.png')
plt.show()

plt.figure()
plt.plot(datarun[:, 4], datarun[:, 5])
plt.xlabel('Time', fontsize=16)
plt.ylabel('Amplitude - Voltage 600 Hz', fontsize=16)
plt.title('Time vs. Amplitude', fontsize=20)
plt.xlim([min(datarun[:, 4]), max(datarun[:, 4])])
plt.ylim([min(datarun[:, 5]), max(datarun[:, 5])])
plt.grid()
plt.savefig('Lab_8_Run3.png')
plt.show()

plt.figure()
plt.plot(datarun[:, 6], datarun[:, 7])
plt.xlabel('Time', fontsize=16)
plt.ylabel('Amplitude - Voltage 900 Hz', fontsize=16)
plt.title('Time vs. Amplitude', fontsize=20)
plt.xlim([min(datarun[:, 6]), max(datarun[:, 6])])
plt.ylim([min(datarun[:, 7]), max(datarun[:, 7])])
plt.grid()
plt.savefig('Lab_8_Run4.png')
plt.show()

plt.figure()
plt.plot(datafft[:, 0], datafft[:, 1])
plt.xlabel('Time - Voltage (FFT - (Peak))', fontsize=16)
plt.ylabel('Amplitude - Voltage (FFT - (Peak)) 100 hz', fontsize=16)
plt.title('Time vs. Amplitude: Fast Fourier Transform', fontsize=18)
plt.xlim([min(datafft[:, 0]), max(datafft[:, 0])])
plt.ylim([min(datafft[:, 1]), max(datafft[:, 1])])
plt.grid()
plt.savefig('Lab_8_Run1_fft.png')
plt.show()

plt.figure()
plt.plot(datafft[:, 2], datafft[:, 3])
plt.xlabel('Time - Voltage (FFT - (Peak))', fontsize=16)
plt.ylabel('Amplitude - Voltage (FFT - (Peak)) 400 hz', fontsize=16)
plt.title('Time vs. Amplitude: Fast Fourier Transform', fontsize=18)
plt.xlim([min(datafft[:, 2]), max(datafft[:, 2])])
plt.ylim([min(datafft[:, 3]), max(datafft[:, 3])])
plt.grid()
plt.savefig('Lab_8_Run2_fft.png')
plt.show()

plt.figure()
plt.plot(datafft[:, 4], datafft[:, 5])
plt.xlabel('Time - Voltage (FFT - (Peak))', fontsize=16)
plt.ylabel('Amplitude - Voltage (FFT - (Peak)) 600 hz', fontsize=16)
plt.title('Time vs. Amplitude: Fast Fourier Transform', fontsize=18)
plt.xlim([min(datafft[:, 4]), max(datafft[:, 4])])
plt.ylim([min(datafft[:, 5]), max(datafft[:, 5])])
plt.grid()
plt.savefig('Lab_8_Run3_fft.png')
plt.show()

plt.figure()
plt.plot(datafft[:, 6], datafft[:, 7])
plt.xlabel('Time - Voltage (FFT - (Peak))', fontsize=16)
plt.ylabel('Amplitude - Voltage (FFT - (Peak)) 900 hz', fontsize=16)
plt.title('Time vs. Amplitude: Fast Fourier Transform', fontsize=18)
plt.xlim([min(datafft[:, 6]), max(datafft[:, 6])])
plt.ylim([min(datafft[:, 7]), max(datafft[:, 7])])
plt.grid()
plt.savefig('Lab_8_Run4_fft.png')
plt.show()

