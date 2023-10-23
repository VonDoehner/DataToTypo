import tkinter as tk

def on_drag_start(event):
    widget = event.widget
    widget.drag_data = {'x': event.x, 'y': event.y}

def on_drag_motion(event):
    widget = event.widget
    x, y = widget.winfo_pointerxy()
    delta_x = x - widget.drag_data['x']
    delta_y = y - widget.drag_data['y']
    widget.place(x=widget.winfo_x() + delta_x, y=widget.winfo_y() + delta_y)
    widget.drag_data['x'] = x
    widget.drag_data['y'] = y

def on_drag_end(event):
    widget = event.widget
    del widget.drag_data

def get_widget_positions():
    positions = {}
    for widget in draggable_widgets:
        x, y = widget.winfo_x(), widget.winfo_y()
        positions[widget] = (x, y)
    return positions

root = tk.Tk()
root.title("Drag and Drop Example")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Create draggable widgets (labels in this example)
draggable_widgets = []
for i in range(1, 6):
    label = tk.Label(canvas, text=f"Item {i}", bg="lightgray")
    label.bind("<ButtonPress-1>", on_drag_start)
    label.bind("<B1-Motion>", on_drag_motion)
    label.bind("<ButtonRelease-1>", on_drag_end)
    label.place(x=10, y=i * 40)
    draggable_widgets.append(label)

# Create a button to get widget positions
get_positions_button = tk.Button(root, text="Get Widget Positions", command=lambda: print(get_widget_positions()))
get_positions_button.pack()

root.mainloop()