katz_deli = []

def line(deli_line):
    if not deli_line:
        return "The line is currently empty."
    else:
        formatted_line = [f"{i+1}. {name}" for i, name in enumerate(deli_line)]
        return "The line is currently: " + " ".join(formatted_line)

def take_a_number(deli_line, name):
    deli_line.append(name)
    position = len(deli_line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving = deli_line.pop(0)
        print(f"Currently serving {serving}.")
