from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk,ImageDraw,ImageFont

root = Tk()




root.geometry("1000x500")
root.maxsize(1000, 500)
root.minsize(1000, 500)

canvas = Canvas(width=1000, height=500,highlightthickness=0)
canvas.pack(expand=True, fill=BOTH)

image = ImageTk.PhotoImage(file="city.png")
canvas.create_image(0, 0, image=image, anchor="nw")

root.title("Cement Replacement")
label = Label(text="PARTIAL REPLACEMENT OF VARIOUS MATERIALS", font="Arial 20 bold", relief=SUNKEN, borderwidth=5,fg="white",bg="#0066cc")
label.place(x=180,y=20)

ttk.Label(root, text="Concrete Material :", font="comicsansms 10 bold",foreground="black",background="#b3d9ff").place(x=36,y=120)

ttk.Label(root, text="Material 1 :", font="comicsansms 10 bold",foreground="black",background="#b3d9ff",).place(x=84,y=190)

ttk.Label(root, text="Material 2 :", font="comicsansms 10 bold",foreground="black",background="#b3d9ff",).place(x=84,y=260)

ttk.Label(root, text="Material 3 :", font="comicsansms 10 bold",foreground="black",background="#b3d9ff",).place(x=84,y=330)

ttk.Separator(root,orient=VERTICAL).place(relx=0.5, rely=0.15, relwidth=0.001, relheight=1)

# creating list of strength grade
strength_grade = [
    "Select",
    "M20",
    "M25",
    "M30",
    "M35",
    "M40",
    "M45",
    "M50"
]

# list of materials of m40
material_cement_m40 = [
    "Select",
    "NA",
    "Cement",
    "Soyabean Husk Ash",
    "Glass Powder",
    "Granite Powder"

]

material_sand_m40 = [
    "Select",
    "NA",
    "Sand",
    "Glass Fine Aggregate",
    "Granite Fine Aggregate"
]

material_agg_m40 =[
    "Select",
    "NA",
    "Aggregate",
    "Glass Coarse Aggregate",
    "Granite Coarse Aggregate"

]

# list of materials of m35
material_cement_m35 = [
    "Select",
    "NA",
    "Cement",
    "Marble Dust",
    "Egg Shell Powder",
    "Fly Ash",
    "Micro Silica",
    "Silica Fume"
]

material_sand_m35 = [
    "Select",
    "NA",
    "Sand",
    "Copper Sand",
    "Glass Granular"
]

material_aggregation_m35 = [
    "Select",
    "NA",
    "Aggregate",
    "Steel Slag"
]

# list of materials of m30
material_cement_m30 = [
    "Select",
    "NA",
    "Cement",
    "White Husk Ash",
    "Wheat Husk Ash",
    "Metakaolin",
    "Marble Dust",
    "Egg Shell Powder",
    "Ggbs",
    "Activated Fly Ash"
]

material_sand_m30 = [
    "Select",
    "NA",
    "Sand",
    "Crumb Rubber",
    "Querry Dust",
    "Foundary Sand",
    "Copper Slag"
]

material_aggregation_m30 = [
    "Select",
    "NA",
    "Aggregate",
    "Steel Slag",
    "Marble"
]

# list of materials of m25
material_cement_m25 = [
    "Select",
    "NA",
    "Cement",
    "Fly Ash",
    "Metakaolin",
    "Waste Marble Powder",
    "Glass Powder"
]

material_sand_m25 =[
    "Select",
    "NA",
    "Sand",
    "Waste Foundary Sand",
    "Querry Dust"
]

material_aggregation_m25 = [
    "Select",
    "NA",
    "Aggregate",
    "E-Waste",
    "Coconut Shell",
    "Silica Fume"
]

# list of materials of m50
material_cement_m50 = [
    "Select",
    "NA",
    "Cement",
    "Fly Ash",
    "Rice Husk Ash",
    "Metakaolin",
    "Egg Shell"
]

material_sand_m50 = [
    "Select",
    "NA",
    "Sand",
    "Stone Crusher Dust",
    "M-Sand"
]

