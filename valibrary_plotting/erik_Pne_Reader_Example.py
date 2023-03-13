import matplotlib.pyplot as plt

pnlreader = PnlReader(project="PORSCHE", batch="B2S2")

dcir = pnlreader.read_dcir()
capacity = pnlreader.read_capacity()

dcir = dcir.loc[dcir.step_type.isin(["CHARGE", "DISCHARGE"])]
capacity = capacity.loc[capacity.step_type.isin(["CHARGE", "DISCHARGE"])]

step_no_dcir = (
    dcir.groupby(["p_project", "p_batch", "p_cell", "cycle"]).step_no.max().unique()
)

data = dcir.loc[dcir.step_no.isin(step_no_dcir)].join(
    capacity.loc[(capacity.label == "CAPACITYCHECK")]
    .rename(columns={"cycle_count": "cycle"})
    .set_index(["p_project", "p_batch", "p_cell", "cycle"]),
    on=["p_project", "p_batch", "p_cell", "cycle"],
    how="inner",
    rsuffix="_capacity",
)

data2 = data.set_index(
    [
        "p_batch",
        "p_cell",
        "step_type",
        "cycle",
        "step_time_millis",
    ]
)


fig, ax = plt.subplots()
ax2 = ax.twinx()
for cell, magic in data2.groupby(["p_batch", "p_cell"]):
    cap = magic.groupby(
        ["p_project", "p_batch", "p_cell", "cycle"]
    ).step_amp_hours_capacity.tail(1)
    dcirdata = magic.xs(("CHARGE", 10000.0), level=["step_type", "step_time_millis"])
    avg = dcirdata.groupby("cycle").instant_dcir.mean()
    ax.scatter(cap.index.get_level_values("cycle"), cap, label=cell)
    ax2.scatter(avg.index, avg, marker="s", label=cell)
ax.legend()
ax.set_xlabel("cycles")
ax.set_ylabel("capacity (Ah)")
ax2.set_ylabel("DCIR")
plt.show()
