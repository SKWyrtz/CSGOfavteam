import itertools
import tkinter as tk
from tkinter import font
import os
import argparse

comparisons_done = 0
bg_colour ='#0e1f2e'
accent_colour = '#073957'

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--teams",
    default="20",
    type=int,
    help="how many teams to be included (as INT)"
)
args = parser.parse_args()

def import_data():
    global teams_dict, wanted_rows, combinations, combinations_lenght

    text_file = open("teams.txt",  "r")
    lines = text_file.read()
    lines = lines.splitlines()
    teams_dict = dict.fromkeys(lines[0:args.teams], 0)

    wanted_rows = len(teams_dict)+3

    combinations = list(itertools.combinations(teams_dict, 2))

    combinations_lenght = 0
    for i in combinations:
        combinations_lenght += 1
    print(f"length of combinations: {combinations_lenght}")

def generate_GUI(root):
    global instructions, team1_label, team2_label, team1_btn, team2_btn, comparisons_left_text

    canvas = tk.Canvas(root, width=800, height=300, bg=bg_colour)
    canvas.grid(columnspan=2, rowspan=wanted_rows)

    #Instructions background
    frame = tk.Frame(root, height=75, width=800, bg=accent_colour)
    frame.grid(columnspan=3, column=0, row=0)
    frame.pack_propagate(False) 
    frame.update()

    #Instructions
    instructions = tk.Label(frame, text="Select your favorite team of the two", font=("Raleway", 18), fg='white', bg=accent_colour )
    instructions.place(x=400, y=35, anchor='center')

    #Restart Button
    restart_btn_text = tk.StringVar()
    restart_btn_text.set("Restart")
    restart_btn = tk.Button(root, textvariable=restart_btn_text, command=lambda:restart())
    restart_btn.place(x=75, y=40, anchor='center')

    #Team1 label
    team1_label =tk.Label(root, text=combinations[0][0], font=("Raleway", 35, font.BOLD), fg='white', bg=bg_colour)
    team1_label.grid(column=0, row=1)

    #Team2 label
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
    root.bind("<a>", team2_press)

    #Team2 Button
    team2_btn_text = tk.StringVar()
    team2_btn_text.set("Team 2")
    team2_btn = tk.Button(root, 
                            textvariable=team2_btn_text,
                            font=("Raleway", 14),
                            width=8,
                            command=lambda:favorite_selected(2, team1_label, team2_label))
    team2_btn.grid(column=1, row=2)
    root.bind("<s>", team2_press)

    comparisons_left_text = tk.Label(root, text=f"Comparisons left: {combinations_lenght}", font=("Raleway", 18), fg='white', bg=bg_colour)
    comparisons_left_text.place(x=290, y=250)

def team1_press(e=None):
    #CHECK IF DONE
    print("Test")
    favorite_selected(1, team1_label, team2_label)


def team2_press(e=None):
    print("Test")
    favorite_selected(2, team1_label, team2_label)


def favorite_selected(team_selected, team_label1, team_label2): 
    global comparisons_done
    if combinations_lenght-1 == comparisons_done:
        show_result()
    else:
        update_gui(team_selected, team_label1, team_label2)

def update_gui(team_selected, team_label1, team_label2):
        global comparisons_done

        team = combinations[comparisons_done][team_selected-1]
        teams_dict[team] += 1
        if not combinations_lenght-1 == comparisons_done:
            next_team1 = combinations[comparisons_done + 1][0]
            next_team2 = combinations[comparisons_done + 1][1]
            team_label1.config(text=next_team1)
            team_label2.config(text=next_team2)
            comparisons_left_text.config(text=f"Comparisons left: {combinations_lenght-(comparisons_done+1)}")
        comparisons_done += 1

def show_result():
        team1_label.destroy()
        team2_label.destroy()
        team1_btn.destroy()
        team2_btn.destroy()
        comparisons_left_text.destroy()
        instructions.config(text="Here is the results:")

        sorted_teams = sorted(teams_dict.items(), key=lambda x:x[1], reverse=True)
        for index, element in enumerate(sorted_teams):
            team_label =tk.Label(root, text=element)
            team_label.grid(columnspan=3, column=0, row=index+1)
            print(element)
                
        #Export Result Button
        export_res_btn_text = tk.StringVar()
        export_res_btn_text.set("Export Result")
        export_res_btn = tk.Button(root, 
                                textvariable=export_res_btn_text,
                                font=("Raleway", 8),
                                command=lambda:export_result())
        export_res_btn.place(x=75, y=270, anchor='center')

def export_result():
    print("Export")

def restart():
    root.destroy()
    os.startfile("main.py")
    
if __name__ == '__main__':
    import_data()
    root = tk.Tk()
    generate_GUI(root)
    root.mainloop()