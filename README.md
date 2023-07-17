# function-plotter

## Application introduction
Mathematical functions plotter python application implemented using following libraries numpy, pyside2 and matplotlib. pytest and pytest-qt are also used for testing. The application has 3 inputs the function equation and the max and min values, then if the function and its range both are valid the plot of the equation will appear if not an error message will appaer.

## Application requirments
```bash
pip install numpy
pip install PySide2
pip install matplotlib
```

## Testing requirments
```bash
pip install pytest
pip install pytest-qt
```

## Application guide
- To use the app execute the following command in your terminal
```bash
python plot.py
```
- To run automated tests execute the following command in your terminal
```bash
pytest test_app.py
```
