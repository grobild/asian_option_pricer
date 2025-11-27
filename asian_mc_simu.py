import numpy as np

def path(N,T,S0,r,sigma):

    Z=np.random.normal(0,1,N)

    pas=T/N

    S=[S0]

    for i in range(N):
        x= S[-1]*np.exp((r-0.5*(sigma**2))*pas+sigma*np.sqrt(pas)*Z[i]) #using Black-Scholes fomrula of S(t+pas)=f(St)
        S.append(x)

    return np.array(S)

def asian_simu(M,N,T,K,S0,r,sigma):

    a=[]

    for i in range(M):
        a.append(np.mean(path(N,T,S0,r,sigma)))   # a is the array of the N means of the N path arrays

    payoff=[]

    for i in range(N):
        if a[i]-K>0:
            payoff.append(a[i]-K)
        else:
            payoff.append(0)      #payoff = max(mean(path)-K,0)

    return np.array(payoff)

def monte_carlo(M,N,T,K,S0,r,sigma):
    payoff=asian_simu(M,N,T,K,S0,r,sigma)
    return np.mean(payoff)*np.exp(-r*T)   # return the discounted mean of the payoff array to get our option price

print(monte_carlo(1000,1000,1,110,100,0.05,0.2))  #simulation with realistic parameters


