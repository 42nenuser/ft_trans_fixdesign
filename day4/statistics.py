def ft_statistics(*args: float, **kwargs: str) -> None:
    """
    Calculates statistics based on given numerical arguments (*args)
    and specified operations (**kwargs).

    Available operations:
    - "mean": Calculates the mean.
    - "median": Calculates the median.
    - "quartile": Calculates the 25th and 75th percentiles.
    - "std": Calculates the standard deviation.
    - "var": Calculates the variance.
    """
    try:
        # Validate input: Check if *args are all numbers
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("All positional arguments must be numbers.")

        # Ensure *args is not empty
        if not args:
            raise ValueError("No numerical arguments provided.")

        import numpy as np

        # Perform the required calculations based on **kwargs
        results = []
        for key, value in kwargs.items():
            if value == "mean":
                results.append(f"mean : {np.mean(args):.1f}")
            elif value == "median":
                results.append(f"median : {np.median(args):.1f}")
            elif value == "quartile":
                q25, q75 = np.percentile(args, [25, 75])
                results.append(f"quartile : [{q25:.1f}, {q75:.1f}]")
            elif value == "std":
                results.append(f"std : {np.std(args):.10f}")
            elif value == "var":
                results.append(f"var : {np.var(args):.10f}")
            else:
                # Handle unknown operation
                raise ValueError(f"Unknown operation: {value}")

        # Print results
        for result in results:
            print(result)
        if not results:
            print("ERROR")
    except Exception as e:
        print("ERROR")
        print(str(e))
