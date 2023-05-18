#ifndef _KACZ_CSR_
#define _KACZ_CSR_

double* RK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* REK_csr_csc(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RGS_csr_csc(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* NSSRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GSSRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_rand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_cyclic_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_sobol_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* REK_csr_csc_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RGS_csr_csc_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* NSSRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GSSRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_rand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_cyclic_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_sobol_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

#endif