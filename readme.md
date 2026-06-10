You are an expert Python developer and AI/ML engineer specializing in Artificial Neural Networks (ANN/JST). I need you to help me build a complete final exam project called "The Zen-Day Optimizer" for my university course on Neural Networks (JST).

## PROJECT OVERVIEW
Build a Python-based daily assistant application that solves real-life daily problems using at least TWO ANN models learned in class. The app must feel like a real, usable application.

## MANDATORY REQUIREMENTS
1. Use **Python** as the primary language
2. Implement **at least 2 ANN models** from the list below:
   - Linear Classification: M-P, Hebbian, Perceptron, Adaline
   - Non-Linear/Complex: Madaline, Backpropagation, Radial Basis Function (RBF)
   - Unsupervised/Clustering: Kohonen (SOM), Learning Vector Quantization (LVQ), Counter Propagation
   - Associative Memory: Hopfield Network
3. Build models **from scratch using NumPy** (no sklearn, no keras, no tensorflow for the core ANN logic)
4. Use **Streamlit** for the user interface/dashboard
5. Use **Matplotlib or Seaborn** to visualize the MSE/error curve during training
6. Every section of code **must have detailed comments** explaining what it does, its input, expected output, and how it works

## GRADING CRITERIA (build with these in mind)
- Creativity of Solution (20%): Make the problem unique and interesting
- Code Quality (30%): Clean code, proper NumPy usage, correct algorithm logic
- Mathematical Analysis (30%): Clearly show weight update formulas, error signal, forward & backward pass logic in code comments
- Presentation & Demo (20%): App must handle real-time new input data

## WHAT TO BUILD
Choose a creative daily-life problem (NOT the exact sleep/coffee example from the slides — be original). Good ideas include things like:
- Social battery predictor for introverts
- Burnout early warning system
- Study session optimizer
- Focus zone recommender
- Mood-based music genre classifier

Then implement:
1. **Model 1**: Choose the most appropriate ANN for classification or pattern recognition
2. **Model 2**: Choose a second ANN for clustering, regression, or associative memory
3. **Streamlit UI**: Sidebar inputs, real-time prediction display, result visualization
4. **MSE/Error curve chart**: Show training convergence using Matplotlib
5. **Parameter comparison**: Show results when learning rate (η) is changed (e.g., 0.01 vs 0.1 vs 0.5)

## CODE STRUCTURE REQUIRED
Organize the code in this order:
1. Imports and library setup (with install instructions in comments)
2. ANN Model 1 class — built from scratch with NumPy, fully commented
3. ANN Model 2 class — built from scratch with NumPy, fully commented
4. Training data and normalization logic
5. Streamlit UI layout (sidebar inputs, main panel results)
6. Training execution with @st.cache_resource
7. Prediction logic with normalization bridge
8. Visualization (MSE curve + any clustering/result chart)
9. Mathematical explanation in comments: show the weight update formula for each model

## ACADEMIC DOCUMENTATION FORMAT (include as docstrings/comments)
The code comments must cover:
- Bab I equivalent: Why this daily problem matters
- Bab II equivalent: Architecture — number of input/hidden/output neurons, activation function used
- Bab III equivalent: One full manual iteration example (Forward + Backward pass with numbers)
- Bab IV equivalent: How changing learning rate or epoch count affects accuracy
- Bab V equivalent: Whether the model successfully solves the problem

## OUTPUT FORMAT
Provide:
1. The complete `app.py` file — fully working, copy-paste ready
2. A `requirements.txt` with all needed libraries
3. Step-by-step run instructions
4. A brief mathematical explanation (in Bahasa Indonesia) for Bab III of the report, showing one manual forward + backward propagation iteration with example numbers

Start by proposing a creative app concept with the two ANN models you'll use and why, then build the full implementation.