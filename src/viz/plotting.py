import matplotlib.pyplot as plt


def plot_hists_diff_scales(df):

    fig, axes = plt.subplots(len(df.columns), 2, figsize=(14,28))
    for i, c in enumerate(df.columns):
        df[c].plot(kind='hist', bins=50, ax=axes[i, 0], title=c)
        df[c].plot(kind='hist', bins=50, ax=axes[i, 1],
                   title='%s (log scaled)' %c, logy=True)

    return fig, axes


def plot_hists_same_scale(df, title=''):

    fig, ax = plt.subplots(5, 2, sharex=True, sharey=True, figsize=(12,6))
    fig.suptitle(title, fontsize=14, y=1.08)
    df.plot(kind='hist', alpha=0.6, bins=50, subplots=True, ax=ax)
