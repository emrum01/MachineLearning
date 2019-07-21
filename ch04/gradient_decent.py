 def numerical_gradient(f,x):
      h = le-4
      grad = np.zeros_like(x.size)

      for idx in range(x.size):
          tmp_val = x[idx]
          x[idx] = tmp_val + h
          