import os

"""
File containing the process technology parameters for FreePDK 45nm.
"""

info = {}
info["name"] = "freepdk45"
info["body_tie_down"] = 0
info["has_pwell"] = True
info["has_nwell"] = True

#GDS file info
GDS = {}
# gds units
GDS["unit"] = (0.0005,1e-9)
# default label zoom
GDS["zoom"] = 0.05

###################################################
##GDS Layer Map
###################################################

# create the GDS layer map
# FIXME: parse the gds layer map from the cadence map?
layer = {}
layer["active"]  = 1
layer["pwell"]   = 2
layer["nwell"]   = 3
layer["nimplant"]= 4
layer["pimplant"]= 5
layer["vtg"]     = 6
layer["vth"]     = 7
layer["thkox"]   = 8
layer["poly"]    = 9
layer["contact"] = 10
layer["active_contact"] = 10
layer["metal1"]  = 11
layer["via1"]    = 12
layer["metal2"]  = 13
layer["via2"]    = 14
layer["metal3"]  = 15
layer["via3"]    = 16
layer["metal4"]  = 17
layer["via4"]    = 18
layer["metal5"]  = 19
layer["via5"]    = 20
layer["metal6"]  = 21
layer["via6"]    = 22
layer["metal7"]  = 23
layer["via7"]    = 24
layer["metal8"]  = 25
layer["via8"]    = 26
layer["metal9"]  = 27
layer["via9"]    = 28
layer["metal10"] = 29
layer["text"]    = 239
layer["boundary"]= 239

###################################################
##END GDS Layer Map
###################################################

###################################################
##DRC/LVS Rules Setup
###################################################

#technology parameter
parameter={}
parameter["min_tx_size"] = 0.09
parameter["beta"] = 3

drclvs_home=os.environ.get("DRCLVS_HOME")
drc={}
#grid size
drc["grid"] = 0.0025

#DRC/LVS test set_up
drc["drc_rules"]=drclvs_home+"/calibreDRC.rul"
drc["lvs_rules"]=drclvs_home+"/calibreLVS.rul"
drc["xrc_rules"]=drclvs_home+"/calibrexRC.rul"
drc["layer_map"]=os.environ.get("OPENRAM_TECH")+"/freepdk45/layers.map"

# minwidth_tx with contact (no dog bone transistors)
drc["minwidth_tx"]=0.09
drc["minlength_channel"] = 0.05

# WELL.1 Minimum spacing of nwell/pwell at different potential
drc["pwell_to_nwell"] = 0.225
# WELL.4 Minimum width of nwell/pwell
drc["minwidth_well"] = 0.2

# POLY.1 Minimum width of poly
drc["minwidth_poly"] = 0.05
# POLY.2 Minimum spacing of poly AND active
drc["poly_to_poly"] = 0.14
# POLY.3 Minimum poly extension beyond active
drc["poly_extend_active"] = 0.055
# POLY.4 Minimum enclosure of active around gate
drc["active_enclosure_gate"] = 0.07
# POLY.5 Minimum spacing of field poly to active
drc["poly_to_active"] = 0.05
# POLY.6 Minimum Minimum spacing of field poly
drc["poly_to_field_poly"] = 0.075
# Not a rule
drc["minarea_poly"] = 0.0

# ACTIVE.2 Minimum spacing of active
drc["active_to_body_active"] = 0.08
# ACTIVE.1 Minimum width of active
drc["minwidth_active"] = 0.09
# Not a rule
drc["active_to_active"] = 0
# ACTIVE.3 Minimum enclosure/spacing of nwell/pwell to active
drc["well_enclosure_active"] = 0.055
# Reserved for asymmetric enclosures
drc["well_extend_active"] = 0.055
# Not a rule
drc["minarea_active"] = 0

# IMPLANT.1 Minimum spacing of nimplant/ pimplant to channel
drc["implant_to_channel"] = 0.07
# Not a rule
drc["implant_enclosure_active"] = 0
# Not a rule
drc["implant_enclosure_contact"] = 0
# IMPLANT.2 Minimum spacing of nimplant/ pimplant to contact
drc["implant_to_contact"] = 0.025
# IMPLANT.3 Minimum width/ spacing of nimplant/ pimplant
drc["implant_to_implant"] = 0.045
# IMPLANT.4 Minimum width/ spacing of nimplant/ pimplant
drc["minwidth_implant"] = 0.045

# CONTACT.1 Minimum width of contact
drc["minwidth_contact"] = 0.065
# CONTACT.2 Minimum spacing of contact
drc["contact_to_contact"] = 0.075
# CONTACT.4 Minimum enclosure of active around contact
drc["active_enclosure_contact"] = 0.005
# Reserved for asymmetric enclosures
drc["active_extend_contact"] = 0.005
# CONTACT.5 Minimum enclosure of poly around contact
drc["poly_enclosure_contact"] = 0.005
# Reserved for asymmetric enclosures
drc["poly_extend_contact"] = 0.005
# CONTACT.6 Minimum spacing of contact and gate
drc["contact_to_gate"] = 0.0375 #changed from 0.035
# CONTACT.7 Minimum spacing of contact and poly
drc["contact_to_poly"] = 0.090

