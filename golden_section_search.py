import math

def objective_function(x):
    return math.exp(-x)+x*x
    #return 2*x*x-x-1

def solution(alpha,epsilon,a_1,b_1):
    lambda_1 = a_1 + (1-alpha)*(b_1 - a_1)
    mu_1     = a_1 + alpha*(b_1 - a_1)
    phi_lambda = objective_function(lambda_1)
    phi_mu     = objective_function(mu_1)
    a_k = a_1
    b_k = b_1
    lambda_k = lambda_1
    mu_k     = mu_1
    k = 1
    #markdown table format
    print('| %10s | %10s | %10s | %10s | %10s | %10s | %10s |'%("k".center(10),"a_k".center(10),"b_k".center(10),
              "lambda_k".center(10),"mu_k".center(10),"phi_lambda".center(10),"phi_mu".center(10)))
    print('|:-:|:-:|:-:|:-:|:-:|:-:|:-:|')
    print('|%-6d | %-f | %-f | %-f | %-f | %-f | %-f |'%(k,a_k,b_k,lambda_k,mu_k,phi_lambda,phi_mu))
    while (b_k - a_k) >= epsilon :
        if phi_lambda <= phi_mu :
           a_k_1 = a_k
           b_k_1 = mu_k
           mu_k_1 = lambda_k
           phi_mu = phi_lambda
           # lambda_k_1 = a_k_1 + (b_k_1 - mu_k_1)
           lambda_k_1 = a_k_1 + (1-alpha)*(b_k_1 - a_k_1)
           phi_lambda = objective_function(lambda_k_1)
        else :
            a_k_1 = lambda_k
            b_k_1 = b_k
            lambda_k_1 = mu_k
            phi_lambda = phi_mu
            # mu_k_1 = b_k_1 - (lambda_k_1 - a_k_1)
            mu_k_1 = a_k_1 + alpha*(b_k_1 - a_k_1)
            phi_mu = objective_function(mu_k_1)
        
        
        lambda_k = lambda_k_1
        mu_k     = mu_k_1
        a_k = a_k_1
        b_k = b_k_1
        k = k + 1
        print('| %-6d | %-f | %-f | %-f | %-f | %-f | %-f |'%(k,a_k,b_k,lambda_k,mu_k,phi_lambda,phi_mu))
    print('the best solution is %5f'%((a_k+b_k)/2))
solution(0.618,1e-4,0,1)
solution((math.sqrt(5)-1)/2,1e-4,0,1)
