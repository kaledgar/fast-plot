from fastplot import fast_plot, df_plot
from constants import x, y, df, df_time_series


df_plot(df,
        'X [$m$]',
        'Effective value $[ m^3 / s^{11}]$',
        width = 8,
        height = 3,
        filename='figure.png',
        regression = True,
        xtics = range(0, 22, 2)
        )
