from enum import Enum


class PlottingBackend(str, Enum):
    _plotly_plot = "plotly"
    _matplotlib_plot = "matplotlib"

    @classmethod
    def _missing_(cls, value):
        if value == "pyplot":
            return cls._matplotlib_plot

        raise ValueError(f"Invalid plotting backend: {value}")


if __name__ == "__main__":
    backend = PlottingBackend("pyplot")

    print(backend)
    # <PlottingBackend._matplotlib_plot: 'matplotlib'>

    print(backend.name)
    # '_matplotlib_plot'

    print(backend.value)
    # getattr(cls, backend.name)(...)
