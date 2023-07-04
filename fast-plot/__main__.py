from fastplot import fast_plot, df_plot
from constants import x, y, df, df_time_series

fast_plot(x, y, 'x', 'y [$m^2$]', 'data', filename = 'data')
df_plot(df, 'x', 'y $m / \sqrt{ps}$', filename='1')
