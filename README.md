# CommLink-BPSK with Channel Impairment Analysis

## Project Overview

This project implements a Binary Phase Shift Keying (BPSK) communication system in Python and analyzes its performance under different channel conditions.

The project compares:

* AWGN (Additive White Gaussian Noise) Channel
* Multipath + AWGN Channel

Performance is evaluated using Bit Error Rate (BER) versus Eb/N0.

---

## Objectives

* Implement a complete BPSK communication system.
* Simulate transmission through an AWGN channel.
* Analyze the effect of a constructive multipath channel.
* Compare BER performance for different Eb/N0 values.
* Validate simulation results using theoretical BER expressions.

---

## System Model

### BPSK Mapping

0 → -1

1 → +1

### AWGN Channel

r = s + w

where:

* s = transmitted signal
* w = Gaussian noise

### Multipath Channel

r = g₁s + g₂s + w

where:

* g₁ = 1.0 (direct path)
* g₂ = 0.5 (secondary path)

The additional path increases received signal power and improves the effective SNR.

---

## Performance Metric

Bit Error Rate (BER)

BER = (Number of Error Bits) / (Total Transmitted Bits)

Simulation performed for Eb/N0 values from 0 dB to 10 dB.

---

## Technologies Used

* Python
* NumPy
* Matplotlib

---

## Results

* BER decreases as Eb/N0 increases.
* Multipath + AWGN channel achieves lower BER than the AWGN channel.
* Constructive path combining provides approximately 3.52 dB signal power gain.
* Improved SNR results in better communication reliability.

---

## How to Run

Install required packages:

pip install numpy matplotlib

Run:

python Project3.py

---

## Author

Communication Systems Project

BPSK Channel Impairment Analysis using Python
