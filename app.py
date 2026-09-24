import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="OpenQuantumBattery",
    page_icon="🔋",
    layout="wide",
)

st.title("🔋 Quantum Battery Simulator")
st.caption("OpenQuantumBattery — an open-source educational simulator for quantum energy storage.")

# ---------- Sidebar ----------
st.sidebar.header("Battery parameters")

omega = st.sidebar.slider(
    r"Battery frequency $\omega_0$",
    min_value=0.1, max_value=5.0, value=1.0, step=0.1
)
Omega = st.sidebar.slider(
    r"Charging strength $\Omega$",
    min_value=0.0, max_value=5.0, value=1.0, step=0.1
)
phi = st.sidebar.slider(
    r"Phase $\phi$",
    min_value=0.0, max_value=2*np.pi, value=0.0, step=0.1
)
gamma = st.sidebar.slider(
    r"Dephasing rate $\gamma$",
    min_value=0.0, max_value=1.0, value=0.0, step=0.01
)
tmax = st.sidebar.slider(
    "Simulation time",
    min_value=1.0, max_value=30.0, value=10.0, step=1.0
)

protocol = st.sidebar.selectbox(
    "Charging protocol",
    ["Rabi charging", "Ramsey interferometer"]
)

N = 1000
t = np.linspace(0, tmax, N)

# ---------- Simple two-level model ----------
# H_B = omega/2 sigma_z
# Rabi population transfer: P_e(t) = sin^2(Omega t / 2)
# Add phenomenological dephasing envelope exp(-gamma t).
coherence = np.exp(-gamma * t) * np.abs(np.sin(Omega * t / 2))
population = np.exp(-gamma * t) * np.sin(Omega * t / 2)**2
energy = omega * population
power = np.gradient(energy, t)

# Ergotropy for this simple pure-state-inspired educational model.
ergotropy = np.maximum(energy - omega * np.minimum(population, 1-population), 0)

# Ramsey signal
ramsey_phase = np.linspace(0, 2*np.pi, 400)
visibility = np.exp(-gamma * tmax / 2)
ramsey_signal = 0.5 * (1 + visibility * np.cos(ramsey_phase + phi))

# ---------- Metrics ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Maximum energy", f"{energy.max():.3f}")
c2.metric("Maximum power", f"{power.max():.3f}")
c3.metric("Final coherence", f"{coherence[-1]:.3f}")
c4.metric("Ramsey visibility", f"{visibility:.3f}")

st.divider()

# ---------- Main plots ----------
left, right = st.columns(2)

with left:
    st.subheader("Battery charging dynamics")
    fig, ax = plt.subplots()
    ax.plot(t, energy, label="Stored energy")
    ax.plot(t, power, label="Power", alpha=0.75)
    ax.set_xlabel("Time")
    ax.set_ylabel("Energy / Power")
    ax.grid(alpha=0.25)
    ax.legend()
    st.pyplot(fig, clear_figure=True)

with right:
    st.subheader("Quantum coherence")
    fig, ax = plt.subplots()
    ax.plot(t, coherence, label=r"$C_{l_1}$")
    ax.set_xlabel("Time")
    ax.set_ylabel("Coherence")
    ax.set_ylim(bottom=0)
    ax.grid(alpha=0.25)
    ax.legend()
    st.pyplot(fig, clear_figure=True)

if protocol == "Ramsey interferometer":
    st.divider()
    st.subheader("Ramsey interferometer")

    st.markdown(
        r"""
        The Ramsey protocol is represented schematically as
        \[
        \pi/2 \;\longrightarrow\; \text{battery interaction}
        \;\longrightarrow\; \pi/2 \;\longrightarrow\; \text{measurement}.
        \]
        """
    )

    fig, ax = plt.subplots()
    ax.plot(ramsey_phase, ramsey_signal)
    ax.set_xlabel(r"Ramsey phase $\varphi$")
    ax.set_ylabel(r"$P_e(\varphi)$")
    ax.set_ylim(0, 1)
    ax.grid(alpha=0.25)
    st.pyplot(fig, clear_figure=True)

    st.info(
        f"Estimated Ramsey visibility: **{visibility:.3f}**. "
        "Increase the dephasing rate γ to observe loss of interference contrast."
    )

st.divider()

with st.expander("Model used in this MVP"):
    st.latex(r"H_B = \frac{\hbar\omega_0}{2}\sigma_z")
    st.latex(r"H_{\mathrm{int}} = \frac{\hbar\Omega}{2}
              (\cos\phi\,\sigma_x+\sin\phi\,\sigma_y)")
    st.markdown(
        """
        This first interface is intentionally lightweight. It is an educational
        MVP rather than a full open-quantum-system solver. The next version can
        replace the phenomenological dynamics with a Lindblad/QuTiP backend,
        add explicit ancilla–battery coupling, and implement collective batteries.
        """
    )

st.caption("OpenQuantumBattery • MIT License • GitHub-ready MVP")
