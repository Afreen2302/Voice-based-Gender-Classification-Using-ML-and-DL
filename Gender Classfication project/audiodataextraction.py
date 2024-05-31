import librosa
import numpy as np
from scipy.stats import skew, kurtosis

def extract_audio_features(audio_file_path):
    # Load audio file using librosa, 'y' contains the audio time series, and 'sr' is the sampling rate
    y, sr = librosa.load(audio_file_path, sr=None)
    
    # Calculate mean of the spectral centroid
    meanfreq = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    
    # Calculate standard deviation of the spectral centroid
    sd = np.std(librosa.feature.spectral_centroid(y=y, sr=sr))
    
    # Calculate median of the audio signal
    median = np.median(y)
    
    # Calculate the 25th percentile (first quartile) of the audio signal
    Q25 = np.percentile(y, 25)
    
    # Calculate the 75th percentile (third quartile) of the audio signal
    Q75 = np.percentile(y, 75)
    
    # Calculate the interquartile range (IQR)
    IQR = Q75 - Q25
    
    # Calculate skewness and kurtosis of the spectral centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    skewness = skew(spectral_centroid)
    kurt = kurtosis(spectral_centroid)
    
    # Calculate spectral flatness measures
    sp_ent = np.mean(librosa.feature.spectral_flatness(y=y))
    sfm = np.mean(librosa.feature.spectral_flatness(y=y))
    
    # Calculate the mean of the spectral centroid
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    
    # Calculate mode of the audio signal using NumPy
    mode_value = float(np.argmax(np.bincount(y.astype(int))))
    
    # Calculate pitch-related features
    pitches = librosa.core.pitch_tuning(y)
    meanfun = np.mean(pitches)
    minfun = np.min(pitches)
    maxfun = np.max(pitches)
    meandom = np.mean(librosa.feature.tempogram(y=y, sr=sr))
    mindom = np.min(librosa.feature.tempogram(y=y, sr=sr))
    maxdom = np.max(librosa.feature.tempogram(y=y, sr=sr))
    dfrange = (maxdom - mindom)
    modindx = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))

    # Store the extracted features in a dictionary
    return {
        'meanfreq': [meanfreq],
        'sd': [sd],
        'median': [median],
        'Q25': [Q25],
        'Q75': [Q75],
        'IQR': [IQR],
        'skew': [skewness],
        'kurt': [kurt],
        'sp.ent': [sp_ent],
        'sfm': [sfm],
        'mode': [mode_value],
        'centroid': [centroid],
        'meanfun': [meanfun],
        'minfun': [minfun],
        'maxfun': [maxfun],
        'meandom': [meandom],
        'mindom': [mindom],
        'maxdom': [maxdom],
        'dfrange': [dfrange],
        'modindx': [modindx],
    }

# Path to the audio file
audio_file_path = 'C:\Gender Classfication project\Gender Classfication project\path\girl_1.mp3'

# Extract features from the audio file
features = extract_audio_features(audio_file_path)

# Print the extracted features
print(features)
