import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parameters
# -------------------------
N_bits = 10000
EbN0_dB_range = np.arange(0, 11, 2)

BER_AWGN = []
BER_Multipath = []

# -------------------------
# Simulation
# -------------------------
for EbN0_dB in EbN0_dB_range:

    bits = np.random.randint(0, 2, N_bits)

    # BPSK Mapping
    symbols = 2 * bits - 1

    EbN0 = 10**(EbN0_dB / 10)
    N0 = 1 / EbN0
    sigma = np.sqrt(N0 / 2)

    # -------------------------
    # AWGN
    # -------------------------
    noise_awgn = sigma * np.random.randn(N_bits)

    r_awgn = symbols + noise_awgn

    bits_hat_awgn = (r_awgn >= 0).astype(int)

    ber_awgn = np.mean(bits != bits_hat_awgn)

    BER_AWGN.append(ber_awgn)

    # -------------------------
    # Multipath + AWGN
    # -------------------------
    gain_direct = 1.0
    gain_reflected = 0.5

    received_signal = (
        gain_direct * symbols +
        gain_reflected * symbols
    )

    noise_multi = sigma * np.random.randn(N_bits)

    r_multi = received_signal + noise_multi

    bits_hat_multi = (r_multi >= 0).astype(int)

    ber_multi = np.mean(bits != bits_hat_multi)

    BER_Multipath.append(ber_multi)

    print(
        f"Eb/N0={EbN0_dB} dB | "
        f"BER(AWGN)={ber_awgn:.6f} | "
        f"BER(Multipath)={ber_multi:.6f}"
    )

# ==================================================
# PLOT 1 : AWGN
# ==================================================
plt.figure(figsize=(6,4))

plt.semilogy(
    EbN0_dB_range,
    BER_AWGN,
    'o-b',
    linewidth=2
)

plt.grid(True, which='both')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BPSK over AWGN')

# ==================================================
# PLOT 2 : Multipath + AWGN
# ==================================================
plt.figure(figsize=(6,4))

plt.semilogy(
    EbN0_dB_range,
    BER_Multipath,
    's-r',
    linewidth=2
)

plt.grid(True, which='both')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BPSK over Multipath + AWGN')

# ==================================================
# PLOT 3 : Comparison
# ==================================================
plt.figure(figsize=(6,4))

plt.semilogy(
    EbN0_dB_range,
    BER_AWGN,
    'o-b',
    linewidth=2,
    label='AWGN'
)

plt.semilogy(
    EbN0_dB_range,
    BER_Multipath,
    's-r',
    linewidth=2,
    label='Multipath + AWGN'
)

plt.grid(True, which='both')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.title('BER Comparison')
plt.legend()

plt.show()