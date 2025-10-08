# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 01:10:31 2018

@author: jfowl
"""
import numpy as np

datarun = np.genfromtxt('Lab_9_data.csv',
                        delimiter=',',
                        skip_header=1)

f = open('Lab_9_LaTeX_Table_Gen.txt', 'w')
f.write('\\begin{center}\n\\captionof{table}{Run 1}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
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
f.write('\\begin{center}\n\\captionof{table}{Run 2}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
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
f.write('\\newpage\n')
f.write('\\begin{center}\n\\captionof{table}{Run 3}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage\\\\ \\hline')
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
f.write('\\begin{center}\n\\captionof{table}{Run 4}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage&Amplitude - Voltage\\\\ \\hline')
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
f.write('\\newpage\n')
f.write('\\begin{center}\n\\captionof{table}{Run 5}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 8]
    second = datarun[i, 9]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 8]
    second = datarun[-i, 9]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\\captionof{table}{Run 6}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 10]
    second = datarun[i, 11]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 10]
    second = datarun[-i, 11]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\newpage\n')
f.write('\\begin{center}\n\\captionof{table}{Run 7}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 12]
    second = datarun[i, 13]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 12]
    second = datarun[-i, 13]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\\captionof{table}{Run 8}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 14]
    second = datarun[i, 15]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 14]
    second = datarun[-i, 15]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\newpage\n')
f.write('\\begin{center}\n\\captionof{table}{Run 9}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 16]
    second = datarun[i, 17]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 16]
    second = datarun[-i, 17]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\begin{center}\n\\captionof{table}{Run 10}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 18]
    second = datarun[i, 19]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 18]
    second = datarun[-i, 19]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}\n')
f.write('\\newpage\n')
f.write('\\begin{center}\n\\captionof{table}{Run 11}\n' +
        '\t\\begin{tabular}{|l|l|}\\hline')
f.write('\nTime - Voltage	&Amplitude - Voltage\\\\ \\hline')
for i in range(6):
    first = datarun[i, 20]
    second = datarun[i, 21]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n.&.\\\\\n.&.\\\\\n.&.\\\\')
for i in range(6):
    first = datarun[-i, 20]
    second = datarun[-i, 21]
    line = '\n{}&{}\\\\ \\hline'.format(first, second)
    f.writelines(line)
f.write('\n\t\\end{tabular}\n\\end{center}')
f.close()
