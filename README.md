# fast-plot
Script that allows to plot data from arrays and dataframes with matplotlib in **one** line of code. 

# Why?

Let me give you an example:

<details>
<summary>Spoiler warning</summary>

When you want:
        
![Figure_1](https://github.com/kkinastowski66/fast-plot/assets/101144906/9dcf1828-035a-45d7-bda8-574f7a7d53c2)

        
In 99% of the situations when I don't want to modify every matplotlib object I prefer to do this:
        
```python
df_plot(df,
        'X [$m$]',
        'Effective value $[ m^3 / s^{11}]$',
        width = 8,
        height = 3,
        filename='figure.png',
        regression = True,
        xtics = range(0, 22, 2)
        )
```
        
than this atrocity: 

```python
    columns_without_first = df.columns[1:]
    fig, ax = plt.subplots()

    if regression:
        regression_model = LinearRegression()
        x = df['x'].values.reshape(-1, 1)

    for column in columns_without_first:
        y = df[column].values.reshape(-1, 1)

        if regression:
            regression_model.fit(x, y)
            y_pred = regression_model.predict(x)
            ax.scatter(df['x'], df[column], label=column)
            ax.plot(df['x'], y_pred, '--', label=None)
        else:
            ax.plot(df['x'], df[column], 'o-', label=column)

    fig.set_figwidth(width)
    fig.set_figheight(height)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if xtics:
        plt.xticks(xtics)
    if legend:
        ax.legend()
    if grid:
        ax.grid(True, ls='--')
    if xlimit:
        plt.xlim(xlimit)
    if ylimit:
        plt.ylim(ylimit)
    if filename:
        plt.savefig(filename)
    plt.show()
```
</details>

## Requirements:

```
pandas~=1.4.4
matplotlib~=3.5.2
numpy~=1.21.5
sklearn~=1.3.0
```
