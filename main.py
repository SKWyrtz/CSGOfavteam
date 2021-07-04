import itertools
import tkinter as tk
from tkinter import font
from tkinter.constants import Y

text_file = open("teams(short).txt",  "r")
lines = text_file.read()
lines = lines.splitlines()
teams_dict = dict.fromkeys(lines, 0)
combinations = list(itertools.combinations(teams_dict, 2))
comparisons_done = 0

bg_colour ='#0e1f2e'
accent_colour = '#073957'

combinations_lenght = 0
for i in combinations:
    combinations_lenght += 1
print(f"length of combinations: {combinations_lenght}")

def generate_GUI(root):
    global instructions, team1_label, team2_label, team1_btn, team2_btn

    canvas = tk.Canvas(root, width=800, height=300, bg=bg_colour)
    canvas.grid(columnspan=2, rowspan=len(teams_dict)+3)

    frame = tk.Frame(root, height=75, width=800, bg=accent_colour)
    frame.grid(columnspan=3, column=0, row=0)
    frame.pack_propagate(False) 
    frame.update()
    instructions = tk.Label(frame, text="Select your favorite team of the two", font=("Raleway", 18), fg='white', bg=accent_colour )
    instructions.place(x=400, y=35, anchor='center')

    team1_label =tk.Label(root, text=combinations[0][0], font=("Raleway", 35, font.BOLD), fg='white', bg=bg_colour)
    team1_label.grid(column=0, row=1)

    team2_label =tk.Label(root, text=combinations[0][1], font=("Raleway", 35, font.BOLD), fg='white', bg=bg_colour)
    team2_label.grid(column=1, row=1)

    #Team1 Button
    team1_btn_text = tk.StringVar()
    team1_btn_text.set("Team 1")
    team1_btn = tk.Button(root, 
                        textvariable=team1_btn_text,
                        font=("Raleway", 14),
                        width=8,
                        command=lambda:favorite_selected(1, team1_label, team2_label))
    team1_btn.grid(column=0, row=2)

    #Team2 Button
    team2_btn_text = tk.StringVar()
    team2_btn_text.set("Team 2")
    team2_btn = tk.Button(root, 
                            textvariable=team2_btn_text,
                            font=("Raleway", 14),
                            width=8,
                            command=lambda:favorite_selected(2, team1_label, team2_label))
    team2_btn.grid(column=1, row=2)

def favorite_selected(team_selected, team_label1, team_label2): 
    global comparisons_done

    if not combinations_lenght == comparisons_done:
        print(f"Comparisons done are now: {comparisons_done}")
        team = combinations[comparisons_done][team_selected-1]
        print(f"The team selected is: {team}")
        teams_dict[team] += 1
        print("This team has been selected  times")
        if not combinations_lenght-1 == comparisons_done:
            next_team1 = combinations[comparisons_done + 1][0]
            next_team2 = combinations[comparisons_done + 1][1]
            team_label1.config(text=next_team1)
            team_label2.config(text=next_team2)
        comparisons_done += 1
    else:
        team1_label.destroy()
        team2_label.destroy()
        team1_btn.destroy()
        team2_btn.destroy()
        instructions.config(text="Here is the results:")

        sorted_teams = sorted(teams_dict.items(), key=lambda x:x[1], reverse=True)
        for index, element in enumerate(sorted_teams):
            team_label =tk.Label(root, text=element)
            team_label.grid(columnspan=3, column=0, row=index+1)
            print(element)
    
if __name__ == '__main__':
    root = tk.Tk()
    generate_GUI(root)
    root.mainloop()