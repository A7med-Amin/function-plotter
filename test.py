import pytest
import plot

@pytest.fixture
def plot(par):
    plot_test = plot.ApplicationWindow()
    par.addWidget(plot_test)

    return plot_test

#    Test the labels
def labels_testing(app):
    assert app.label1.text() == "Please enter your equation"
    assert app.label2.text() == "Please enter the min value"
    assert app.label3.text() == "Please enter the max value"

#    Test the Equation textfield
@pytest.mark.parametrize("value, isvalid", [
    ('x)3', False), ( '2*x^2 + 4*x + 12', True), ('x^2 & x|2', False), 
    ('x*z', False), ('y+16', False), ('z^2 +5 +4', False), 
    ('x+2', True), ('x^2 + 2*x + 9 -', False), ('', False), 
])
def equation_testing(app, value, isvalid):
    app.textfield1.setText(value)
    assert app.equation_check() == isvalid

#    Test the min-value textfield
@pytest.mark.parametrize("value, isvalid", [
    ('-10' , True ) , ('0', True ), ('4' , True ),
    ('10', True), ('20.5' , True), ('min', False),
    ('' , False), ('^' , False) , ('-' , False)
])
def min_val_testing(app, value, isvalid):
    app.textfield2.setText(value)
    assert app.minimum_check() == isvalid

#    Test the max-value textfield
@pytest.mark.parametrize("value, isvalid", [
    ('-10' , True ) , ('0', True ), ('4' , True ),
    ('10', True), ('20.5' , True), ('min', False),
    ('' , False), ('^' , False) , ('-' , False)
])
def max_val_testing(app, value, isvalid):
    app.textfield3.setText(value)
    assert app.maximum_check() == isvalid
