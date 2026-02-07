🚨 SafeDose: Tylenol Pediatric Calculator
Project Overview

SafeDose is a specialized clinical tool designed to provide accurate acetaminophen (Tylenol) dosing recommendations for pediatric patients. Developed with a "Safety-First" architecture, the app prioritizes weight-based dosing (15mg/kg) over age-based estimates and incorporates strict data-validation guardrails to prevent common medication errors.

Key Features

Weight-Based Precision: Calculates dosage using the 15mg/kg clinical standard for Children's Liquid Tylenol (160mg/5mL).

Safety "Hard Stop" Logic: Utilizing CDC/WHO growth percentile data, the app cross-references the entered weight against the patient's age. If a significant mismatch is detected (suggesting a lbs/kg swap or data entry error), the app refuses to calculate a dose and directs the user to a physician.

Practical Dosing: Rounds outputs to the nearest 1.25mL increment to align with standard pediatric oral syringe markings, reducing measuring errors by caregivers.

Clinical Guardrails: Automatically caps pediatric doses at the standard adult maximum (650mg) to ensure safety for older/larger children.

Challenges & Technical Iterations

Clinical Fail-Safes: A primary challenge was addressing the "distracted user" risk. Early iterations used "Soft Warnings" for improbable weights, but user testing (logic-based) suggested that providing a dosage number alongside a warning was a safety risk. The current version uses a Hard Stop to force data re-entry.

Environment Management: Navigating macOS's "Externally Managed Environment" (PEP 668) required the implementation of a Python Virtual Environment (venv) to ensure stable dependency management and deployment.

UI/UX for High-Stress Situations: The interface was designed for simplicity, recognizing that caregivers using this app may be in high-stress situations (treating a febrile child).

Technical Stack

Language: Python 3.14

Framework: Streamlit

Deployment: Streamlit Cloud / GitHub

Data Source: CDC Growth Chart LMS Parameters (Simplified for Logic Bounds)

Disclaimer

This application is for educational purposes only. Always consult with a healthcare professional before administering medication. Do not exceed 5 doses in a 24-hour period.
