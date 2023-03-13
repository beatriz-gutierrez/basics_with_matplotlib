import matplotlib.pyplot as plt


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
for temperature in df["temperature"].unique():
    df_temp = df[df["temperature"] == temperature]
    days = df_temp[df_temp["temperature"] == temperature]["days"].unique()
    df_median_dch = []
    df_median_dcir = []
    for dd in days:
        df_median_dch.append(df_temp[df_temp["days"] == dd]["Dch.Cap"].median(axis=0))
        df_median_dcir.append(df_temp[df_temp["days"] == dd]["10s"].median(axis=0))
    print(temperature)
    print("median dch:" + str((df_median_dch[-1] / df_median_dch[0]) * 100))
    print("median dcir:" + str((df_median_dcir[-1] / df_median_dcir[0]) * 100))
    ax1.plot( #last capa check
        days,
        (df_median_dch / df_median_dch[0]) * 100,
        label="B3 Sample T60",
        markerfacecolor="None",
        marker="o",
        linestyle="--",
    )
    ax1.grid(True, alpha=0.5)
    ax1.set_xlim([0, 600])
    ax1.set_ylim([70, 105])
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Capacity \%")
    ax1.legend()
    ax2.plot(# dcir
        days,
        (df_median_dcir / df_median_dcir[0]) * 100,
        markerfacecolor="None",
        marker="o",
        linestyle="--",
    )
    plt.ylabel("DCIR \%")
    plt.ylim([90, 185])
