import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

# Step 2: Reading FITS Data
def read_fits(filename):
    hdulist = fits.open(filename)
    return hdulist[0].data

# Step 3: Master Bias Creation
def create_master_bias(bias_frames):
    return np.mean(bias_frames, axis=0)

# Step 5: Flat Frame Correction
def correct_flat_frame(flat_frame, master_bias, dark_frame):
    flat_frame_corrected = flat_frame - master_bias
    flat_frame_corrected -= dark_frame
    return flat_frame_corrected

# Step 6: Statistics Calculation
def calculate_statistics(data):
    stats = {'max': np.max(data), 'min': np.min(data), 'mean': np.mean(data), 'std': np.std(data)}
    return stats

# Step 7: Flat Frame Normalization
def normalize_flat_frame(flat_frame_corrected):
    return flat_frame_corrected / np.mean(flat_frame_corrected)

# Step 8: Science Frame Correction
def correct_science_frame(science_frame, master_bias, dark_frame, flat_frame_normalized):
    science_frame_corrected = science_frame - master_bias
    science_frame_corrected -= dark_frame
    science_frame_corrected /= flat_frame_normalized
    return science_frame_corrected

# Step 10: Data Writing
def write_fits(data, filename):
    fits.writeto(filename, data, overwrite=True)

# Step 11: Plotting Color Maps
def plot_color_map(data, title):
    plt.imshow(data, cmap='gray')
    plt.colorbar()
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    # Step 1: Image Acquisition - Download FITS files manually

    # Step 2: Reading FITS Data
    bias_frames = [
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b01.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b02.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b03.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b04.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b05.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b06.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b07.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b08.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b09.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b10.fits'),
    read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Bias/b11.fits')
]  # list of bias frames
    dark_frame = read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Dark/dark_300s.fits')
    flat_frame = read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Flat/Flat_B_50s.fits',)
    science_frame = read_fits('http://www.phyast.pitt.edu/~wmwv/Classes/A1263/Labs/Lab3/images/Light/NGC_2194B.fits')

    # Step 3: Master Bias Creation
    master_bias = create_master_bias(bias_frames)

    # Step 5: Flat Frame Correction
    flat_frame_corrected = correct_flat_frame(flat_frame, master_bias, dark_frame)

    # Step 6: Statistics Calculation
    stats_master_flat = calculate_statistics(flat_frame_corrected)
    print("Master Flat Frame Statistics:", stats_master_flat)

    # Step 7: Flat Frame Normalization
    flat_frame_normalized = normalize_flat_frame(flat_frame_corrected)

    # Step 8: Science Frame Correction
    science_frame_corrected = correct_science_frame(science_frame, master_bias, dark_frame, flat_frame_normalized)

    # Step 10: Data Writing
    write_fits(science_frame_corrected, 'reduced_science_frame.fits')

    # Step 11: Plotting Color Maps
    plot_color_map(master_bias, 'Master Bias Frame')
    plot_color_map(dark_frame, 'Dark Frame')
    plot_color_map(flat_frame, 'Flat Frame')
    plot_color_map(flat_frame_corrected, 'Corrected Flat Frame')
    plot_color_map(flat_frame_normalized, 'Normalized Flat Frame')
    plot_color_map(science_frame, 'Science Frame')
    plot_color_map(science_frame_corrected, 'Corrected Science Frame')

    # Save the outputs as FITS files
    write_fits(master_bias, 'master_bias.fits')
    write_fits(dark_frame, 'dark_frame.fits')
    write_fits(flat_frame, 'flat_frame.fits')
    write_fits(flat_frame_corrected, 'corrected_flat_frame.fits')
    write_fits(flat_frame_normalized, 'normalized_flat_frame.fits')
    write_fits(science_frame, 'science_frame.fits')
    write_fits(science_frame_corrected, 'corrected_science_frame.fits')


