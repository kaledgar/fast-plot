# fast-plot
Package of python functions to plot data with matplotlib.

# Why?

When you want:

![1](https://github.com/kkinastowski66/fast-plot/assets/101144906/fcaaeddd-8008-4039-91c0-6d2b24b1be88)

it's faster to do this:

```python
df_plot(df, 'x', 'y $m / \sqrt{ps}$', width = 8, height = 3, filename='graph.png')
```

than:

```python
columns_without_first = df.columns[1:]
fig, ax = plt.subplots()
for column in columns_without_first:
  ax.plot(df['x'], df[column], label=column)
fig.set_figwidth(width)
fig.set_figheight(height)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
if legend:
  ax.legend()
if grid:
  ax.grid(True, ls = '--')
if filename:
  plt.savefig(filename)

plt.show()
```
