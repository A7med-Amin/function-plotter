import pytest
import plot

@pytest.fixture
def plot(qtbot):
    plot_test = plot.ApplicationWindow()
    qtbot.addWidget(plot_test)

    return plot_test

def test_labels(app):
    assert app.label1.text() == "Please enter your equation"
    assert app.label2.text() == "Please enter the min value"
    assert app.label3.text() == "Please enter the max value"

