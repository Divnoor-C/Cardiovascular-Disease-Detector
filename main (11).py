"""
main code to run the prediction
"""
from __future__ import annotations
import tkinter as tk
from project_2_code import QuestionnaireApp
from visual import DataVisualizer


def run_code() -> None:
    """
    Runs the code, including GUI, Visuals, and our model to get the repsonse and interactive experience
    """
    mainroot = tk.Tk()
    app = QuestionnaireApp(mainroot, "cardio_train.csv")
    mainroot.geometry('750x750')
    mainroot.mainloop()
    app_responses = app.get_responses()
    if app_responses:
        data_visualizer = DataVisualizer(app)
        data_visualizer.create_bar_graph(app_responses)
        data_visualizer.create_pie_charts(app_responses)


if __name__ == "__main__":
    run_code()
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'max_instance_attributes': 100,
        'extra-imports': ['hashlib', 'tkinter', 'project_2_code', 'visual'],
        'allowed-io': ['feature_importance']
    })
