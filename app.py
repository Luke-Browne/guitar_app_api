import json
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
keys = pd.DataFrame([
    ['C_maj','D_min','E_min','F_maj','G_maj','A_min','Bb_min'],
    ['Cs_maj','Eb_min','F_min','Fs_maj','Gs_maj','Bb_min','C_min'],
    ['D_maj','E_min','Fs_min','G_maj','A_maj','B_min','Cs_min'],
    ['Eb_maj','F_min','G_min','Gs_maj','Bb_maj','C_min','D_min'],
    ['E_maj','Fs_min','Gs_min','A_maj','C_maj','Cs_min','Eb_min'],
    ['F_maj','G_min','A_min','Bb_maj','Cs_maj','D_min','E_min'],
    ['Fs_maj','Gs_min','Bb_min','C_maj','D_maj','Eb_min','F_min'],
    ['G_maj','A_min','C_min','Cs_maj','Eb_maj','E_min','Fs_min'],
    ['Gs_maj','Bb_min','Cs_min','D_maj','E_maj','F_min','G_min'],
    ['A_maj','B_min','D_min','Eb_maj','F_maj','Fs_min','Gs_min'],
    ['Bb_maj','C_min','Eb_min','E_maj','Fs_maj','G_min','A_min'],
    ['B_maj','Cs_min','E_min','F_maj','G_maj','Gs_min','Bb_min'],
        
    ['C_min','D_dim','Eb_maj','F_min','G_min','Gs_maj','Bb_maj'],
    ['Cs_min','Eb_dim','E_maj','Fs_min','Gs_min','A_maj','B_maj'],
    ['D_min','E_dim','F_maj','G_min','A_min','Bb_maj','C_maj'],
    ['Ds_min','F_dim','Fs_maj','Gs_min','Bb_min','C_maj','Cs_maj'],
    ['E_min','Fs_dim','G_maj','A_min','B_min','Cs_maj','D_maj'],
    ['F_min','G_dim','Gs_maj','Bb_min','C_min','D_maj','Ds_maj'],
    ['Fs_min','Gs_dim','A_maj','B_min','Cs_min','Ds_maj','E_maj'],
    ['G_min','A_dim','Bb_maj','C_min','D_min','E_maj','F_maj'],
    ['Gs_min','Bb_dim','C_maj','Cs_min','Ds_min','F_maj','Fs_maj'],
    ['A_min','B_dim','Cs_maj','D_min','E_min','Fs_maj','G_maj'],
    ['Bb_min','C_dim','D_maj','Ds_min','F_min','G_maj','Gs_maj'],
    ['B_min','Cs_dim','Ds_maj','E_min','Fs_min','Gs_maj','A_maj']    
])

chords = []
finalChords = []
ChordsForProgression = []

def Gen_CMaj():
    chords = keys.iloc[[0]]
    return chords
def Gen_CsMaj():
    chords = keys.iloc[[1]]
    return chords
def Gen_DMaj():
    chords = keys.iloc[[2]]
    return chords
def Gen_EfMaj():
    chords = keys.iloc[[3]]
    return chords
def Gen_EMaj():
    chords = keys.iloc[[4]]
    return chords
def Gen_FMaj():
    chords = keys.iloc[[5]]
    return chords
def Gen_FsMaj():
    chords = keys.iloc[[6]]
    return chords
def Gen_GMaj():
    chords = keys.iloc[[7]]
    return chords
def Gen_GsMaj():
    chords = keys.iloc[[8]]
    return chords
def Gen_AMaj():
    chords = keys.iloc[[9]]
    return chords
def Gen_BfMaj():
    chords = keys.iloc[[10]]
    return chords
def Gen_BMaj():
    chords = keys.iloc[[11]]
    return chords

# Take a look at the chord/key data
keys.head(12)
@app.route('/keys',methods=['GET'])
def get_chords():
    key = str(request.args['key'])
    pattern = str(request.args['pattern'])
    print('selected pattern: ' + pattern)

    if(pattern == 'I-V-vi-IV'):
        progression = 1
    elif(pattern == 'I-IV-V-IV'):
        progression = 2
    elif(pattern == 'ii-V-I'):
        progression = 3
    elif(pattern == '12BarBlues'):
        progression = 4
    elif(pattern == 'I-vi-IV-V'):
        progression = 5
    elif(pattern == 'Canon'):
        progression = 6
    else:
        progression = 1

    options = {'CMajor': Gen_CMaj(), 'CsMajor': Gen_CsMaj(), 'DMajor': Gen_DMaj(), 'EfMajor': Gen_EfMaj(), 'EMajor': Gen_EMaj(), 'FMajor': Gen_FMaj(), 'FsMajor': Gen_FsMaj(), 'GMajor': Gen_GMaj(), 'GsMajor': Gen_GsMaj(), 'AMajor': Gen_AMaj(), 'BfMajor': Gen_BfMaj(), 'BMajor': Gen_BMaj()}
    ChordsForProgression = options.get(key)
    print(ChordsForProgression)

    if(progression == 1):
        finalChords = ''
        finalChords = ChordsForProgression[0] + ',' + ChordsForProgression[4] + ',' + ChordsForProgression[5] + ',' + ChordsForProgression[3]
        print(finalChords)
        return finalChords.to_json()
    if(progression == 2):
        finalChords = ''
        finalChords = ChordsForProgression[0] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[4] + ',' + ChordsForProgression[3]
        print(finalChords)
        return finalChords.to_json()
    if(progression == 3):
        finalChords = ''
        finalChords = ChordsForProgression[1] + ',' + ChordsForProgression[4] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[0]
        print(finalChords)
        return finalChords.to_json()
    if(progression == 4):
        finalChords = ''
        finalChords = ChordsForProgression[0] + ','  + ChordsForProgression[0] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[4] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[0]
        print(finalChords)
        return finalChords.to_json()
    if(progression == 5):
        finalChords = ''
        finalChords = ChordsForProgression[0] + ',' + ChordsForProgression[5] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[4]
        print(finalChords)
        return finalChords.to_json()
    if(progression == 6):
        finalChords = ''
        finalChords = ChordsForProgression[0] + ',' + ChordsForProgression[4] + ',' + ChordsForProgression[5] + ',' + ChordsForProgression[2] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[0] + ',' + ChordsForProgression[3] + ',' + ChordsForProgression[4]
        print(finalChords)
        return finalChords.to_json()

app.run(debug=True, host="192.168.1.16")
