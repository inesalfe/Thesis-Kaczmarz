%% Setup

clc
clear

N_pixels = 128;
M = 19558;
N = 16384;
seed = 3;
it_gauss = 4470000;
it_poisson = 5060000;

%% RK Poisson

filename = "../../outputs/tomo_poisson_reg/RK_sol_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_poisson) + ".txt";
x_poisson = load(filename);

%% RK Gaussian

filename = "../../outputs/tomo_gauss_reg/RK_sol_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_gauss) + ".txt";
x_gauss = load(filename);

%% Original

filename = "../../../data/ct_gaussian/x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
fileID = fopen(filename);
x = fread(fileID,'double');

%% LS

filename = "../../../data/ct_gaussian/x_ls_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
fileID = fopen(filename);
x_ls = fread(fileID,'double');

%%

min_list = [min(x_poisson), min(x_gauss), min(x), min(x_ls)];
max_list = [max(x_poisson), max(x_gauss), max(x), max(x_ls)];

min_list = [min(x_poisson), min(x_gauss), min(x)];
max_list = [max(x_poisson), max(x_gauss), max(x)];

min_val = min(min_list);
max_val = min(max_list);

% min_val = -0.3;
% max_val = 1;

%%

figure1 = figure(1);
imagesc(reshape(x_poisson,N_pixels,N_pixels))
colorbar
% caxis manual
% caxis([min_val max_val])
filename_fig = "pdf_poisson/RK_poisson_x_reg_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_poisson) + ".pdf";
saveas(figure1,filename_fig);

figure2 = figure(2);
imagesc(reshape(x_gauss,N_pixels,N_pixels))
colorbar
% caxis manual
% caxis([min_val max_val])
filename_fig = "pdf_gauss/RK_gauss_x_reg_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_gauss) + ".pdf";
saveas(figure2,filename_fig);

% figure3 = figure(3);
% imagesc(reshape(x,N_pixels,N_pixels))
% colorbar
% caxis manual
% caxis([min_val max_val])
% filename_fig = "pdf_poisson/RK_original_x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_poisson) + ".pdf";
% saveas(figure3,filename_fig);
% filename_fig = "pdf_gauss/RK_original_x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + "_" + int2str(it_gauss) + ".pdf";
% saveas(figure3,filename_fig);

% figure4 = figure(4);
% imagesc(reshape(x,N_pixels,N_pixels))
% colorbar
% % caxis manual
% % caxis([min_val max_val])
% filename_fig = "pdf_poisson/RK_original_x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".pdf";
% saveas(figure4,filename_fig);
% filename_fig = "pdf_gauss/RK_original_x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".pdf";
% saveas(figure4,filename_fig);