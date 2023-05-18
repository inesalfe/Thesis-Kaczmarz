%% Reset

clc;
clear;

addpath('AIRToolsII/')
AIRToolsII_setup('temporary')

%% Save

N = 128;
theta_inc = 1.5;
theta = 0:theta_inc:178.5;

seed = 1;
eta = 0.001;
save_sparse_ct_gaussian(N,theta,seed,eta);

seed = 2;
eta = 0.002;
save_sparse_ct_gaussian(N,theta,seed,eta);

seed = 3;
eta = 0.004;
save_sparse_ct_gaussian(N,theta,seed,eta);

seed = 4;
eta = 0.008;
save_sparse_ct_gaussian(N,theta,seed,eta);