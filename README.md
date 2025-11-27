# 🔱 Monte Carlo Arithmetic Asian Option Simulator

## 🚀 Overview

This repository contains a robust Python implementation of a **Monte Carlo simulator** used to price **Arithmetic Average Asian Options**.

Unlike standard European options, Asian options (which depend on the average price of the underlying asset over the option's life) generally lack a simple, closed-form analytical solution like the Black-Scholes formula. Therefore, Monte Carlo simulation is the industry standard for obtaining the theoretical "fair value" of these exotic derivatives.

The simulator uses the **Geometric Brownian Motion (GBM)** model under the **risk-neutral measure** to generate multiple independent price paths for the underlying asset.

## 📊 Methodology

The pricing engine is built on two core financial and mathematical concepts:

### 1. Geometric Brownian Motion (GBM)
The path of the underlying asset price ($S_t$) is modeled by the following discrete-time step equation:

$$
S_{t+\Delta t} = S_t \exp\left( (r - \frac{1}{2}\sigma^2) \Delta t + \sigma \sqrt{\Delta t} \epsilon \right)
$$

Where:
* $r$ is the **risk-free rate**.
* $\sigma$ is the **volatility** of the asset.
* $\Delta t$ is the time increment.
* $\epsilon$ is a random variable drawn from the standard normal distribution ($\epsilon \sim N(0, 1)$).

### 2. Option Payoff Calculation
For each simulated path $i$, the final price is determined by the Arithmetic Average of the discrete monitoring points ($S_{t_j}$):

$$
A_T = \frac{1}{N_{steps}} \sum_{j=1}^{N_{steps}} S_{t_j}
$$

The payoff for a **Call Option** is $\max(A_T - K, 0)$ and for a **Put Option** is $\max(K - A_T, 0)$.

The final option price ($C_0$) is the average of all discounted payoffs:

$$
C_0 = e^{-rT} \cdot \left( \frac{1}{N_{paths}} \sum_{i=1}^{N_{paths}} \text{Payoff}_i \right)
$$

## 🛠️ Prerequisites

To run the simulator, you need the following Python libraries:

```bash
pip install numpy pandas scipy

git clone https://github.com/grobild/asian_option_pricer/
cd asian_option_pricer

python asian_mc_simu.py
