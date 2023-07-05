from fastplot import fast_plot, df_plot
from constants import x, y, df, df_time_series


df_plot(df,
        r'$ \tau $ [ps]',
        'Max. Ablation Efficiency $[ mm^3 / (W \cdot min)]$',
        width = 8,
        height = 6,
        ylimit = (.15, .45),
        filename='figure1.png',
        regression = True,
        )
