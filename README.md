# OpenQuantumBattery 🔋

A visual and educational open-source simulator for **quantum batteries**.

## Current MVP

The first version provides an interactive two-level quantum battery with:

- battery frequency $\omega_0$;
- charging strength $\Omega$;
- phase $\phi$;
- phenomenological dephasing $\gamma$;
- stored energy;
- charging power;
- coherence;
- Ramsey-interferometer visibility;
- interactive parameter exploration.

## Run locally

```bash
git clone https://github.com/YOUR-USERNAME/openquantumbattery.git
cd openquantumbattery

python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate        # Windows

pip install -r requirements.txt
streamlit run app.py
```

The application will open in the browser.

## Scientific roadmap

### Phase 1 — Two-level quantum battery
- unitary charging
- stored energy
- charging power
- coherence

### Phase 2 — Open quantum battery
- Lindblad master equation
- relaxation
- dephasing
- thermal environments

### Phase 3 — Quantum thermodynamics
- ergotropy
- passive states
- extractable work
- charging efficiency

### Phase 4 — Ramsey quantum battery
- ancilla qubit
- first $\pi/2$ pulse
- ancilla–battery interaction
- second $\pi/2$ pulse
- Ramsey fringes
- visibility

### Phase 5 — Many-body batteries
- parallel charging
- collective charging
- Dicke-type models
- quantum advantage metrics

## License

MIT License.
