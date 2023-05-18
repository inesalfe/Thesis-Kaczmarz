function save_sparse_ct_poisson(N_pixels,theta,seed,intensity)

    [A,b,x] = paralleltomo(N_pixels,theta);

    x_init = x;
    
    % Build RHS and print matrix parameters

    M = size(A,1);
    N = size(A,2);

    fileID = fopen('ct_poisson/carac.txt','a+');

    fprintf(fileID, "N_pixels: %d\n", N_pixels);
    fprintf("N_pixels: %d\n", N_pixels);
    fprintf(fileID, "Angles: %d\n", size(theta,2));
    fprintf("Angles: %d\n", size(theta,2));

    fprintf(fileID, "M (pre deletion): %d\n", M);
    fprintf("M (pre deletion): %d\n", M);
    fprintf(fileID, "N (pre deletion): %d\n", N);
    fprintf("N (pre deletion): %d\n", N);

    % Delete rows of zeros

    idx = any(vecnorm(A,2,2) ~= 0, 2);
    b = b(idx,:);
    A = A(idx,:);

    M = size(A,1);
    N = size(A,2);

    % Error

    rng(seed);
    error = zeros(M,1);
    b_error = zeros(M,1);
    init_inten = intensity;
    for i=1:M
        poisson_var = init_inten*exp(-b(i));
        rand = poissrnd(poisson_var);
        while rand <= 0 || rand > init_inten
            rand = poissrnd(poisson_var);
        end
        error(i) = -log(rand/init_inten) - b(i);
        b_error(i) = -log(rand/init_inten);
    end

    % Indices of columns to be deleted

    logic_pixels = zeros(N,1);
    for i=1:M
        if b_error(i) == 0
            for j=1:N
                if full(A(i,j)) ~= 0
                    logic_pixels(j) = 1;
                end
            end
        end
    end
    idx_pixels = [];
    for j=1:N
        if logic_pixels(j) == 0
            idx_pixels(end+1) = j-1;
        end
    end
    
    % Delete cols

    idx = any(logic_pixels ~= 1, 2);
    A = A(:,idx);
    x = x(idx);
    N = size(A,2);

    % Delete rows with b values set to zero

    idx = any(vecnorm(A,2,2) ~= 0, 2);
    b = b(idx,:);
    b_error = b_error(idx,:);
    A = A(idx,:);
    M = size(A,1);

    fprintf(fileID, "M: %d\n", M);
    fprintf("M: %d\n", M);
    fprintf(fileID, "N: %d\n", N);
    fprintf("N: %d\n", N);
    fprintf(fileID, "Density: %f\n", nnz(A)/M/N);
    fprintf("Density: %f\n", nnz(A)/M/N);
    fprintf(fileID, "Residual: %f\n", norm(A*x-b));
    fprintf("Residual: %f\n", norm(A*x-b));

    fclose(fileID);

    x_ls = cgls(A,b_error,[],1E-18,10000);
    fprintf("CGLS solution compleated!\n");
    x_ls_reg = lsqlin(A,b_error,-eye(M,N),zeros(M,1));
    fprintf("Regularized solution compleated!\n");

    fileID_error = fopen('ct_poisson/error_details.txt','a+');

    fprintf("norm(A*x-b_error): %f\n", norm(A*x-b_error));
    fprintf("norm(A*x_ls-b_error): %f\n", norm(A*x_ls-b_error));
    fprintf("norm(A*x_ls_reg-b_error): %f\n", norm(A*x_ls_reg-b_error));
    fprintf("norm(x-x_ls): %f\n", norm(x-x_ls));
    fprintf("norm(error): %f\n", norm(error));

    fprintf(fileID_error, "norm(A*x-b_error): %f\n", norm(A*x-b_error));
    fprintf(fileID_error, "norm(A*x_ls-b_error): %f\n", norm(A*x_ls-b_error));
    fprintf(fileID_error, "norm(A*x_ls_reg-b_error): %f\n", norm(A*x_ls_reg-b_error));
    fprintf(fileID_error, "norm(x-x_ls): %f\n", norm(x-x_ls));
    fprintf(fileID_error, "norm(error): %f\n", norm(error));
    
    x_ls_full = zeros(1,N_pixels*N_pixels);
    for i=1:N
        x_ls_full(idx_pixels(i)+1) = x_ls(i);
    end
    
    x_ls_reg_full = zeros(1,N_pixels*N_pixels);
    for i=1:N
        x_ls_reg_full(idx_pixels(i)+1) = x_ls_reg(i);
    end
    
    max_pixel = max(max(x_init), max(x_ls));
    min_pixel = min(min(x_init), min(x_ls));

    figure_ls_reg = figure(3);
    imagesc(reshape(x_ls_reg_full,N_pixels,N_pixels))
    colorbar
    caxis manual
    caxis([min_pixel max_pixel])
    filename_fig = "ct_poisson/x_ls_reg_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".png";
    saveas(figure_ls_reg,filename_fig);
    
    figure_init = figure(2);
    imagesc(reshape(x_init,N_pixels,N_pixels))
    colorbar
    caxis manual
    caxis([min_pixel max_pixel])
    filename_fig = "ct_poisson/x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".png";
    saveas(figure_init,filename_fig);
    
    figure_ls = figure(1);
    imagesc(reshape(x_ls_full,N_pixels,N_pixels))
    colorbar
    caxis manual
    caxis([min_pixel max_pixel])
    filename_fig = "ct_poisson/x_ls_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".png";
    saveas(figure_ls,filename_fig);

    % Save

    % CSR

    NNZ = size(nonzeros(A),1);

    row_idx = zeros(M+1,1);
    row_idx(1) = 0;
    cols = zeros(NNZ,1);
    values = zeros(NNZ,1);

    counter = 0;
    element_per_row = 0;
    for i=1:M
        for j=1:N
            if A(i,j) ~= 0
                element_per_row = element_per_row + 1;
                counter = counter + 1;
                cols(counter,1) = j-1;
                values(counter,1) = A(i,j);
            end
        end
        row_idx(i+1) = row_idx(i) + element_per_row;
        element_per_row = 0;
    end

    filename_idx_pixels = "ct_poisson/idx_pixels_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_idx_pixels = fopen(filename_idx_pixels,'w');
    fwrite(file_idx_pixels, N_pixels*N_pixels, 'int');
    fwrite(file_idx_pixels, idx_pixels, 'int');
    fclose(file_idx_pixels);

    filename_logic_pixels = "ct_poisson/logic_pixels_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_logic_pixels = fopen(filename_logic_pixels,'w');
    fwrite(file_logic_pixels, N_pixels*N_pixels, 'int');
    fwrite(file_logic_pixels, logic_pixels, 'int');
    fclose(file_logic_pixels);
    
    filename_error = "ct_poisson/error_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_error = fopen(filename_error,'w');
    fwrite(file_error, error, 'double');
    fclose(file_error);

    filename_x = "ct_poisson/x_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_x = fopen(filename_x,'w');
    fwrite(file_x, x, 'double');
    fclose(file_x);

    filename_x_ls = "ct_poisson/x_ls_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_x_ls = fopen(filename_x_ls,'w');
    fwrite(file_x_ls, x_ls, 'double');
    fclose(file_x_ls);

    filename_x_ls_reg = "ct_poisson/x_ls_reg_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_x_ls_reg = fopen(filename_x_ls_reg,'w');
    fwrite(file_x_ls_reg, x_ls_reg, 'double');
    fclose(file_x_ls_reg);
    
    filename_b = "ct_poisson/b_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_b = fopen(filename_b,'w');
    fwrite(file_b, b, 'double');
    fclose(file_b);

    filename_b_error = "ct_poisson/b_error_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_b_error = fopen(filename_b_error,'w');
    fwrite(file_b_error, b_error, 'double');
    fclose(file_b_error);

    filename_row_idx = "ct_poisson/row_idx_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_row_idx = fopen(filename_row_idx,'w');
    fwrite(file_row_idx, row_idx, 'int');
    fclose(file_row_idx);

    filename_cols = "ct_poisson/cols_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_cols = fopen(filename_cols,'w');
    fwrite(file_cols, NNZ, 'int');
    fwrite(file_cols, cols, 'int');
    fclose(file_cols);

    filename_values = "ct_poisson/values_" + int2str(M) + "_" + int2str(N) + "_" + int2str(seed) + ".bin";
    file_values = fopen(filename_values,'w');
    fwrite(file_values, NNZ, 'int');
    fwrite(file_values, values, 'double');
    fclose(file_values);