material_aggregation_m50 = [
    "Select",
    "NA",
    "Aggregate",
    "Coconut Shell"
]

# list of materials of m20
material_cement_m20 = [
    "Select",
    "NA",
    "Cement",
    "Stone Dust",
    "Rice Husk Ash",
    "Fly Ash",
    "Silica Fume",
    "Ggbs",
    "Granite Powder"
]

material_sand_m20 = [
    "Select",
    "NA",
    "Sand",
    "Crushed Sand",
    "Waste Glass Powder",
    "M-Sand",
    "Tiles Powder"

]

material_aggregation_m20 = [
    "Select",
    "NA",
    "E-Waste",
    "Aggregate",
    "Tiles Crushed",
    "Reclaimed Rubber",
    "Coconut Shell"
]

materials_cement = [
    "Cement"
]
materials_sand = [
    "Sand"
]
materials_agg = [
    "Aggregate"
]

novalue = "NA"


def clear():
    if my_combo.get() == "Select" and material_combo.get() == " ":
        tmsg.showerror("Error!", "Empty Field")

    else:
        my_combo.set("Select")
        material_combo.set(" ")
        material_combo1.set(" ")
        material_combo2.set(" ")




def pick_all_material(e):
    if my_combo.get() == "M40":
        material_combo.config(values=material_cement_m40)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m40)
        material_combo1.current(0)
        material_combo2.config(values=material_agg_m40)
        material_combo2.current(0)

    if my_combo.get() == "M30":
        material_combo.config(values=material_cement_m30)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m30)
        material_combo1.current(0)
        material_combo2.config(values=material_aggregation_m30)
        material_combo2.current(0)

    if my_combo.get() == "M35":
        material_combo.config(values=material_cement_m35)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m35)
        material_combo1.current(0)
        material_combo2.config(values=material_aggregation_m35)
        material_combo2.current(0)

    if my_combo.get() == "M25":
        material_combo.config(values=material_cement_m25)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m25)
        material_combo1.current(0)
        material_combo2.config(values=material_aggregation_m25)
        material_combo2.current(0)

    if my_combo.get() == "M20":
        material_combo.config(values=material_cement_m20)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m20)
        material_combo1.current(0)
        material_combo2.config(values=material_aggregation_m20)
        material_combo2.current(0)

    if my_combo.get() == "M50":
        material_combo.config(values=material_cement_m50)
        material_combo.current(0)
        material_combo1.config(values=material_sand_m50)
        material_combo1.current(0)
        material_combo2.config(values=material_aggregation_m50)
        material_combo2.current(0)

    if my_combo.get() == "M45":
        material_combo.config(values=novalue)
        material_combo.current(0)
        material_combo1.config(values=novalue)
        material_combo1.current(0)
        material_combo2.config(values=novalue)
        material_combo2.current(0)

def pick_material(e):
    if my_combo.get() == "M40" or "M30" or "M35" or "M25" or "M20" or "M50":
        if material_combo.get() == "Cement":
            material_combo1.config(values=materials_sand)
            material_combo1.current(0)
            material_combo2.config(values=materials_agg)
            material_combo2.current(0)

    if my_combo.get() == "M40":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_agg_m40)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m40)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_cement_m40)
            material_combo1.current(0)

    if my_combo.get() == "M30":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_aggregation_m30)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m30)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_cement_m30)
            material_combo1.current(0)

    if my_combo.get() == "M20":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_aggregation_m20)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m20)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_cement_m20)
            material_combo1.current(0)

    if my_combo.get() == "M35":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_aggregation_m35)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m35)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_cement_m35)
            material_combo1.current(0)

    if my_combo.get() == "M25":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_aggregation_m25)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m25)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_cement_m25)
            material_combo1.current(0)

    if my_combo.get() == "M50":
        if material_combo.get() == "NA" and material_combo1.get() == "NA":
            material_combo2.config(values=material_aggregation_m50)
            material_combo2.current(0)

        if material_combo.get() == "NA" and material_combo2.get() == "NA":
            material_combo1.config(values=material_sand_m50)
            material_combo1.current(0)

        if material_combo1.get() == "NA" and material_combo2.get() == "NA":
            material_combo.config(values=material_cement_m50)
            material_combo.current(0)


