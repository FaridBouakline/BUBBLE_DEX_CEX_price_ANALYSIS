import numpy as np
from scipy import stats
from functools import partial

def rolling_window(a, window):
    ''' use of rolling method without pandas module
    :param a Input 1d Numpy array
    :param window : Size of the rolling window'''
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def apply_rolling_function(arr, window_size, func, *args, **kwargs):
    """
    Apply a custom function with parameters to rolling windows of a NumPy array.
    
    :param arr: Input 1D NumPy array
    :param window_size: Size of the rolling window
    :param func: Custom function to apply to each window
    :param *args: Positional arguments to pass to the custom function
    :param **kwargs: Keyword arguments to pass to the custom function
    :return: NumPy array with the rolling function applied
    """
    if hasattr(np.lib.stride_tricks, 'sliding_window_view'):
        # For NumPy 1.20+
        windows = np.lib.stride_tricks.sliding_window_view(arr, window_size)
    else:
        # For older NumPy versions
        windows = rolling_window(arr, window_size)
    
    # Use partial to create a new function with the additional parameters
    parameterized_func = partial(func, *args, **kwargs)
    
    return np.array([parameterized_func(window) for window in windows])




def hurst_chan(p, l):
    """
    Arguments:
        p: ndarray -- the price series to be tested
        l: list of integers or an integer -- lag(s) to test for mean reversion
    Returns:
        Hurst exponent
    """
    if isinstance(l, int):
        lags = [1, l]
    else:
        lags = l
    assert lags[-1] >=2, "Lag in prices must be greater or equal 2"
    #print(f"Price lags of {lags[1:]} are included")
    lp = np.log(p)
    var = [np.var(lp[l:] - lp[:-l]) for l in lags]

    hr = stats.linregress(np.log(lags), np.log(var))[0] / 2
    return hr

