####################################
#CtrlPt_Insert.py
#write script that adds the input number of
#control points to a beam
#
#Modified History:
#2015 09 Becket Hui
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, os

def write(savFolder, nCP):
 """!
 @brief:
 @  write the Pinnacle script that add CPs to a beam
 @param:
 @  savFolder: location of the patient folder, where the script would be saved to
 @  nCP: number of control points to be added
 """
 fw = open(savFolder+'addCP.Script','w')
 fw.write('////////////////////\n')
 fw.write('////addCP.Script////\n')
 fw.write('////////////////////\n')
 fw.write('\n')
 fw.write('//turn off auto surround block\n')
# fw.write('TrialList.Current.BeamList.Current.SetBeamType = \"Step & Shoot MLC\";\n')
 fw.write('TrialList.Current.BeamList.Current.AutoSurround = 0;\n')
 fw.write('//add empty block to first control point\n')
 fw.write('TrialList.Current.BeamList.Current.AddModifier = "Add Block";\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ModifierList.Last.MakeCurrent = "Add Block";\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ModifierList.Current.InsideMode = "Block";\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ModifierList.Current.ReorderMinusOne = " 1";\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ModifierList.Current.ChangeNotify = " 1";\n')
 fw.write('//turn store control point dose on//\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.StoreCPDose = 1;\n')
 fw.write('//add control points//\n')
 for ii in range(nCP):
  fw.write('TrialList.Current.BeamList.Current.CPManager.AddControlPoint = "Add Control Point";\n')
  fw.write('TrialList.Current.BeamList.Current.CPManager.ControlPointList.Last.WeightLocked = 1;\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ControlPointList.#"#0".MakeCurrent = 1;\n')
 fw.write('//Delete empty block in first control point//\n')
 fw.write('TrialList.Current.BeamList.Current.RemoveCurrentModifier = "Delete Block";\n')
 fw.close()

 fw = open(savFolder+'addCPAllB.Script','w')
 fw.write('////////////////////////\n')
 fw.write('////addCPAllB.Script////\n')
 fw.write('////////////////////////\n')
 fw.write('\n')
 fw.write('TrialList.Current.BeamList.ChildrenEachCurrent.#"@".Script.ExecuteNow = "%saddCP.Script";\n' %savFolder)
 fw.write('WindowList.BeamSegments.Create = "Control Points...";\n')
 fw.write('TrialList.Current.BeamList.#"#0".MakeCurrent = 1;\n')
 fw.write('TrialList.Current.BeamList.Current.CPManager.ModifierList.#"#0".MakeCurrent = 1;\n')
 fw.close()

if __name__ == "__main__":
 savFolder = str(sys.argv[1])
 nCP = int(sys.argv[2])
 write(savFolder, nCP)
