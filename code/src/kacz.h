#ifndef _KACZ_
#define _KACZ_

double* RK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* REK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RGS(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* NSSRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GSSRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_rand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_cyclic(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_sobol(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* REK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RGS_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* REK_max_it(int M, int N, double**& A, double*& b, double*& x, int max_it, int n_runs);

double* RGS_max_it(int M, int N, double**& A, double*& b, double*& x, int max_it, int n_runs);

double* NSSRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GSSRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* GRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_rand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_cyclic_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_rand_noshuffle_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_quasirand_sobol_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

double* RK_norep_quasirand_sobol_noshuffle_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs);

#endif