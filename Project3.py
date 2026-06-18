import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# PARAMETERS
# ---------------------------------------
N_bits = 10000
EbN0_dB_range = np.arange(0, 11, 2)

BER_AWGN = []
BER_Multipath = []

# ---------------------------------------
# MAIN LOOP
# ---------------------------------------
for EbN0_dB in EbN0_dB_range:

    # Generate random bits
    bits = np.random.randint(0, 2, N_bits)

    # BPSK Mapping
    # 0 -> -1
    # 1 -> +1
    symbols = 2 * bits - 1

    # Convert Eb/N0 from dB to linear
    EbN0 = 10**(EbN0_dB / 10)

    # Assume Eb = 1
    N0 = 1 / EbN0
    sigma = np.sqrt(N0 / 2)

    # =====================================
    # CASE 1 : AWGN CHANNEL
    # =====================================

    noise_awgn = sigma * np.random.randn(N_bits)

    r_awgn = symbols + noise_awgn

    bits_hat_awgn = (r_awgn >= 0).astype(int)

    ber_awgn = np.mean(bits != bits_hat_awgn)

    BER_AWGN.append(ber_awgn)

    # =====================================
    # CASE 2 : MULTIPATH + AWGN
    # =====================================

    # Two-path channel
    # Direct path = 1
    # Delayed path = 0.5

    h = np.array([1, 0.5])

    multipath_signal = np.convolve(
        symbols,
        h,
        mode='same'
    )

    noise_multi = sigma * np.random.randn(len(multipath_signal))

    r_multi = multipath_signal + noise_multi

    bits_hat_multi = (r_multi >= 0).astype(int)

    ber_multi = np.mean(bits != bits_hat_multi)

    BER_Multipath.append(ber_multi)

    print(
        f"Eb/N0={EbN0_dB} dB | "
        f"BER(AWGN)={ber_awgn:.5f} | "
        f"BER(Multipath)={ber_multi:.5f}"
    )

# =====================================
# GRAPH 1
# AWGN ONLY
# =====================================

plt.figure(figsize=(8,5))

plt.semilogy(
    EbN0_dB_range,
    BER_AWGN,
    'o-'
)

plt.grid(True, which='both')

plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")

plt.title("BPSK over AWGN Channel")

plt.show()

# =====================================
# GRAPH 2
# MULTIPATH + AWGN
# =====================================

plt.figure(figsize=(8,5))

plt.semilogy(
    EbN0_dB_range,
    BER_Multipath,
    's-r'
)

plt.grid(True, which='both')

plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")

plt.title("BPSK over Multipath + AWGN Channel")

plt.show()

# =====================================
# GRAPH 3
# COMPARISON
# =====================================

plt.figure(figsize=(8,5))

plt.semilogy(
    EbN0_dB_range,
    BER_AWGN,
    'o-',
    label='AWGN'
)

plt.semilogy(
    EbN0_dB_range,
    BER_Multipath,
    's-r',
    label='Multipath + AWGN'
)

plt.grid(True, which='both')

plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")

plt.title("BER Comparison")

plt.legend()

plt.show()