# METAL1.1 Minimum width of metal1
drc["minwidth_metal1"] = 0.065
# METAL1.2 Minimum spacing of metal1
drc["metal1_to_metal1"] = 0.065
# METAL1.3 Minimum enclosure around contact on two opposite sides
drc["metal1_enclosure_contact"] = 0
# Reserved for asymmetric enclosures
drc["metal1_extend_contact"] = 0.035
# METAL1.4 inimum enclosure around via1 on two opposite sides
drc["metal1_extend_via1"] = 0.035
# Reserved for asymmetric enclosures
drc["metal1_enclosure_via1"] = 0
# Not a rule
drc["minarea_metal1"] = 0

# VIA1.1 Minimum width of via1
drc["minwidth_via1"] = 0.065
# VIA1.2 Minimum spacing of via1
drc["via1_to_via1"] = 0.075

# METALINT.1 Minimum width of intermediate metal
drc["minwidth_metal2"] = 0.07
# METALINT.2 Minimum spacing of intermediate metal
drc["metal2_to_metal2"] = 0.07
# METALINT.3 Minimum enclosure around via1 on two opposite sides
drc["metal2_extend_via1"] = 0.035
# Reserved for asymmetric enclosures
drc["metal2_enclosure_via1"] = 0
# METALINT.4 Minimum enclosure around via[2-3] on two opposite sides
drc["metal2_extend_via2"] = 0.035
# Reserved for asymmetric enclosures
drc["metal2_enclosure_via2"] = 0
# Not a rule
drc["minarea_metal2"] = 0

# VIA2-3.1 Minimum width of Via[2-3]
drc["minwidth_via2"] = 0.065
# VIA2-3.2 Minimum spacing of Via[2-3]
drc["via2_to_via2"] = 0.075

# METALINT.1 Minimum width of intermediate metal
drc["minwidth_metal3"] = 0.07
# METALINT.2 Minimum spacing of intermediate metal
drc["metal3_to_metal3"] = 0.07
# METALINT.3 Minimum enclosure around via1 on two opposite sides
drc["metal3_extend_via2"] = 0.035
# Reserved for asymmetric enclosures
drc["metal3_enclosure_via2"] = 0
# METALINT.4 Minimum enclosure around via[2-3] on two opposite sides
drc["metal3_extend_via3"]=0.035
# Reserved for asymmetric enclosures
drc["metal3_enclosure_via3"] = 0
# Not a rule
drc["minarea_metal3"] = 0

# VIA2-3.1 Minimum width of Via[2-3]
drc["minwidth_via3"] = 0.065
# VIA2-3.2 Minimum spacing of Via[2-3]
drc["via3_to_via3"] = 0.07

# METALSMG.1 Minimum width of semi-global metal
drc["minwidth_metal4"] = 0.14
# METALSMG.2 Minimum spacing of semi-global metal
drc["metal4_to_metal4"] = 0.14
# METALSMG.3 Minimum enclosure around via[3-6] on two opposite sides
drc["metal4_extend_via3"] = 0.07
# Reserved for asymmetric enclosure
drc["metal4_enclosure_via3"] = 0
# METALSMG.3 Minimum enclosure around via[3-6] on two opposite sides
drc["metal4_enclosure_via4"] = 0
# Reserved for asymmetric enclosure
drc["metal4_extend_via4"] = 0.07

# Metal 5-10 are ommitted



###################################################
##END DRC/LVS Rules
###################################################

###################################################
##Spice Simulation Parameters
###################################################

#spice info
spice = {}
spice["nmos"] = "nmos_vtg"
spice["pmos"] = "pmos_vtg"
# This is a map of corners to model files
SPICE_MODEL_DIR=os.environ.get("SPICE_MODEL_DIR")
spice["fet_models"] = { "TT" : [SPICE_MODEL_DIR+"/NMOS_VTG.inc",SPICE_MODEL_DIR+"/PMOS_VTG.inc"]}

#spice stimulus related variables
spice["feasible_period"] = 5 # estimated feasible period in ns
spice["supply_voltage"] = 1.0        # ideal vdd in [Volts]
spice["rise_time"] = 0.005           # rise time in [Nano-seconds]
spice["fall_time"] = 0.005           # fall time in [Nano-seconds]
spice["nom_corner"] = ("TT", 1.0, 25) # Nominal process corner

#sram signal names
spice["vdd_name"] = "vdd"
spice["gnd_name"] = "gnd"
spice["control_signals"] = ["CSb", "WEb", "OEb"]
spice["data_name"] = "DATA"
spice["addr_name"] = "ADDR"
spice["minwidth_tx"] = drc["minwidth_tx"]
spice["channel"] = drc["minlength_channel"]
spice["clk"] = "clk"

# analytical delay parameters
spice["wire_unit_r"] = 0.075     # Unit wire resistance in ohms/square
spice["wire_unit_c"] = 0.64      # Unit wire capacitance ff/um^2
spice["min_tx_r"] = 9250.0       # Minimum transistor on resistance in ohms
spice["min_tx_drain_c"] = 0.7    # Minimum transistor drain capacitance in ff
spice["min_tx_gate_c"] = 0.2     # Minimum transistor gate capacitance in ff
spice["msflop_setup"] = 9        # DFF setup time in ps
spice["msflop_hold"] = 1         # DFF hold time in ps
spice["msflop_delay"] = 20.5     # DFF Clk-to-q delay in ps
spice["msflop_slew"] = 13.1      # DFF output slew in ps w/ no load
spice["msflop_in_cap"] = 0.2091  # Input capacitance of ms_flop (Din) [Femto-farad]


###################################################
##END Spice Simulation Parameters
###################################################

