BeautifulJason (https://pypi.org/project/beautifuljason/) scripts to perform quality control tasks.

Styrene-butadiene rubber
STYRENE-BUTADIENE RUBBER SCRIPTS
The following are scripts based on the ISO 21561-1:2015 (https://cdn.standards.iteh.ai/samples/66501/6f65c8e942c04a1997eb1d2537436998/ISO-21561-1-2015.pdf):

SBR_analysis_with_blank_hdf5.py is as specified in the ISO method

SBR_analysis_simple_hdf5.py ignores the residual solvent contribution

SBR_analysis_solventsubtraction.py subtracts the residual solvent contribution by using Jason automatic solvent detection and peak deconvolution. It is also coded purely with BeautifulJason instead of using h5py
