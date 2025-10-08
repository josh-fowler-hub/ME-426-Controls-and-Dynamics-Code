# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:30:03 2018

@author: jfowl
"""

from numba import jit
import numpy as np
import scipy.stats as st
import Python_Tools.Table_Maker as TM
import statsmodels.stats.weightstats as ws
import matplotlib.pyplot as plt
import datetime as dt
import os

start = dt.datetime.now()
print('Program Start on: {} .....'.format(start))


cwd = os.getcwd()  # Gets the current working directory

print('The following was imported for use:')
print('\n')
print(np.__name__)
print(plt.__name__)
print(TM.__name__)
print(dt.__name__)
print('\n')  # The \ is an escape character that tells the interpreter to
# treat the following character as a special character or treat a special
# character as a regular character, in this case \n is a new line
print('The current working directory is: {}'.format(cwd))
print('\n')

clss = 'ME_429'
lab = 'Lab1'
task = ['Task1', 'Task2', 'Task3']
Vs = ['Vin', 'Vout', 'Vout_Vin']
hist = 'Histogram'
dens = 'Density_Plot'

Task1 = np.genfromtxt(
        cwd + '\\ME_429_Lab1_Task1.csv',
        delimiter=',',
        skip_header=1,
        usecols=(1))
Task2 = np.genfromtxt(
        cwd + '\\ME_429_Lab1_Task2.csv',
        delimiter=',',
        skip_header=1)
Task3 = np.genfromtxt(
        cwd + '\\ME_429_Lab1_Task3.csv',
        delimiter=',',
        skip_header=1)

for i in range(len(Task1)):
    Task1[i] = Task1[i]*1000

for i in range(len(Task3[:, 1])):
    Task3[i, 1] = Task3[i, 1]/1000


@jit
def samp_mean(xs):
    tot = 0
    for x in xs:
        tot += x
    x_bar = tot/len(xs)
    return x_bar


@jit
def samp_Var_std(xs):
    tot = 0
    for x in xs:
        tot += (x - samp_mean(xs))**2
    Var = tot/(len(xs) - 1)
    std = np.sqrt(tot/(len(xs) - 1))
    return Var, std


@jit
def Z_score(xs):
    x_bar = samp_mean(xs)
    Var, std = samp_Var_std(xs)
    Zs = []
    outliers = []
    for x in xs:
        Zs.append(round((x - x_bar)/std, 5))
        if (x - x_bar)/std > 3.0:
            outliers.append([x, round((x - x_bar)/std, 5)])
    return Zs, outliers


@jit
def mean_uncert(xs, delta=0):
    Var, std = samp_Var_std(xs)
    un = std/np.sqrt(len(xs))
    if delta > un:
        un = delta
    else:
        pass
    return un


@jit
def uncert_multiply(xs, ys, delta1=0, delta2=0):
    xbar, ybar = samp_mean(xs), samp_mean(ys)
    dxbar, dybar = mean_uncert(xs, delta1), mean_uncert(ys, delta2)
    un = xbar*ybar*((dxbar/xbar) + (dybar/ybar))
    return un


@jit
def uncert_divide(xs, ys, delta1=0, delta2=0):
    xbar, ybar = samp_mean(xs), samp_mean(ys)
    dxbar, dybar = mean_uncert(xs, delta1), mean_uncert(ys, delta2)
    un = (xbar/ybar)*((dxbar/xbar) + (dybar/ybar))
    return un


@jit
def uncert_add_subtract(xs, ys, delta1=0, delta2=0):
    dxbar, dybar = mean_uncert(xs, delta1), mean_uncert(ys, delta2)
    un = dxbar + dybar
    return un


@jit
def t_test_range(xs, pop_means):
    tpx = 'Sample Mean != Population Mean in Range Specified!'
    for mu in pop_means:
        t_value, p_value = st.ttest_1samp(xs, mu)
        if p_value > 0.05:
            tpx = [t_value, p_value, mu]
        else:
            continue
    return tpx


@jit
def z_test_range(xs, pop_means):
    tpx = 'Sample Mean != Population Mean in Range Specified!'
    for mu in pop_means:
        z_value, p_value = ws.ztest(xs, value=mu)
        if p_value > 0.05:
            tpx = [z_value, p_value, mu]
        else:
            continue
    return tpx


print('Performing Calculations .....')

task1_avg = samp_mean(Task1)
task2_avg0 = samp_mean(Task2[:, 0])
task2_avg1 = samp_mean(Task2[:, 1])
task2_avg2 = samp_mean(Task2[:, 2])
task3_avg0 = samp_mean(Task3[:, 0])
task3_avg1 = samp_mean(Task3[:, 1])
task3_avg2 = samp_mean(Task3[:, 2])

task1_Var, task1_std = samp_Var_std(Task1)
task2_Var0, task2_std0 = samp_Var_std(Task2[:, 0])
task2_Var1, task2_std1 = samp_Var_std(Task2[:, 1])
task2_Var2, task2_std2 = samp_Var_std(Task2[:, 2])
task3_Var0, task3_std0 = samp_Var_std(Task3[:, 0])
task3_Var1, task3_std1 = samp_Var_std(Task3[:, 1])
task3_Var2, task3_std2 = samp_Var_std(Task3[:, 2])

task1_Z, outliers1 = Z_score(Task1)
task2_Z0, outliers20 = Z_score(Task2[:, 0])
task2_Z1, outliers21 = Z_score(Task2[:, 1])
task2_Z2, outliers22 = Z_score(Task2[:, 2])
task3_Z0, outliers30 = Z_score(Task3[:, 0])
task3_Z1, outliers31 = Z_score(Task3[:, 1])
task3_Z2, outliers32 = Z_score(Task3[:, 2])

task1_dens = st.kde.gaussian_kde(Task1)
task1_space = np.linspace(min(Task1), max(Task1), 150)
task2_dens0 = st.kde.gaussian_kde(Task2[:, 0])
task2_space0 = np.linspace(min(Task2[:, 0]), max(Task2[:, 0]), 150)
task2_dens1 = st.kde.gaussian_kde(Task2[:, 1])
task2_space1 = np.linspace(min(Task2[:, 1]), max(Task2[:, 1]), 150)
task2_dens2 = st.kde.gaussian_kde(Task2[:, 2])
task2_space2 = np.linspace(min(Task2[:, 2]), max(Task2[:, 2]), 150)
task3_dens0 = st.kde.gaussian_kde(Task3[:, 0])
task3_space0 = np.linspace(min(Task3[:, 0]), max(Task3[:, 0]), 150)
task3_dens1 = st.kde.gaussian_kde(Task3[:, 1])
task3_space1 = np.linspace(min(Task3[:, 1]), max(Task3[:, 1]), 150)
task3_dens2 = st.kde.gaussian_kde(Task3[:, 2])
task3_space2 = np.linspace(min(Task3[:, 2]), max(Task3[:, 2]), 150)

task1_delta = (task1_avg + 2)*0.01
task2_delta0 = (task2_avg0 + 0.002)*0.005
task2_delta1 = (task2_avg1 + 0.002)*0.005
task3_delta0 = (task2_avg0 + 0.002)*0.005
task3_delta1 = (task2_avg1 + 0.0002)*0.1

task1_un = mean_uncert(Task1, task1_delta)
task2_un0 = mean_uncert(Task2[:, 0], task2_delta0)
task2_un1 = mean_uncert(Task2[:, 1], task2_delta1)
task2_un2 = uncert_divide(Task2[:, 1], Task2[:, 0], task2_delta1, task2_delta0)
task3_un0 = mean_uncert(Task3[:, 0], task3_delta0)
task3_un1 = mean_uncert(Task3[:, 1], task3_delta1)
task3_un2 = uncert_divide(Task3[:, 1], Task3[:, 0], task3_delta1, task2_delta0)

alpha = 1 - 0.025

dof1 = len(Task1) - 1
dof2 = len(Task2[:, 0]) - 1
dof3 = len(Task3[:, 0]) - 1

task1_t = st.t.ppf(alpha, dof1)
task2_t = st.t.ppf(alpha, dof2)
task3_t = st.t.ppf(alpha, dof3)

task1_CL = task1_std*task1_t
task2_CL0 = task2_std0*task2_t
task2_CL1 = task2_std1*task2_t
task2_CL2 = task2_std2*task2_t
task3_CL0 = task3_std0*task2_t
task3_CL1 = task3_std1*task2_t
task3_CL2 = task3_std2*task2_t

task1_chi2 = st.chi2.ppf(alpha, dof1)
task2_chi2 = st.chi2.ppf(alpha, dof2)
task3_chi2 = st.chi2.ppf(alpha, dof3)

task1_s = (task1_std*np.sqrt(dof1))/task1_chi2
task2_s0 = (task2_std0*np.sqrt(dof2))/task1_chi2
task2_s1 = (task2_std1*np.sqrt(dof2))/task1_chi2
task2_s2 = (task2_std2*np.sqrt(dof2))/task1_chi2
task3_s0 = (task3_std0*np.sqrt(dof3))/task1_chi2
task3_s1 = (task3_std1*np.sqrt(dof3))/task1_chi2
task3_s2 = (task3_std2*np.sqrt(dof3))/task1_chi2

task1_mfg = 1000*0.05
task2_mfg = 0.5*task2_avg2*0.01
task3_mfg = task3_avg0*0.01

print('..... Calculations Complete')
print('\n')
tdelta = dt.datetime.now() - start
tmess = 'Time Taken: {}.....'.format(tdelta)
print(tmess)

print('Displaying Descriptive Statistics .....')
Desc_names1 = ['  Task', ' Mean', '  Variance', ' Standard Dev']
header1 = 'Descriptive Statistics '
footer1 = 'Task 1: Resistances Task2: Voltage Divider Task3: Wheatstone Bridge'
print('\tWriting Results to CSV File .....')
desc_stats = []
desc_stats.append(Desc_names1)
desc_stats.append(['Task 1', task1_avg, task1_Var, task1_std])
desc_stats.append(['Task 2 Vin', task2_avg0, task2_Var0, task2_std0])
desc_stats.append(['Task 2 Vout', task2_avg1, task2_Var1, task2_std1])
desc_stats.append(['Task 2 Vout/Vin', task2_avg2, task2_Var2, task2_std2])
desc_stats.append(['Task 3 Vin', task3_avg0, task3_Var0, task3_std0])
desc_stats.append(['Task 3 Vout', task3_avg1, task3_Var1, task3_std1])
desc_stats.append(['Task 3 Vout/Vin', task3_avg2, task3_Var2, task3_std2])
desc_stats = np.asanyarray(desc_stats)
filename1 = 'ME_429_Lab1_Desc_Stats.csv'
np.savetxt(filename1, desc_stats, delimiter=',', fmt='%s')
Z_names = ['Task 1', 'Task 2 Vin', 'Task 2 Vout', 'Task 2 Out',
           'Task 3 Vin', 'Task 3 Vout', 'Task 3 Out']
Zs1 = []
Zs1.append(Z_names)
for i in range(len(task2_Z0)):
    Z1 = task1_Z[i]
    Z2 = task2_Z0[i]
    Z3 = task2_Z1[i]
    Z4 = task2_Z2[i]
    try:
        Z5 = task3_Z0[i]
        Z6 = task3_Z1[i]
        Z7 = task3_Z2[i]
    except IndexError:
        Z5 = 'N/A'
        Z6 = 'N/A'
        Z7 = 'N/A'
    row = [Z1, Z2, Z3, Z4, Z5, Z6, Z7]
    Zs1.append(row)

Zs1 = np.asanyarray(Zs1)
filename2 = 'ME_429_Lab1_Zscores.csv'
np.savetxt(filename2, Zs1, delimiter=',', fmt='%s')
print('''\t..... Results Written to CSV''' +
      '''file in location:\n\t{} \n\tunder filenames:\n\t{}\n\t{}'''.format(
              cwd, filename1, filename2))
Desc_Table = TM.Table_Maker(Desc_names1, header1, footer1, horz_sep='',
                            vert_sep='')
Desc_Table.header_print()
Desc_Table.field_print()
Desc_Table.row_print(['Task 1', task1_avg, task1_Var, task1_std])
Desc_Table.row_print(['Task 2 Vin', task2_avg0, task2_Var0, task2_std0])
Desc_Table.row_print(['Task 2 Vout', task2_avg1, task2_Var1, task2_std1])
Desc_Table.row_print(['Task 2 Vout/Vin', task2_avg2, task2_Var2, task2_std2])
Desc_Table.row_print(['Task 3 Vin', task3_avg0, task3_Var0, task3_std0])
Desc_Table.row_print(['Task 3 Vout', task3_avg1, task3_Var1, task3_std1])
Desc_Table.row_print(['Task 3 Vout/Vin', task3_avg2, task3_Var2, task3_std2])
Desc_Table.footer_print()

print('\n\n')
print('..... Descriptive Statistics Displayed')
print('\n')
tdelta = dt.datetime.now() - start
tmess = 'Time Taken: {}.....'.format(tdelta)
print(tmess)
print('\n\n')

print('Displaying Plots .....')

plt.figure()
plt.hist(Task1, bins=8, label='Resistance')
plt.xlabel('Resistance (Ohms)')
plt.ylabel('Count')
plt.title('Histogram: Resistance')
plt.legend()
plt.savefig('{}_{}_{}_{}'.format(clss, lab, task[0], hist))
plt.show()

plt.figure()
plt.plot(task1_space, task1_dens(task1_space), label='Distribution')
plt.xlabel('Resistance (Ohms)')
plt.ylabel('Probability Density')
plt.title('Density: Resistance')
plt.legend()
plt.savefig('{}_{}_{}_{}'.format(clss, lab, task[0], dens))
plt.grid()

plt.show()

plt.figure()
plt.hist(Task2[:, 0], bins=16, label='Vin')
plt.xlabel('Voltage (V)')
plt.ylabel('Count')
plt.title('Histogram: Task 2 Voltage In')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[0], hist))
plt.show()

plt.figure()
plt.plot(task2_space0, task2_dens0(task2_space0), label='Distribution')
plt.xlabel('Voltage (V)')
plt.ylabel('Probability Density')
plt.title('Density: Task 2 Voltage In')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[0], dens))
plt.show()

plt.figure()
plt.hist(Task2[:, 1], bins=20, label='Vout')
plt.xlabel('Voltage (V)')
plt.ylabel('Count')
plt.title('Histogram: Task 2 Voltage Out')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[1], hist))
plt.show()

plt.figure()
plt.plot(task2_space1, task2_dens1(task2_space1), label='Distribution')
plt.xlabel('Voltage (V)')
plt.ylabel('Probability Density')
plt.title('Density: Task 2 Voltage Out')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[1], dens))
plt.show()

plt.figure()
plt.hist(Task2[:, 2], bins=20, label='Vout/Vin')
plt.xlabel('Vout/Vin')
plt.ylabel('Count')
plt.title('Histogram: Task 2 Voltage Out / Voltage In')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[2], hist))
plt.show()

plt.figure()
plt.plot(task2_space2, task2_dens2(task2_space2), label='Distribution')
plt.xlabel('Vout/Vin')
plt.ylabel('Probability Density')
plt.title('Density: Task 2 Voltage Out / Voltage In')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[2], dens))
plt.show()

plt.figure()
plt.hist(Task3[:, 0], bins=16, label='Vin')
plt.xlabel('Voltage (V)')
plt.ylabel('Count')
plt.title('Histogram: Task 3 Voltage In')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[1], Vs[2], hist))
plt.show()

plt.figure()
plt.plot(task3_space0, task3_dens0(task3_space0), label='Distribution')
plt.xlabel('Voltage (V)')
plt.ylabel('Probability Density')
plt.title('Density: Task 3 Voltage In')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[2], Vs[0], dens))
plt.show()

plt.figure()
plt.hist(Task3[:, 1], bins=20, label='Vout')
plt.xlabel('Voltage (V)')
plt.ylabel('Count')
plt.title('Histogram: Task 3 Voltage Out')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[2], Vs[1], hist))
plt.show()

plt.figure()
plt.plot(task3_space1, task3_dens1(task3_space1), label='Distribution')
plt.xlabel('Voltage (V)')
plt.ylabel('Probability Density')
plt.title('Density: Task 3 Voltage Out')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[2], Vs[1], dens))
plt.show()

plt.figure()
plt.hist(Task3[:, 2], bins=20, label='Vout/Vin')
plt.xlabel('Vout/Vin')
plt.ylabel('Count')
plt.title('Histogram: Task 3 Voltage Out / Voltage In')
plt.legend()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[2], Vs[2], hist))
plt.show()

plt.figure()
plt.plot(task3_space2, task3_dens2(task3_space2), label='Distribution')
plt.xlabel('Vout/Vin')
plt.ylabel('Probability Density')
plt.title('Density: Task 3 Voltage Out / Voltage In')
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_{}_{}'.format(clss, lab, task[2], Vs[2], dens))
plt.show()
print('..... Plots Displayed')
print('\n')
tdelta = dt.datetime.now() - start
tmess = 'Time Taken: {}.....'.format(tdelta)
print(tmess)

print('\n\n')
print('Performing Hypothesis Testing .....')
print('Task 1 Values')
print('-'*72)
print('Mean Resistance = {} +- {} Ohms'.format(task1_avg, task1_un))
print('Population Mean: {} +- {} Ohms'.format(task1_avg, task1_CL))
print('Population Std Dev: {} +- {} Ohms'.format(task1_std, task1_s))
print('\n')
print('Manufacturer Garuntee: {} +- {} Ohms'.format(1000, task1_mfg))
print('Max Level: {} +- {}'.format(task1_avg, 3*(task1_std + task1_s)))
print('\n')
print('Test for Significance')
print('-'*72)
print('Test\t\tt-value\t\tp-value\t\tPopulation Mean')
print('t\t', t_test_range(Task1, np.linspace(950, 1050, 101)))
print('Z\t', z_test_range(Task1, np.linspace(950, 1050, 101)))
print('\n\n')

print('Task 2 Values')
print('-'*72)
print('Mean Vin = {} +- {} V'.format(task2_avg0, task2_un0))
print('Population Mean: {} +- {} V'.format(task2_avg0, task2_CL0))
print('Population Std Dev: {} +- {} V'.format(task2_std0, task2_s0))
print('\n')
print('Mean Vout = {} +- {} V'.format(task2_avg1, task2_un1))
print('Population Mean: {} +- {} V'.format(task2_avg1, task2_CL1))
print('Population Std Dev: {} +- {} V'.format(task2_std1, task2_s1))
print('\n')
print('Mean Vout/Vin = {} +- {}'.format(task2_avg2, task2_un2))
print('Population Mean: {} +- {}'.format(task2_avg2, task2_CL2))
print('Population Std Dev: {} +- {}'.format(task2_std2, task2_s2))
print('\n')
print('Needed Output: {} +- {}'.format(task2_avg2, task2_mfg))
print('Max Level: {} +- {}'.format(task2_avg2, 3*(task2_std2 + task2_s2)))
print('\n')
print('Test for Significance')
print('-'*72)
print('Test\t\tt-value\t\tp-value\t\tPopulation Mean')
print('t\t', t_test_range(Task2[:, 2],
                   np.linspace(0.5*task2_avg0 - task2_mfg,
                               0.5*task2_avg0 + task2_mfg,
                               101)))
print('Z\t', z_test_range(Task2[:, 2],
                   np.linspace(0.5*task2_avg0 - task2_mfg,
                               0.5*task2_avg0 + task2_mfg,
                               101)))
print('\n\n')

print('Task 3 Values')
print('-'*72)
print('Mean Vin = {} +- {} V'.format(task3_avg0, task3_un0))
print('Population Mean: {} +- {} V'.format(task3_avg0, task3_CL0))
print('Population Std Dev: {} +- {} V'.format(task3_std0, task3_s0))
print('\n')
print('Mean Vout = {} +- {} V'.format(task3_avg1, task3_un1))
print('Population Mean: {} +- {} V'.format(task3_avg1, task3_CL1))
print('Population Std Dev: {} +- {} V'.format(task3_std1, task3_s1))
print('\n')
print('Mean Vout/Vin = {} +- {}'.format(task3_avg2, task3_un2))
print('Population Mean: {} +- {}'.format(task3_avg2, task3_CL2))
print('Population Std Dev: {} +- {}'.format(task3_std2, task3_s2))
print('\n')
print('Vout/Vin Needed: {} +- {}'.format(0, task3_mfg))
print('Max Level: {} +- {}'.format(task3_avg2, 3*(task3_std2 + task3_s2)))
print('\n')
print('Test for Significance')
print('-'*72)
print('Test\t\tt-value\t\tp-value\t\tPopulation Mean')
print('t\t', t_test_range(
      Task3[:, 2], np.linspace(0 - task3_mfg, 0 + task3_mfg, 101)))
print('Z\t', z_test_range(
      Task3[:, 2], np.linspace(0 - task3_mfg, 0 + task3_mfg, 101)))
print('..... Hypothesis Testing Complete')
print('\n')
tdelta = dt.datetime.now() - start
tmess = 'Time Taken: {}.....'.format(tdelta)
print(tmess)
print('\n\n')

print('Finding Outliers .....')
print('\n\n')
print('Outliers: Task1')
print('-'*72)
for x, y in outliers1:
    print('Resistance: {} Ohms, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task2 Vin')
print('-'*72)
for x, y in outliers20:
    print('Vin: {} V, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task2 Vout')
print('-'*72)
for x, y in outliers21:
    print('Vout: {} V, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task2 Vout/Vin')
print('-'*72)
for x, y in outliers22:
    print('Output: {}, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task3 Vin')
print('-'*72)
for x, y in outliers30:
    print('Vin: {} V, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task3 Vout')
print('-'*72)
for x, y in outliers31:
    print('Vout: {} V, Z: {}'.format(x, y))
print('\n\n')

print('Outliers: Task3 Vout/Vin')
print('-'*72)
for x, y in outliers32:
    print('Output: {}, Z: {}'.format(x, y))
print('..... Outliers Found')
print('\n')
tdelta = dt.datetime.now() - start
tmess = 'Time Taken: {}.....'.format(tdelta)
print(tmess)
print('\n\n')
end = dt.datetime.now()
total_timer = end - start
tmess = 'Total Time Taken: {}.....'.format(total_timer)
print('Program Complete on: {} .....'.format(tmess))
print('End Program')
