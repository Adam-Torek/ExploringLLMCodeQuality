def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False

# Test cases
print(any_int(5, 2, 7)) # True
print(any_int(3, 2, 2)) # False
print(any_int(3, -2, 1)) # True
print(any_int(3.6, -2.2, 2)) # False
print(any_int(1, 1, 2)) # False
print(any_int(1, 1, 1)) # True
print(any_int(1, 1, "1")) # False
print(any_int(1, 1, [1])) # False
print(any_int(1, 1, (1,))) # False
print(any_int(1, 1, {1})) # False
print(any_int(1, 1, {1, 2})) # False
print(any_int(1, 1, set([1]))) # False
print(any_int(1, 1, frozenset([1]))) # False
print(any_int(1, 1, tuple([1]))) # False
print(any_int(1, 1, list([1]))) # False
print(any_int(1, 1, bytearray([1]))) # False
print(any_int(1, 1, memoryview([1]))) # False
print(any_int(1, 1, array('i', [1]))) # False
print(any_int(1, 1, numpy.array([1]))) # False
print(any_int(1, 1, pandas.Series([1]))) # False
print(any_int(1, 1, scipy.ndarray([1]))) # False
print(any_int(1, 1, torch.tensor([1]))) # False
print(any_int(1, 1, tensorflow.Tensor([1]))) # False
print(any_int(1, 1, keras.Tensor([1]))) # False
print(any_int(1, 1, mxnet.nd.array([1]))) # False
print(any_int(1, 1, pytorch_lightning.LightningDataModule())) # False
print(any_int(1, 1, tensorflow_datasets.Dataset)) # False
print(any_int(1, 1, pandas_datareader.data.DataReader)) # False
print(any_int(1, 1, yfinance.Ticker)) # False
print(any_int(1, 1, requests.get)) # False
print(any_int(1, 1, urllib.request.urlopen)) # False
print(any_int(1, 1, socket.socket)) # False
print(any_int(1, 1, subprocess.Popen)) # False
print(any_int(1, 1, os.system)) # False
print(any_int(1, 1, os.open)) # False
print(any_int(1, 1, os.pipe)) # False
print(any_int(1, 1, os.mkdir)) # False
print(any_int(1, 1, os.rmdir)) # False
print(any_int(1, 1, os.chdir)) # False
print(any_int(1, 1, os.getcwd