Button(root, text="Clear", command=clear, width=10, bg="White", borderwidth=5, font="Arial 10 bold").place(x=220,y=390)

# def pick_all_material1(e):
#     if my_combo.get() == "M40":
#         material_combo.config(values=material_cement_m40)
#         material_combo.current(0)
#         if material_combo.get() == "Soyabean Husk Ash":
#             material_combo1 = ttk.Combobox(root, values=novalue)
#             material_combo1.current(0)
#             material_combo1.place(x=220, y=260)
#
#             material_combo2 = ttk.Combobox(root, values=novalue)
#             material_combo2.current(0)
#             material_combo2.place(x=220, y=330)

def findvalue():
    if material_combo.get() == "Select" and material_combo1.get() == "Select" and material_combo2.get() == "Select":
        tmsg.showerror("Error!", "Please Enter the Data !")
    elif my_combo.get() == "Select" and material_combo.get() == " " and material_combo1.get() == " " and material_combo2.get() == " ":
        tmsg.showerror("Error!", "Please Enter the Data !")

    elif material_combo.get() == "Select" or material_combo1.get() == "Select" or material_combo2.get() == "Select":
        tmsg.showerror("Error!", "Please Enter all Data !")

    else:
        a = ttk.Label(root, text="Add material(%) :", font="comicsansms 10 bold", foreground="black",background="#b3d9ff")
        a.place(x=540, y=120)

        b = ttk.Label(root, text="Replacer + Material 1(KG) :", font="comicsansms 10 bold", foreground="black",background="#b3d9ff")
        b.place(x=530, y=190)

        c = ttk.Label(root, text="Cement(Kg/m3) :", font="comicsansms 10 bold", foreground="black",background="#b3d9ff")
        c.place(x=542, y=260)

        d = ttk.Label(root, text="Sand(Kg/m3) :", font="comicsansms 10 bold", foreground="black", background="#b3d9ff")
        d.place(x=557, y=330)

        n = ttk.Label(root, text="Aggregate(Kg/m3) :", font="comicsansms 10 bold", foreground="black", background= "#b3d9ff")
        n.place(x=525, y=400)

        # average in % of m20
        per_value_cement_stonedust_m20 = "20"
        per_value_cement_rice_hus_m20 = "5"
        per_value_cement_flyash_m20 = "10"
        per_value_cement_silicafume_m20 = "15"
        per_value_cement_ggbs_m20 = "20"
        per_value_cement_grapow_m20 = "20"
        per_value_sand_crushesand_m20 = "30"
        per_value_sand_wasteglasspow_m20 = "20"
        per_value_sand_msand_m20 = "10"
        per_value_sand_tilespow_m20 = "50"
        per_value_agg_ewaste_m20 = "12"
        per_value_agg_tilecrushed_m20 = "50"
        per_value_agg_reclrub_m20 = "9"
        per_value_agg_cocoshell_m20 = "5"

        # average in % of m40
        per_value_cement_glass_m40 = "12.5"
        per_value_cement_soyabean_m40 = "10"
        per_value_cement_granite_m40 = "15"
        per_value_sand_glass_m40 = "20"
        per_value_sand_granite_m40 = "10"
        per_value_agg_glass_m40 = "10"
        per_value_agg_granite_m40 = "5"

        # average in % of m35
        per_value_cement_marble_dust_m35 = "10"
        per_value_cement_egg_shell_m35 = "4"
        per_value_cement_fly_ash_m35 = "35"
        per_value_cement_micro_silica_m35 = "15"
        per_value_cement_silica_fume_m35 = "13"
        per_value_sand_copper_sand_m35 = "40"
        per_value_sand_glass_granular_m35 = "20"
        per_value_agg_steel_slag_m35 = "45"

        # average in % of m30
        per_value_cement_white_husk_m30 = "10"
        per_value_cement_wheat_husk_m30 = "10"
        per_value_cement_metakaolin_m30 = "20"
        per_value_cement_egg_shell_m30 = "10"
        per_value_cement_marble_dust_m30 = "10"
        per_value_cement_ggbs_m30 = "20"
        per_value_cement_fly_ash_m30 = "40"
        per_value_sand_crumb_rub_m30 = "10"
        per_value_sand_querry_dust_m30 = "20"
        per_value_sand_foundary_sand_m30 = "25"
        per_value_sand_copper_slag_m30 = "40"
        per_value_agg_steel_slag_m30 = "30"
        per_value_agg_marble_m30 = "20"

        # average in % of m25
        per_value_cement_fly_ash_m25 = "25"
        per_value_cement_metakaolin_m25 = "20"
        per_value_cement_waste_marb_m25 = "12"
        per_value_cement_glass_pow_m25 = "10"
        per_value_sand_waste_fond_m25 = "20"
        per_value_sand_querry_dust_m25 = "20"
        per_value_agg_ewaste_m25 = "10"
        per_value_agg_cocoshell_m25 = "10"
        per_value_agg_silicafume_m25 = "10"

        # average in % of m50
        per_value_cement_fly_ash_m50 = "15"
        per_value_cement_rice_husk_ash_m50 = "15"
        per_value_cement_metakaolin_m50 = "10"
        per_value_cement_egg_shell_m50 = "5"
        per_value_sand_stone_crusher_m50 = "10"
        per_value_sand_msand_m50 = "70"
        per_value_agg_cocoshell_m50 = "5"

        # kg/m^3
        cement_per_kgm3_m20 = "400"
        sand_per_kgm3_m20 = "672"
        agg_per_kgm3_m20 = "1326"
        cement_per_kgm3_m35 = "445"
        sand_per_kgm3_m35 = "620"
        agg_per_kgm3_m35 = "1171"
        cement_per_kgm3_m30 = "420"
        sand_per_kgm3_m30 = "685"
        agg_per_kgm3_m30 = "1170"
        cement_per_kgm3_m25 = "554"
        sand_per_kgm3_m25 = "558"
        agg_per_kgm3_m25 = "1155"
        cement_per_kgm3_m50 = "410"
        sand_per_kgm3_m50 = "764"
        agg_per_kgm3_m50 = "1152"
        cement_per_kgm3_m40 = "320"
        sand_per_kgm3_m40 = "720"
        agg_per_kgm3_m40 = "1090"
        cement_per_kgm3_m45 = "410"
        sand_per_kgm3_m45 = "850"
        agg_per_kgm3_m45 = "1118"
        no_value = "NA"

        # mix material in kg for m40
        material_in_kg_soyabean_cement_m40 = "32 Soyabean + 288 Cement"
        material_in_kg_glass_cement_m40 = "40 Glass Powder + 280 Cement"
        material_in_kg_glass_sand_m40 = "144 Glass F.A. + 576 F.A."
        material_in_kg_glass_agg_m40 = "109 Glass F.A. + 981 Aggregate"
        material_in_kg_granite_cement_m40 = "48 Granite Powder + 272 Cement"
        material_in_kg_granite_sand_m40 = "72 Granite F.A.+ 648 F.A."
        material_in_kg_granite_agg_m40 = "54.4 Granite C.A.+ 1035.5 C.A."

        # mix material in kg for m50
        material_in_kg_fly_cement_m50 = "61.5 Fly Ash + 378.5 Cement"
        material_in_kg_rice_cement_m50 = "61.5 Rice Husk Ash + 378.5 Cement"
        material_in_kg_metakaolin_cement_m50 = "41 Metakaolin + 369 Cement"
        material_in_kg_egg_cement_m50 = "20.5 Egg Shell + 389.5 Cement"
        material_in_kg_stone_sand_m50 = "76.4 Stone Crusher Dust + 687.6 Sand"
        material_in_kg_msand_sand_m50 = "535 M-Sand + 229 Sand"
        material_in_kg_coco_agg_m50 = "57.6 Coconut Shell + 1094 Aggregate"

        # mix material in kg for m25
        material_in_kg_fly_cement_m25 = "139 Fly Ash + 415 Cement"
        material_in_kg_metakaolin_cement_m25 = "111 Fly Ash + 443 Cement"
        material_in_kg_waste_cement_m25 = "66.5 Waste Marble Powder + 487.5 Cement"
        material_in_kg_glass_cement_m25 = "55 Glass Powder + 499 Cement"
        material_in_kg_waste_sand_m25 = "112 Waste Foundary Sand + 446 Sand"
        material_in_kg_Querry_sand_m25 = "112 Querry Dust + 446 Sand"
        material_in_kg_ewaste_agg_m25 = "116 E-Waste + 1038 Aggregate"
        material_in_kg_coco_agg_m25 = "116 Coconut Shell + 1039 Aggregate"
        material_in_kg_sili_agg_m25 = "116 Silica Fume + 1038 Aggregate"

        # mix material in kg for m30
        material_in_kg_white_cement_m30 = "42 White Husk Ash + 420 Cement"
        material_in_kg_wheat_cement_m30 = "42 Wheat Husk Ash + 378 Cement"
        material_in_kg_metakaolin_cement_m30 = "84 Metakaolin + 336 Cement"
        material_in_kg_marble_cement_m30 = "42 Marble Dust + 378 Cement"
        material_in_kg_egg_cement_m30 = "42 Egg Shell Powder + 378 Cement"
        material_in_kg_Ggbs_cement_m30 = "84 GGBS + 336 Cement"
        material_in_kg_activ_cement_m30 = "168 Activated Fly Ash + 252 Cement"
        material_in_kg_crumb_sand_m30 = "68.5 Crumb Rubber + 616.5 Sand"
        material_in_kg_querry_sand_m30 = "137 Querry Dust + 548 Sand"
        material_in_kg_foundary_sand_m30 = "171.25 Foundary Sand + 513.75 Sand"
        material_in_kg_copper_sand_m30 = "274 Copper Slag + 411 Sand"
        material_in_kg_steel_agg_m30 = "351 Steel Slag + 819 Aggregate"
        material_in_kg_marb_agg_m30 = "234 Marble + 936 Aggregate"

        # mix material in kg for m30
        material_in_kg_marb_cement_m35 = "44.5 Marble Dust + 400.5 Cement"
        material_in_kg_egg_cement_m35 = "17.8 Egg Shell Powder + 421.2 Cement"
        material_in_kg_fly_cement_m35 = "155.7 Egg Fly Ash + 289.25 Cement"
        material_in_kg_micro_cement_m35 = "66.75 Micro Silica + 378.25 Cement"
        material_in_kg_sili_cement_m35 = "57.85 Silica Fume + 387.15 Cement"
        material_in_kg_copper_sand_m35 = "248 Copper Sand + 372 Sand"
        material_in_kg_glass_sand_m35 = "124 Glass Granular + 496 Sand"
        material_in_kg_steel_agg_m35 = "527 Steel Slag + 644 Aggregate"

        # mix material in kg for m20
        material_in_kg_stone_cement_m20 = "80 Stone Dust + 320 Cement"
        material_in_kg_rice_cement_m20 = "20 Rice Husk Ash + 380 Cement"
        material_in_kg_fly_cement_m20 = "20 Fly Ash + 360 Cement"
        material_in_kg_silica_cement_m20 = "60 Silica Fume + 340 Cement"
        material_in_kg_ggbs_cement_m20 = "80 Ggbs + 320 Cement"
        material_in_kg_granite_cement_m20 = "80 Granite Powder + 320 Cement"
        material_in_kg_crushed_sand_m20 = "201.6 Crushed Sand + 470.4 Sand"
        material_in_kg_waste_sand_m20 = "135 Waste Glass Powder + 537 Sand"
        material_in_kg_msand_sand_m20 = "67 M-Sand + 605 Sand"
        material_in_kg_tiles_sand_m20 = "336 Tiles Powder + 336 Sand"
        material_in_kg_ewaste_agg_m20 = "160 E-Waste + 1166 Aggregate"
        material_in_kg_tiles_agg_m20 = "663 Tiles Crushed + 663 Aggregate"
        material_in_kg_reclaimed_agg_m20 = "120 Reclaimed Rubber + 1207 Aggregate"
        material_in_kg_coconut_agg_m20 = "66 Coconut Shell + 1260 Aggregate"


        if my_combo.get() == "M40":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)

                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m40)
                my_combo3.place(x=720, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=720, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "Soyabean Husk Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_soyabean_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_soyabean_cement_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Glass Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_glass_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_glass_cement_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Granite Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_granite_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_granite_cement_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Glass Fine Aggregate" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_glass_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_glass_sand_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m40)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Granite Fine Aggregate" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_granite_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_granite_sand_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m40)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m40)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Glass Coarse Aggregate" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_glass_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_glass_agg_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m40)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Granite Coarse Aggregate" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_granite_m40)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root,width=38)
                my_combo2.insert(0, material_in_kg_granite_agg_m40)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m40)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m40)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M50":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)
                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)
                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m50)
                my_combo3.place(x=720, y=260)
                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=720, y=330)
                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "Fly Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_fly_ash_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_fly_cement_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Rice Husk Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_rice_husk_ash_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_rice_cement_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Metakaolin" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_metakaolin_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_metakaolin_cement_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Egg Shell" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_egg_shell_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_egg_cement_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Stone Crusher Dust" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_stone_crusher_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_stone_sand_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m50)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "M-Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_msand_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_msand_sand_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m50)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m50)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Coconut Shell" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_cocoshell_m50)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_coco_agg_m50)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m50)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m50)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M25":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)
                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)
                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=720, y=260)
                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=720, y=330)
                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "Fly Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_fly_ash_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_fly_cement_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Metakaolin" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_metakaolin_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_metakaolin_cement_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Waste Marble Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_waste_marb_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_waste_cement_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Glass Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_glass_pow_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_glass_cement_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Waste Foundary Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_waste_fond_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_waste_sand_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Querry Dust" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_querry_dust_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_Querry_sand_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m25)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "E-Waste" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_ewaste_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_ewaste_agg_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Coconut Shell" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_cocoshell_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_coco_agg_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Silica Fume" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_silicafume_m25)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_sili_agg_m25)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m25)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m25)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M30":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)
                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)
                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=720, y=260)
                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=720, y=330)
                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "White Husk Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_white_husk_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_white_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Wheat Husk Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_wheat_husk_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_wheat_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Metakaolin" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_metakaolin_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_metakaolin_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Marble Dust" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_marble_dust_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_marble_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Ggbs" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_ggbs_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_Ggbs_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Egg Shell Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_egg_shell_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_egg_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Activated Fly Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_fly_ash_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_activ_cement_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Querry Dust" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_querry_dust_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_querry_sand_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Crumb Rubber" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_crumb_rub_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_crumb_sand_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Foundary Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_foundary_sand_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_foundary_sand_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Copper Slag" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_copper_slag_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_copper_sand_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m30)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Steel Slag" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_steel_slag_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_steel_agg_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Marble" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_marble_m30)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_marb_agg_m30)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m30)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m30)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M35":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)
                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)
                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m35)
                my_combo3.place(x=720, y=260)
                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=720, y=330)
                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "Marble Dust" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_marble_dust_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_marb_cement_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Egg Shell Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_egg_shell_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_egg_cement_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Fly Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_fly_ash_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_fly_cement_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Micro Silica" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_micro_silica_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_micro_cement_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Silica Fume" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_silica_fume_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_sili_cement_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Copper Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_copper_sand_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_copper_sand_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m35)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Glass Granular" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_glass_granular_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_glass_sand_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m35)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m35)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Steel Slag" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_steel_slag_m35)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_steel_agg_m35)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m35)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m35)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M20":
            if material_combo.get() == "Cement" or material_combo1.get() == "Sand" or material_combo2.get() == "Aggregate":
                my_combo1 = Entry(root)
                my_combo1.insert(0, no_value)
                my_combo1.place(x=720, y=120)
                my_combo2 = Entry(root)
                my_combo2.insert(0, no_value)
                my_combo2.place(x=720, y=190)
                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=720, y=260)
                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=720, y=330)
                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=720, y=400)

            elif material_combo.get() == "Stone Dust" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_stonedust_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_stone_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Rice Husk Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_rice_hus_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_rice_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Fly Ash" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_flyash_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_fly_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Silica Fume" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_silicafume_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_silica_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Ggbs" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_ggbs_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_ggbs_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo.get() == "Granite Powder" and material_combo1.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_cement_grapow_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_granite_cement_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, no_value)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Crushed Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_crushesand_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_crushed_sand_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Waste Glass Powder" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_wasteglasspow_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_waste_sand_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "M-Sand" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_msand_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_msand_sand_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo1.get() == "Tiles Powder" and material_combo.get() == "NA" and material_combo2.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_sand_tilespow_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_tiles_sand_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, no_value)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, agg_per_kgm3_m20)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "E-Waste" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_ewaste_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_ewaste_agg_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Tiles Crushed" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_tilecrushed_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_tiles_agg_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Reclaimed Rubeer" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_reclrub_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_reclaimed_agg_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

            elif material_combo2.get() == "Coconut Shell" and material_combo.get() == "NA" and material_combo1.get() == "NA":

                my_combo1 = Entry(root)
                my_combo1.insert(0, per_value_agg_cocoshell_m20)
                my_combo1.place(x=750, y=120)

                my_combo2 = Entry(root, width=38)
                my_combo2.insert(0, material_in_kg_coconut_agg_m20)
                my_combo2.place(x=750, y=190)

                my_combo3 = Entry(root)
                my_combo3.insert(0, cement_per_kgm3_m20)
                my_combo3.place(x=750, y=260)

                my_combo4 = Entry(root)
                my_combo4.insert(0, sand_per_kgm3_m20)
                my_combo4.place(x=750, y=330)

                my_combo5 = Entry(root)
                my_combo5.insert(0, no_value)
                my_combo5.place(x=750, y=400)

        if my_combo.get() == "M45":
            my_combo1 = Entry(root)
            my_combo1.insert(0,no_value)
            my_combo1.place(x=750, y=120)

            my_combo2 = Entry(root)
            my_combo2.insert(0, no_value)
            my_combo2.place(x=750, y=190)

            my_combo3 = Entry(root)
            my_combo3.insert(0, cement_per_kgm3_m45)
            my_combo3.place(x=750, y=260)

            my_combo4 = Entry(root)
            my_combo4.insert(0, sand_per_kgm3_m45)
            my_combo4.place(x=750, y=330)

            my_combo5 = Entry(root)
            my_combo5.insert(0, agg_per_kgm3_m45)
            my_combo5.place(x=750, y=400)

        def clear():


                my_combo1.destroy()
                my_combo2.destroy()
                my_combo3.destroy()
                my_combo4.destroy()
                my_combo5.destroy()
        Button(root, text="Clear", command=clear, width=10, bg="White", borderwidth=5, font="Arial 10 bold").place(
            x=700, y=450)



# create combobox 1
my_combo = ttk.Combobox(root, values=strength_grade,state="readonly")
my_combo.current(0)
my_combo.place(x=220,y=120)

# create combobox 2
material_combo = ttk.Combobox(root, values=[" "],state="readonly")
material_combo.current(0)
material_combo.place(x=220,y=190)

# create combobox 3
material_combo1 = ttk.Combobox(root, values=[" "],state="readonly")
material_combo1.current(0)
material_combo1.place(x=220,y=260)

# create combobox 4
material_combo2 = ttk.Combobox(root, values=[" "],state="readonly")
material_combo2.current(0)
material_combo2.place(x=220,y=330)

my_combo.bind("<<ComboboxSelected>>", pick_all_material)
material_combo.bind("<<ComboboxSelected>>", pick_material)


# adding button
Button(root, text="Find", command=findvalue,width=10,bg="White",borderwidth=5,font="Arial 10 bold",textvariable="x").place(x=100,y=390)
Button(root, text="Exit", command=root.destroy,width=10,bg="White",borderwidth=5,font="Arial 10 bold").place(x=340,y=390)


root.mainloop()
