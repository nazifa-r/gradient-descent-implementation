# gradient descent visualizations (1d, 2d, 3d)

this is a simple learning project i built while studying gradient descent in my numerical methods course and starting my machine learning journey.
the goal was to understand gradient descent visually by implementing it from scratch using numpy and matplotlib.

---

## what this project does

this project demonstrates gradient descent on different functions:

### 1d gradient descent
- function: f(x) = x^2  
- shows convergence to minimum at x = 0

### 2d gradient descent
- function: f(x, y) = x^2 + y^2  
- shows convergence to global minimum at (0, 0)
- includes contour plot (heatmap)  
- includes optimization trail showing the path taken by gradient descent

### 3d gradient descent (sinusoidal surface)
- function: (sin5x * cos5x) / 5
- shows optimization on a non-convex surface


---

## visualizations

### 1d gradient descent
![1d gradient descent](https://i.imgur.com/GYZNXX4.png)

### 2d gradient descent
![2d gradient descent](https://i.imgur.com/tKSj9br.png)

### 3d gradient descent
![3d gradient descent](https://i.imgur.com/6PaMxbN.png)

---

## what i learned

- how gradient descent updates parameters step by step
- how derivatives guide optimization
- effect of learning rate on convergence
- difference between convex and non-convex functions
- how optimization behaves in higher dimensions
- how to implement math concepts in python

---

## project structure

```bash id="w0kq9s"
project-folder/
│
├── main1d.py
├── main2d.py
├── main3d.py
├── README.md
└── images/ (optional if you used local images)
